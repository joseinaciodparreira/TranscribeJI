"""
Instagram Data Normalizer - Camada de Normalização

Transforma dados brutos do Instagram em entidades consistentes e estruturadas.
Aplica regras de limpeza, padronização e extração de features básicas.
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
import argparse


class InstagramNormalizer:
    """Normaliza dados brutos do Instagram para estrutura consistente."""
    
    def __init__(self):
        pass
    
    def normalize_date(self, date_str: Optional[str]) -> Optional[str]:
        """
        Normaliza datas para formato ISO 8601.
        
        Aceita múltiplos formatos e retorna YYYY-MM-DDTHH:MM:SS
        """
        if not date_str:
            return None
        
        # Se já estiver em ISO, retorna
        try:
            datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return date_str
        except:
            pass
        
        # Tenta parsear formatos comuns
        formats = [
            "%d/%m/%Y",
            "%Y-%m-%d",
            "%d %b %Y",
            "%B %d, %Y",
            "%d de %B de %Y"
        ]
        
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt.isoformat()
            except:
                continue
        
        return date_str  # Retorna original se não conseguir parsear
    
    def parse_count(self, count_value: Any) -> Optional[int]:
        """
        Converte contagens para inteiro.
        
        Lida com formatos como '1.2K', '1,234', '1.234', etc.
        """
        if count_value is None:
            return None
        
        if isinstance(count_value, int):
            return count_value
        
        if isinstance(count_value, float):
            return int(count_value)
        
        text = str(count_value).strip().upper()
        
        # Remove espaços
        text = text.replace(" ", "")
        
        # Verifica sufixos K, M, B
        multiplier = 1
        if text.endswith("K"):
            multiplier = 1000
            text = text[:-1]
        elif text.endswith("M"):
            multiplier = 1000000
            text = text[:-1]
        elif text.endswith("B"):
            multiplier = 1000000000
            text = text[:-1]
        
        # Substitui vírgula por ponto se necessário
        if "," in text and "." not in text:
            text = text.replace(",", ".")
        elif "," in text and "." in text:
            # Formato europeu: 1.234,56
            text = text.replace(".", "").replace(",", ".")
        
        try:
            return int(float(text) * multiplier)
        except:
            return None
    
    def clean_text(self, text: Optional[str]) -> Optional[str]:
        """
        Limpa texto de quebras estranhas e caracteres especiais.
        """
        if not text:
            return None
        
        # Remove quebras de linha múltiplas
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        # Remove espaços extras
        text = re.sub(r' +', ' ', text)
        
        # Remove caracteres de controle
        text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t')
        
        return text.strip()
    
    def extract_hashtags(self, text: str) -> List[str]:
        """Extrai hashtags de um texto."""
        if not text:
            return []
        
        hashtags = re.findall(r'#(\w+)', text, re.UNICODE)
        return [tag.lower() for tag in hashtags]
    
    def extract_mentions(self, text: str) -> List[str]:
        """Extrai menções de um texto."""
        if not text:
            return []
        
        mentions = re.findall(r'@(\w+)', text, re.UNICODE)
        return [mention.lower() for mention in mentions]
    
    def extract_links(self, text: str) -> List[str]:
        """Extrai URLs de um texto."""
        if not text:
            return []
        
        pattern = r'(https?://[^\s<>"{}|\\^`\[\]]+)'
        links = re.findall(pattern, text, re.UNICODE)
        return links
    
    def detect_language(self, text: str) -> str:
        """Detecta idioma predominante do texto (heurística simples)."""
        if not text:
            return "unknown"
        
        # Palavras indicativas por idioma
        pt_words = ['o', 'a', 'de', 'da', 'do', 'em', 'um', 'uma', 'para', 'com', 'não', 'sou', 'eu', 'meu', 'minha']
        en_words = ['the', 'a', 'of', 'in', 'to', 'and', 'is', 'i', 'my', 'me', 'you', 'your', 'for', 'with']
        es_words = ['el', 'la', 'de', 'en', 'un', 'una', 'para', 'con', 'no', 'soy', 'yo', 'mi', 'tu']
        
        words = text.lower().split()
        
        pt_count = sum(1 for word in words if word in pt_words)
        en_count = sum(1 for word in words if word in en_words)
        es_count = sum(1 for word in words if word in es_words)
        
        counts = {'pt': pt_count, 'en': en_count, 'es': es_count}
        max_lang = max(counts, key=counts.get)
        
        return max_lang if counts[max_lang] > 0 else "unknown"
    
    def normalize_profile(self, raw_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Normaliza dados do perfil."""
        profile = {
            "profile_id": raw_profile.get("username", "").lower(),
            "username": raw_profile.get("username"),
            "display_name": self.clean_text(raw_profile.get("display_name")),
            "bio_text": self.clean_text(raw_profile.get("bio_text")),
            "category": raw_profile.get("category"),
            "followers_count": self.parse_count(raw_profile.get("followers_count")),
            "following_count": self.parse_count(raw_profile.get("following_count")),
            "posts_count": self.parse_count(raw_profile.get("posts_count")),
            "external_url": raw_profile.get("external_url"),
            "is_verified": bool(raw_profile.get("is_verified", False)),
            "is_business": bool(raw_profile.get("is_business", False)),
            "bio_language": None,
            "bio_hashtags": [],
            "bio_mentions": [],
            "bio_links": [],
            "scraped_at": self.normalize_date(raw_profile.get("scraped_at"))
        }
        
        # Extrai elementos da bio
        if profile["bio_text"]:
            profile["bio_language"] = self.detect_language(profile["bio_text"])
            profile["bio_hashtags"] = self.extract_hashtags(profile["bio_text"])
            profile["bio_mentions"] = self.extract_mentions(profile["bio_text"])
            profile["bio_links"] = self.extract_links(profile["bio_text"])
        
        return profile
    
    def normalize_post(self, raw_post: Dict[str, Any], profile_id: str) -> Dict[str, Any]:
        """Normaliza dados de um post."""
        caption = self.clean_text(raw_post.get("caption_text"))
        
        post = {
            "post_id": f"{profile_id}_{raw_post.get('shortcode', raw_post.get('index', 0))}",
            "profile_id": profile_id,
            "shortcode": raw_post.get("shortcode"),
            "content_type": raw_post.get("content_type", "image"),
            "caption_text": caption,
            "likes_count": self.parse_count(raw_post.get("likes_count")),
            "comments_count": self.parse_count(raw_post.get("comments_count")),
            "published_at": self.normalize_date(raw_post.get("published_at")),
            "is_pinned": bool(raw_post.get("is_pinned", False)),
            "hashtags": raw_post.get("hashtags", []) or self.extract_hashtags(caption or ""),
            "mentions": raw_post.get("mentions", []) or self.extract_mentions(caption or ""),
            "first_line_hook": None,
            "has_cta": False,
            "has_location": False,
            "language": None
        }
        
        # Extrai primeira linha (gancho)
        if caption:
            lines = caption.split('\n')
            post["first_line_hook"] = lines[0].strip() if lines else None
            
            # Detecta CTA na legenda
            cta_keywords = [
                'clique', 'link', 'saiba mais', 'compre', 'comprar', 
                'agende', 'agenda', 'chame', 'chamar', 'whatsapp',
                'inscreva', 'inscrever', 'cadastre', 'cadastrar',
                'baixe', 'baixar', 'download', 'acesse', 'acessar',
                'peça', 'pedir', 'solicite', 'solicitar', 'garanta',
                'click', 'link in bio', 'buy', 'shop', 'subscribe',
                'dm', 'send message', 'tap link'
            ]
            
            caption_lower = caption.lower()
            post["has_cta"] = any(keyword in caption_lower for keyword in cta_keywords)
            
            # Detecta localização
            location_keywords = [
                'brasil', 'são paulo', 'rio de janeiro', 'bh', 'curitiba',
                'porto alegre', 'salvador', 'recife', 'fortaleza',
                '📍', '🗺️', 'localização', 'endereco', 'endereço',
                'rua', 'avenida', 'av.', 'nº', 'numero'
            ]
            post["has_location"] = any(keyword in caption_lower for keyword in location_keywords)
            
            # Idioma
            post["language"] = self.detect_language(caption)
        
        return post
    
    def normalize_run(self, run_dir: str) -> Dict[str, Any]:
        """
        Carrega dados brutos de uma execução e normaliza tudo.
        
        Returns:
            Dicionário com dados normalizados (perfil + posts)
        """
        run_path = Path(run_dir)
        bronze_dir = run_path / "bronze"
        silver_dir = run_path / "silver"
        
        # Carrega dados brutos
        raw_file = bronze_dir / "raw_profile.json"
        if not raw_file.exists():
            raise FileNotFoundError(f"Arquivo bruto não encontrado: {raw_file}")
        
        with open(raw_file, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        # Normaliza perfil
        raw_profile = raw_data.get("profile", {})
        normalized_profile = self.normalize_profile(raw_profile)
        profile_id = normalized_profile["profile_id"]
        
        # Normaliza posts
        raw_posts = raw_data.get("posts", [])
        normalized_posts = [
            self.normalize_post(raw_post, profile_id)
            for raw_post in raw_posts
        ]
        
        # Dados normalizados completos
        normalized_data = {
            "profile": normalized_profile,
            "posts": normalized_posts,
            "metadata": {
                "normalized_at": datetime.now().isoformat(),
                "source_run": run_path.name,
                "total_posts": len(normalized_posts)
            }
        }
        
        # Salva dados normalizados
        silver_file = silver_dir / "normalized_data.json"
        silver_dir.mkdir(parents=True, exist_ok=True)
        
        with open(silver_file, "w", encoding="utf-8") as f:
            json.dump(normalized_data, f, indent=2, ensure_ascii=False)
        
        print(f"Dados normalizados salvos em: {silver_file}")
        
        return normalized_data


def main():
    parser = argparse.ArgumentParser(description="Normalizador de dados do Instagram")
    parser.add_argument("--run-dir", required=True, help="Diretório da execução para normalizar")
    
    args = parser.parse_args()
    
    normalizer = InstagramNormalizer()
    
    try:
        result = normalizer.normalize_run(args.run_dir)
        
        print(f"\n✅ Normalização concluída!")
        print(f"Perfil: @{result['profile']['username']}")
        print(f"Posts normalizados: {len(result['posts'])}")
        print(f"Bio language: {result['profile'].get('bio_language', 'unknown')}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Erro na normalização: {e}")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
