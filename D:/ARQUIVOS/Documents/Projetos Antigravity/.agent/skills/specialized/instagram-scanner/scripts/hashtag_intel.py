#!/usr/bin/env python3
"""
Inteligência de Hashtags do Instagram
Camada 3: Enriquecimento - Análise de hashtags

Analisa performance de hashtags, detecta shadowban, sugere alternativas.
"""

import argparse
import json
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Set
from collections import defaultdict, Counter


class HashtagIntelligence:
    """Sistema de inteligência de hashtags."""
    
    COMMON_BANNED_HASHTAGS = {
        '#adulting', '#alone', '#always', '#assday', '#attractive',
        '#babe', '#badbitcztwerk', '#balenciaga', '#beautyblogger',
        '#bikinibody', '#boho', '#brain', '#bra', '#costumes',
        '#curvygirls', '#date', '#dating', '#desk', '#direct',
        '#dm', '#dogsofinstagram', '#elevator', '#eggplant',
        '#fitnessgirls', '#gloves', '#goddess', '#graffitiigers',
        '#hardworkpaysoff', '#humpday', '#ice', '#instamood',
        '#italiano', '#kansas', '#kickoff', '#kissing', '#lean',
        '#like', '#lingerie', '#master', '#models', '#mustfollow',
        '#nasty', '#newyears', '#newyearsday', '#overnight',
        '#parties', '#petite', '#popular', '#pornfood', '#pushups',
        '#rate', '#ravens', '#saltwater', '#selfharm', '#sexy',
        '#single', '#skateboarding', '#skype', '#snap', '#snapchat',
        '#snowstorm', '#sopretty', '#stranger', '#streetphoto',
        '#sunbathing', '#swole', '#tanlines', '#teens', '#tgif',
        '#thinspo', '#thought', '#tinder', '#todayimwearing',
        '#undies', '#valentinesday', '#woman', '#workflow',
        '#wshh', '#young'
    }
    
    def __init__(self, posts_data: List[Dict], config: Dict = None):
        self.posts = posts_data
        self.config = config or {}
        self.blacklist_path = self.config.get('hashtag_blacklist_path')
        self.min_posts_for_analysis = self.config.get('min_hashtag_performance_posts', 10)
        
        self.custom_blacklist: Set[str] = set()
        if self.blacklist_path and Path(self.blacklist_path).exists():
            with open(self.blacklist_path, 'r', encoding='utf-8') as f:
                for line in f:
                    tag = line.strip().lower()
                    if tag and not tag.startswith('#'):
                        tag = '#' + tag
                    if tag:
                        self.custom_blacklist.add(tag)
    
    def _extract_hashtags_from_text(self, text: str) -> List[str]:
        if not text:
            return []
        pattern = r'#[\w\u00C0-\u024F\u1E00-\u1EFF]+'
        matches = re.findall(pattern, text, re.UNICODE)
        return [tag.lower() for tag in matches]
    
    def _extract_all_hashtags(self) -> Dict[str, List[int]]:
        hashtag_to_posts = defaultdict(list)
        for idx, post in enumerate(self.posts):
            caption = post.get('caption_text', '')
            hashtags = self._extract_hashtags_from_text(caption)
            for tag in hashtags:
                hashtag_to_posts[tag].append(idx)
        return dict(hashtag_to_posts)
    
    def analyze_hashtag_frequency(self) -> Dict[str, Any]:
        hashtag_to_posts = self._extract_all_hashtags()
        total_posts_with_hashtags = sum(1 for p in self.posts if self._extract_hashtags_from_text(p.get('caption_text', '')))
        
        frequency = {tag: len(posts) for tag, posts in hashtag_to_posts.items()}
        top_20 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:20]
        unique_count = len(frequency)
        
        all_tags_in_posts = []
        for post in self.posts:
            tags = self._extract_hashtags_from_text(post.get('caption_text', ''))
            all_tags_in_posts.extend(tags)
        
        avg_per_post = len(all_tags_in_posts) / len(self.posts) if self.posts else 0
        
        categories = {"overused (>50% posts)": 0, "frequent (20-50% posts)": 0,
                      "moderate (10-20% posts)": 0, "occasional (5-10% posts)": 0, "rare (<5% posts)": 0}
        
        for tag, count in frequency.items():
            pct = count / len(self.posts) if self.posts else 0
            if pct > 0.5: categories["overused (>50% posts)"] += 1
            elif pct > 0.2: categories["frequent (20-50% posts)"] += 1
            elif pct > 0.1: categories["moderate (10-20% posts)"] += 1
            elif pct > 0.05: categories["occasional (5-10% posts)"] += 1
            else: categories["rare (<5% posts)"] += 1
        
        return {
            "total_unique_hashtags": unique_count,
            "posts_using_hashtags": total_posts_with_hashtags,
            "avg_hashtags_per_post": round(avg_per_post, 2),
            "top_20_most_used": [{"hashtag": tag, "count": count} for tag, count in top_20],
            "usage_distribution": categories
        }
    
    def detect_banned_hashtags(self) -> Dict[str, Any]:
        hashtag_to_posts = self._extract_all_hashtags()
        all_hashtags = set(hashtag_to_posts.keys())
        all_banned = self.COMMON_BANNED_HASHTAGS.union(self.custom_blacklist)
        found_banned = all_hashtags.intersection(all_banned)
        
        banned_details = []
        for tag in found_banned:
            banned_details.append({
                "hashtag": tag,
                "times_used": len(hashtag_to_posts.get(tag, [])),
                "source": "common_blacklist" if tag in self.COMMON_BANNED_HASHTAGS else "custom_blacklist",
                "risk_level": "high"
            })
        
        return {
            "banned_hashtags_found": len(found_banned),
            "banned_list": sorted([t for t in found_banned]),
            "details": banned_details,
            "recommendation": "Remova imediatamente estas hashtags para evitar shadowban" if found_banned else "Nenhuma hashtag banida detectada"
        }
    
    def analyze_hashtag_performance(self) -> Dict[str, Any]:
        if len(self.posts) < self.min_posts_for_analysis:
            return {"success": False, "error": f"Mínimo de {self.min_posts_for_analysis} posts necessário"}
        
        hashtag_to_posts = self._extract_all_hashtags()
        performance_data = []
        
        for tag, post_indices in hashtag_to_posts.items():
            if len(post_indices) < 2:
                continue
            
            engagements = []
            for idx in post_indices:
                post = self.posts[idx]
                likes = post.get('likes_count', 0) or 0
                comments = post.get('comments_count', 0) or 0
                engagements.append(likes + comments * 2)
            
            avg_engagement = sum(engagements) / len(engagements)
            performance_data.append({
                "hashtag": tag, "posts_count": len(post_indices),
                "avg_engagement": round(avg_engagement, 2),
                "max_engagement": max(engagements), "min_engagement": min(engagements)
            })
        
        performance_data.sort(key=lambda x: x['avg_engagement'], reverse=True)
        
        insights = []
        if performance_data:
            best = performance_data[0]
            insights.append(f"A hashtag #{best['hashtag']} tem o maior engajamento médio ({best['avg_engagement']})")
        
        return {
            "success": True,
            "hashtags_analyzed": len(performance_data),
            "top_performers": performance_data[:15],
            "worst_performers": performance_data[-10:] if len(performance_data) > 10 else [],
            "insights": insights
        }
    
    def suggest_related_hashtags(self, niche_keywords: List[str] = None) -> Dict[str, Any]:
        all_captions = ' '.join([p.get('caption_text', '') for p in self.posts])
        stopwords_pt = {'de', 'do', 'da', 'em', 'um', 'uma', 'o', 'a', 'os', 'as', 'que', 'e', 'é', 'para', 'com', 'não', 'se', 'na', 'no', 'por', 'mais', 'como', 'mas'}
        
        words = re.findall(r'\b\w+\b', all_captions.lower())
        word_freq = Counter(w for w in words if w not in stopwords_pt and len(w) > 3)
        top_keywords = word_freq.most_common(20)
        
        suggestions = []
        for keyword, freq in top_keywords[:10]:
            variations = [f"#{keyword}", f"#{keyword}brasil", f"#{keyword}br", f"#dicasde{keyword}", f"#{keyword}digital"]
            suggestions.extend(variations)
        
        suggestions = list(set(s for s in suggestions if len(s) <= 30))
        
        return {
            "detected_keywords": [{"word": w, "frequency": f} for w, f in top_keywords],
            "suggested_hashtags": suggestions[:30],
            "tip": "Combine hashtags de nicho específico com hashtags de volume médio"
        }
    
    def run_full_analysis(self, niche_keywords: List[str] = None) -> Dict[str, Any]:
        results = {
            "analysis_date": datetime.now().isoformat(),
            "posts_analyzed": len(self.posts),
            "frequency_analysis": self.analyze_hashtag_frequency(),
            "banned_detection": self.detect_banned_hashtags(),
            "performance_analysis": self.analyze_hashtag_performance(),
            "suggestions": self.suggest_related_hashtags(niche_keywords)
        }
        results["hashtag_quality_score"] = self._calculate_quality_score(results)
        return results
    
    def _calculate_quality_score(self, results: Dict) -> float:
        score = 10.0
        banned_count = results['banned_detection']['banned_hashtags_found']
        if banned_count > 0:
            score -= min(banned_count * 1.5, 5.0)
        
        avg_per_post = results['frequency_analysis']['avg_hashtags_per_post']
        if avg_per_post < 3: score -= 2.0
        elif avg_per_post > 30: score -= 1.5
        
        unique_hashtags = results['frequency_analysis']['total_unique_hashtags']
        if unique_hashtags > 50: score += 1.0
        elif unique_hashtags > 20: score += 0.5
        
        return max(0.0, min(10.0, score))


def main():
    parser = argparse.ArgumentParser(description="Inteligência de Hashtags")
    parser.add_argument("--input", "-i", required=True, help="JSON de posts")
    parser.add_argument("--output", "-o", default=None, help="Saída JSON")
    parser.add_argument("--config", "-c", default="config.yaml", help="Configuração")
    parser.add_argument("--keywords", nargs='+', default=None, help="Palavras-chave")
    
    args = parser.parse_args()
    
    config = {}
    if Path(args.config).exists():
        import yaml
        with open(args.config, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    
    with open(args.input, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    analyzer = HashtagIntelligence(posts, config)
    results = analyzer.run_full_analysis(args.keywords)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✅ Análise salva em {args.output}")
    else:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    
    return 0 if results.get('hashtag_quality_score', 0) >= 5 else 1


if __name__ == "__main__":
    sys.exit(main())
