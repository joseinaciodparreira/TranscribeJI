#!/usr/bin/env python3
"""
Análise Temporal do Instagram
Camada 3: Enriquecimento - Features temporais

Analisa padrões de postagem, melhores horários, frequência ideal e tendências.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict

import pandas as pd
import duckdb


class TemporalAnalyzer:
    """Analisa padrões temporais de posts do Instagram."""
    
    def __init__(self, posts_data: List[Dict], config: Dict = None):
        self.posts = posts_data
        self.config = config or {}
        self.min_posts = self.config.get('min_posts_for_temporal', 20)
        
        # Mapeamento de dias da semana em português
        self.day_names = {
            0: 'Segunda',
            1: 'Terça',
            2: 'Quarta',
            3: 'Quinta',
            4: 'Sexta',
            5: 'Sábado',
            6: 'Domingo'
        }
    
    def _parse_dates(self) -> Optional[pd.DataFrame]:
        """Converte posts para DataFrame com datas parseadas."""
        if len(self.posts) < self.min_posts:
            return None
        
        df_data = []
        for post in self.posts:
            published_at = post.get('published_at')
            if not published_at:
                continue
            
            try:
                dt = pd.to_datetime(published_at)
                df_data.append({
                    'shortcode': post.get('shortcode'),
                    'published_at': dt,
                    'day_of_week': dt.dayofweek,
                    'hour': dt.hour,
                    'likes_count': post.get('likes_count', 0) or 0,
                    'comments_count': post.get('comments_count', 0) or 0,
                    'content_type': post.get('content_type', 'image'),
                    'caption_text': post.get('caption_text', '')
                })
            except:
                continue
        
        if len(df_data) < self.min_posts:
            return None
        
        return pd.DataFrame(df_data)
    
    def analyze_best_posting_times(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Identifica melhores horários para postar."""
        # Agrupa por dia da semana e hora
        df['engagement'] = df['likes_count'] + df['comments_count'] * 2
        
        hourly_performance = df.groupby(['day_of_week', 'hour']).agg({
            'engagement': ['mean', 'count'],
            'shortcode': 'count'
        }).reset_index()
        
        hourly_performance.columns = ['day_of_week', 'hour', 'avg_engagement', 'total_posts']
        
        # Melhores combinações
        best_times = hourly_performance.nlargest(10, 'avg_engagement')
        
        result = {
            "top_10_times": [],
            "by_day": {},
            "recommendations": []
        }
        
        for _, row in best_times.iterrows():
            day_name = self.day_names.get(row['day_of_week'], 'Desconhecido')
            result["top_10_times"].append({
                "day": day_name,
                "day_index": int(row['day_of_week']),
                "hour": int(row['hour']),
                "formatted_time": f"{int(row['hour']):02d}:00",
                "avg_engagement": float(row['avg_engagement']),
                "posts_count": int(row['total_posts'])
            })
        
        # Por dia da semana
        for day_idx in range(7):
            day_data = hourly_performance[hourly_performance['day_of_week'] == day_idx]
            if len(day_data) > 0:
                best_hour_row = day_data.loc[day_data['avg_engagement'].idxmax()]
                result["by_day"][self.day_names[day_idx]] = {
                    "best_hour": int(best_hour_row['hour']),
                    "avg_engagement": float(best_hour_row['avg_engagement'])
                }
        
        # Recomendações
        if len(result["top_10_times"]) > 0:
            top_3 = result["top_10_times"][:3]
            result["recommendations"] = [
                f"Postar às {t['formatted_time']} na {t['day']} (engajamento médio: {t['avg_engagement']:.1f})"
                for t in top_3
            ]
        
        return result
    
    def analyze_posting_frequency(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analisa frequência de postagem."""
        df_sorted = df.sort_values('published_at')
        
        # Calcula intervalos entre posts
        df_sorted['time_diff'] = df_sorted['published_at'].diff()
        
        # Frequência média
        avg_days_between = df_sorted['time_diff'].dt.total_seconds().mean() / 86400
        avg_hours_between = df_sorted['time_diff'].dt.total_seconds().mean() / 3600
        
        # Posts por semana
        date_range = (df_sorted['published_at'].max() - df_sorted['published_at'].min()).days
        weeks = max(date_range / 7, 1)
        posts_per_week = len(df) / weeks
        
        # Consistência
        std_days = df_sorted['time_diff'].dt.total_seconds().std() / 86400 if len(df_sorted) > 1 else 0
        
        # Distribuição por tipo de conteúdo
        content_dist = df.groupby('content_type').size().to_dict()
        
        return {
            "avg_days_between_posts": round(avg_days_between, 2) if pd.notna(avg_days_between) else None,
            "avg_hours_between_posts": round(avg_hours_between, 2) if pd.notna(avg_hours_between) else None,
            "posts_per_week": round(posts_per_week, 2),
            "consistency_score": self._calculate_consistency_score(std_days, avg_days_between),
            "consistency_std_days": round(std_days, 2) if pd.notna(std_days) else None,
            "date_range_days": date_range,
            "total_posts_analyzed": len(df),
            "content_type_distribution": content_dist,
            "frequency_recommendation": self._get_frequency_recommendation(posts_per_week, std_days)
        }
    
    def _calculate_consistency_score(self, std_days: float, avg_days: float) -> float:
        """Calcula score de consistência (0-10)."""
        if pd.isna(std_days) or pd.isna(avg_days) or avg_days == 0:
            return 0.0
        
        # Coeficiente de variação
        cv = std_days / avg_days if avg_days > 0 else 999
        
        # Score baseado no CV (menor CV = mais consistente)
        if cv < 0.3:
            return 10.0
        elif cv < 0.5:
            return 8.0
        elif cv < 0.7:
            return 6.0
        elif cv < 1.0:
            return 4.0
        else:
            return 2.0
    
    def _get_frequency_recommendation(self, posts_per_week: float, std_days: float) -> str:
        """Gera recomendação de frequência."""
        if posts_per_week < 3:
            return "Aumente a frequência para pelo menos 3-4 posts por semana"
        elif posts_per_week < 5:
            if std_days and std_days > 2:
                return "Mantenha a frequência mas melhore a consistência (regularidade)"
            return "Frequência adequada, mantenha a regularidade"
        elif posts_per_week < 10:
            return "Ótima frequência! Foque em consistência e qualidade"
        else:
            return "Frequência muito alta - avalie se há burnout ou perda de qualidade"
    
    def analyze_growth_trend(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analisa tendência de engajamento ao longo do tempo."""
        df_sorted = df.sort_values('published_at')
        
        # Rolling average de engajamento
        df_sorted['engagement'] = df_sorted['likes_count'] + df_sorted['comments_count'] * 2
        df_sorted['rolling_avg'] = df_sorted['engagement'].rolling(window=5, min_periods=1).mean()
        
        # Tendência (slope simples)
        if len(df_sorted) > 5:
            first_half = df_sorted.head(len(df_sorted)//2)['engagement'].mean()
            second_half = df_sorted.tail(len(df_sorted)//2)['engagement'].mean()
            
            if second_half > first_half * 1.2:
                trend = "crescente"
                trend_score = 8.0
            elif second_half > first_half * 1.05:
                trend = "levemente_crescente"
                trend_score = 6.5
            elif second_half > first_half * 0.95:
                trend = "estavel"
                trend_score = 5.0
            elif second_half > first_half * 0.8:
                trend = "levemente_decrescente"
                trend_score = 3.5
            else:
                trend = "decrescente"
                trend_score = 2.0
        else:
            trend = "insuficiente_dados"
            trend_score = 5.0
        
        return {
            "trend": trend,
            "trend_score": trend_score,
            "first_half_avg_engagement": round(first_half, 2) if 'first_half' in dir() else None,
            "second_half_avg_engagement": round(second_half, 2) if 'second_half' in dir() else None,
            "change_percent": round((second_half - first_half) / first_half * 100, 2) if 'first_half' in dir() and first_half > 0 else None
        }
    
    def run_full_analysis(self) -> Dict[str, Any]:
        """Executa análise temporal completa."""
        df = self._parse_dates()
        
        if df is None:
            return {
                "success": False,
                "error": f"Dados insuficientes para análise temporal. Mínimo necessário: {self.min_posts} posts com data.",
                "posts_available": len(self.posts)
            }
        
        results = {
            "success": True,
            "analysis_date": datetime.now().isoformat(),
            "posts_analyzed": len(df),
            "date_range": {
                "start": df['published_at'].min().isoformat(),
                "end": df['published_at'].max().isoformat(),
                "days": (df['published_at'].max() - df['published_at'].min()).days
            },
            "best_posting_times": self.analyze_best_posting_times(df),
            "posting_frequency": self.analyze_posting_frequency(df),
            "growth_trend": self.analyze_growth_trend(df)
        }
        
        return results


def main():
    parser = argparse.ArgumentParser(description="Análise Temporal do Instagram")
    parser.add_argument("--input", "-i", required=True, help="Caminho para arquivo JSON de posts")
    parser.add_argument("--output", "-o", default=None, help="Caminho para arquivo de saída JSON")
    parser.add_argument("--min-posts", type=int, default=20, help="Mínimo de posts para análise")
    
    args = parser.parse_args()
    
    # Carrega posts
    with open(args.input, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    analyzer = TemporalAnalyzer(posts, {'min_posts_for_temporal': args.min_posts})
    results = analyzer.run_full_analysis()
    
    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✅ Análise salva em {args.output}")
    else:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    
    return 0 if results.get('success') else 1


if __name__ == "__main__":
    sys.exit(main())
