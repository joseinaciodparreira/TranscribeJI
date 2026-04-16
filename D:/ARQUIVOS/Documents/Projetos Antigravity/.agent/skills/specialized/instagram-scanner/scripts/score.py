"""
Instagram Scoring Engine - Camada de Análise Estratégica

Gera scores explicáveis e diagnósticos estratégicos baseados nos dados normalizados.
Cada score inclui justificativas detalhadas para auditoria.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import argparse
import re


class InstagramScorer:
    """Motor de scoring e análise estratégica do Instagram."""
    
    # Palavras-chave para detecção de padrões
    OFFER_KEYWORDS = [
        'consulta', 'sessão', 'pacote', 'programa', 'curso', 'mentoria',
        'workshop', 'treinamento', 'ebook', 'guia', 'material',
        'desconto', 'promoção', 'oferta', 'lançamento', 'vagas',
        'inscrição', 'matrícula', 'compra', 'preço', 'valor', 'investimento',
        'consulting', 'session', 'package', 'course', 'program', 'coaching'
    ]
    
    AUTHORITY_KEYWORDS = [
        'especialista', 'expert', 'autoridade', 'referência', 'pioneiro',
        'fundador', 'diretor', 'ceo', 'professor', 'doutor', 'phd',
        'anos de experiência', '+10 anos', '+5 anos', 'desde',
        'formado', 'certificado', 'credenciado', 'reconhecido',
        'specialist', 'expert', 'founder', 'director', 'years experience'
    ]
    
    SOCIAL_PROOF_KEYWORDS = [
        'depoimento', 'testemunho', 'resultado', 'case', 'antes e depois',
        'transformação', 'evolução', 'aluno', 'cliente', 'paciente',
        'milhares', '+1000', '+500', 'centenas', 'avaliações', 'reviews',
        '⭐', '🌟', 'recomendo', 'indicaram',
        'testimonial', 'result', 'transformation', 'student', 'client', 'reviews'
    ]
    
    PAIN_KEYWORDS = [
        'problema', 'dificuldade', 'desafio', 'dor', 'sofrimento',
        'frustração', 'ansiedade', 'estresse', 'medo', 'insegurança',
        'não consegue', 'não sabe', 'não tem', 'cansado', 'sobrecarregado',
        'problem', 'difficulty', 'challenge', 'pain', 'struggle', 'frustrated'
    ]
    
    DESIRE_KEYWORDS = [
        'conquista', 'alcance', 'atingir', 'realizar', 'transformar',
        'liberdade', 'sucesso', 'prosperidade', 'abundância', 'felicidade',
        'resultado', 'objetivo', 'meta', 'sonho', 'vida dos sonhos',
        'achieve', 'reach', 'transform', 'freedom', 'success', 'dream'
    ]
    
    CTA_STRONG = [
        'clique agora', 'compre agora', 'inscreva-se já', 'garanta sua vaga',
        'últimas vagas', 'só hoje', 'oferta por tempo limitado',
        'chame no whatsapp', 'agende agora', 'reserve já',
        'click now', 'buy now', 'sign up now', 'limited spots', 'only today'
    ]
    
    CTA_WEAK = [
        'saiba mais', 'confira', 'veja', 'conheça', 'descubra',
        'leia mais', 'acompanhe', 'segue', 'follow', 'check out'
    ]
    
    def __init__(self):
        self.scores = {}
        self.justifications = {}
    
    def _count_keyword_matches(self, text: str, keywords: List[str]) -> int:
        """Conta ocorrências de palavras-chave em um texto."""
        if not text:
            return 0
        
        text_lower = text.lower()
        count = sum(1 for keyword in keywords if keyword.lower() in text_lower)
        return count
    
    def _analyze_bio(self, bio_text: str) -> Dict[str, Any]:
        """Analisa a bio do perfil."""
        analysis = {
            "has_niche": False,
            "has_offer": False,
            "has_mechanism": False,
            "has_cta": False,
            "cta_strength": "none",
            "has_authority": False,
            "has_proof": False,
            "has_pain": False,
            "has_desire": False,
            "is_positioned": False,
            "word_count": 0,
            "character_count": 0
        }
        
        if not bio_text:
            return analysis
        
        analysis["word_count"] = len(bio_text.split())
        analysis["character_count"] = len(bio_text)
        
        # Detecta nicho (palavras específicas de categoria/profissão)
        niche_patterns = [
            r'\b(nutricionista|psicologo|médico|advogado|coach|mentor|consultor)\b',
            r'\b(marketing|vendas|gestao|financas|saude|bem-estar|fitness)\b',
            r'\b(emagrecimento|hipertrofia|ansiedade|terapia|nutricao)\b'
        ]
        analysis["has_niche"] = any(re.search(pattern, bio_text.lower()) for pattern in niche_patterns)
        
        # Detecta oferta
        analysis["has_offer"] = self._count_keyword_matches(bio_text, self.OFFER_KEYWORDS) > 0
        
        # Detecta mecanismo único
        mechanism_patterns = [
            r'método\s+\w+', r'sistema\s+\w+', r'técnica\s+\w+',
            r'way\s+\w+', r'framework', r'protocolo'
        ]
        analysis["has_mechanism"] = any(re.search(pattern, bio_text.lower()) for pattern in mechanism_patterns)
        
        # Detecta CTA
        has_strong_cta = any(cta in bio_text.lower() for cta in self.CTA_STRONG)
        has_weak_cta = any(cta in bio_text.lower() for cta in self.CTA_WEAK)
        
        if has_strong_cta:
            analysis["has_cta"] = True
            analysis["cta_strength"] = "strong"
        elif has_weak_cta:
            analysis["has_cta"] = True
            analysis["cta_strength"] = "weak"
        
        # Detecta autoridade
        analysis["has_authority"] = self._count_keyword_matches(bio_text, self.AUTHORITY_KEYWORDS) > 0
        
        # Detecta prova social
        analysis["has_proof"] = self._count_keyword_matches(bio_text, self.SOCIAL_PROOF_KEYWORDS) > 0
        
        # Detecta dor e desejo
        analysis["has_pain"] = self._count_keyword_matches(bio_text, self.PAIN_KEYWORDS) > 0
        analysis["has_desire"] = self._count_keyword_matches(bio_text, self.DESIRE_KEYWORDS) > 0
        
        # Bio está posicionada?
        positioning_factors = [
            analysis["has_niche"],
            analysis["has_mechanism"],
            analysis["has_authority"],
            analysis["word_count"] >= 10 and analysis["word_count"] <= 80
        ]
        analysis["is_positioned"] = sum(positioning_factors) >= 2
        
        return analysis
    
    def _analyze_posts(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa padrão de conteúdo dos posts."""
        if not posts:
            return {
                "total_posts": 0,
                "avg_caption_length": 0,
                "posts_with_cta": 0,
                "posts_with_hashtags": 0,
                "posts_with_location": 0,
                "content_types": {},
                "avg_hashtags_per_post": 0,
                "posts_with_offer": 0,
                "posts_with_authority": 0,
                "posts_with_proof": 0
            }
        
        total = len(posts)
        caption_lengths = []
        posts_with_cta = 0
        posts_with_hashtags = 0
        posts_with_location = 0
        content_types = {}
        hashtag_counts = []
        posts_with_offer = 0
        posts_with_authority = 0
        posts_with_proof = 0
        
        for post in posts:
            caption = post.get("caption_text", "") or ""
            
            # Comprimento da legenda
            caption_lengths.append(len(caption.split()))
            
            # CTA
            if post.get("has_cta"):
                posts_with_cta += 1
            
            # Hashtags
            hashtags = post.get("hashtags", [])
            if hashtags:
                posts_with_hashtags += 1
                hashtag_counts.append(len(hashtags))
            
            # Localização
            if post.get("has_location"):
                posts_with_location += 1
            
            # Tipo de conteúdo
            content_type = post.get("content_type", "image")
            content_types[content_type] = content_types.get(content_type, 0) + 1
            
            # Detecção de padrões na legenda
            if self._count_keyword_matches(caption, self.OFFER_KEYWORDS) > 0:
                posts_with_offer += 1
            
            if self._count_keyword_matches(caption, self.AUTHORITY_KEYWORDS) > 0:
                posts_with_authority += 1
            
            if self._count_keyword_matches(caption, self.SOCIAL_PROOF_KEYWORDS) > 0:
                posts_with_proof += 1
        
        return {
            "total_posts": total,
            "avg_caption_length": sum(caption_lengths) / total if total else 0,
            "posts_with_cta": posts_with_cta,
            "cta_percentage": (posts_with_cta / total * 100) if total else 0,
            "posts_with_hashtags": posts_with_hashtags,
            "posts_with_location": posts_with_location,
            "content_types": content_types,
            "avg_hashtags_per_post": sum(hashtag_counts) / len(hashtag_counts) if hashtag_counts else 0,
            "posts_with_offer": posts_with_offer,
            "offer_percentage": (posts_with_offer / total * 100) if total else 0,
            "posts_with_authority": posts_with_authority,
            "authority_percentage": (posts_with_authority / total * 100) if total else 0,
            "posts_with_proof": posts_with_proof,
            "proof_percentage": (posts_with_proof / total * 100) if total else 0
        }
    
    def calculate_score_bio(self, bio_analysis: Dict[str, Any]) -> Tuple[float, List[str]]:
        """Calcula score da bio (0-10) com justificativas."""
        score = 0.0
        justifications = []
        
        # Nicho claro (+2 pontos)
        if bio_analysis["has_niche"]:
            score += 2.0
            justifications.append("✓ Nicho claro identificado")
        else:
            justifications.append("✗ Nicho não está claro")
        
        # Oferta presente (+2 pontos)
        if bio_analysis["has_offer"]:
            score += 2.0
            justifications.append("✓ Oferta identificada")
        else:
            justifications.append("✗ Sem oferta clara")
        
        # Mecanismo único (+2 pontos)
        if bio_analysis["has_mechanism"]:
            score += 2.0
            justifications.append("✓ Possui mecanismo/método próprio")
        else:
            justifications.append("✗ Sem mecanismo diferenciado")
        
        # CTA presente (+1.5 pontos)
        if bio_analysis["has_cta"]:
            if bio_analysis["cta_strength"] == "strong":
                score += 1.5
                justifications.append("✓ CTA forte e direto")
            else:
                score += 0.8
                justifications.append("~ CTA presente mas fraco")
        else:
            justifications.append("✗ Sem call-to-action")
        
        # Autoridade (+1.5 pontos)
        if bio_analysis["has_authority"]:
            score += 1.5
            justifications.append("✓ Marcadores de autoridade presentes")
        else:
            justifications.append("✗ Sem marcadores de autoridade")
        
        # Prova social (+1 ponto)
        if bio_analysis["has_proof"]:
            score += 1.0
            justifications.append("✓ Elementos de prova social")
        else:
            justifications.append("✗ Sem prova social")
        
        # Tamanho adequado (+0.5 pontos bônus)
        word_count = bio_analysis["word_count"]
        if 15 <= word_count <= 60:
            score += 0.5
            justifications.append("✓ Tamanho da bio adequado")
        
        return min(score, 10.0), justifications
    
    def calculate_score_content(self, post_analysis: Dict[str, Any]) -> Tuple[float, List[str]]:
        """Calcula score de conteúdo (0-10) com justificativas."""
        score = 0.0
        justifications = []
        
        # Frequência de CTA (até 2 pontos)
        cta_pct = post_analysis.get("cta_percentage", 0)
        if cta_pct >= 30:
            score += 2.0
            justifications.append("✓ Boa frequência de CTAs ({:.0f}%)".format(cta_pct))
        elif cta_pct >= 15:
            score += 1.0
            justifications.append("~ CTAs presentes mas pouco frequentes ({:.0f}%)".format(cta_pct))
        else:
            justifications.append("✗ Poucos ou nenhum CTA ({:.0f}%)".format(cta_pct))
        
        # Conteúdo educativo/autoridade (até 2 pontos)
        auth_pct = post_analysis.get("authority_percentage", 0)
        if auth_pct >= 40:
            score += 2.0
            justifications.append("✓ Forte conteúdo de autoridade ({:.0f}%)".format(auth_pct))
        elif auth_pct >= 20:
            score += 1.0
            justifications.append("~ Algum conteúdo de autoridade ({:.0f}%)".format(auth_pct))
        else:
            justifications.append("✗ Pouco conteúdo de autoridade ({:.0f}%)".format(auth_pct))
        
        # Prova social nos posts (até 2 pontos)
        proof_pct = post_analysis.get("proof_percentage", 0)
        if proof_pct >= 20:
            score += 2.0
            justifications.append("✓ Boa presença de prova social ({:.0f}%)".format(proof_pct))
        elif proof_pct >= 10:
            score += 1.0
            justifications.append("~ Alguma prova social ({:.0f}%)".format(proof_pct))
        else:
            justifications.append("✗ Pouca prova social nos posts ({:.0f}%)".format(proof_pct))
        
        # Conteúdo de oferta (até 1.5 pontos)
        offer_pct = post_analysis.get("offer_percentage", 0)
        if 10 <= offer_pct <= 30:
            score += 1.5
            justifications.append("✓ Equilíbrio de posts de oferta ({:.0f}%)".format(offer_pct))
        elif offer_pct < 10:
            score += 0.5
            justifications.append("~ Poucos posts de oferta ({:.0f}%)".format(offer_pct))
        else:
            justifications.append("! Excesso de posts de venda ({:.0f}%)".format(offer_pct))
        
        # Uso de hashtags (até 1 ponto)
        hashtag_posts_pct = (post_analysis.get("posts_with_hashtags", 0) / max(post_analysis.get("total_posts", 1), 1)) * 100
        if hashtag_posts_pct >= 80:
            score += 1.0
            justifications.append("✓ Bom uso de hashtags")
        elif hashtag_posts_pct >= 50:
            score += 0.5
            justifications.append("~ Uso moderado de hashtags")
        else:
            justifications.append("✗ Pouco uso de hashtags")
        
        # Localização (até 1 ponto)
        location_posts_pct = (post_analysis.get("posts_with_location", 0) / max(post_analysis.get("total_posts", 1), 1)) * 100
        if location_posts_pct >= 30:
            score += 1.0
            justifications.append("✓ Bom sinal de localização")
        elif location_posts_pct > 0:
            score += 0.5
            justifications.append("~ Alguns sinais de localização")
        else:
            justifications.append("✗ Sem sinais de localização")
        
        # Diversidade de conteúdo (até 1.5 pontos)
        content_types = post_analysis.get("content_types", {})
        type_count = len(content_types)
        if type_count >= 3:
            score += 1.5
            justifications.append("✓ Boa diversidade de formatos")
        elif type_count == 2:
            score += 0.8
            justifications.append("~ Pouca diversidade de formatos")
        elif type_count == 1:
            justifications.append("✗ Apenas um formato de conteúdo")
        
        return min(score, 10.0), justifications
    
    def calculate_all_scores(self, normalized_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula todos os scores do perfil."""
        profile = normalized_data.get("profile", {})
        posts = normalized_data.get("posts", [])
        
        # Análises preliminares
        bio_analysis = self._analyze_bio(profile.get("bio_text"))
        post_analysis = self._analyze_posts(posts)
        
        # Scores individuais
        bio_score, bio_just = self.calculate_score_bio(bio_analysis)
        content_score, content_just = self.calculate_score_content(post_analysis)
        
        # Score de posicionamento (baseado na bio + consistência)
        positioning_factors = [
            bio_analysis["is_positioned"] * 3,
            bio_analysis["has_niche"] * 2,
            content_score / 2
        ]
        positioning_score = min(sum(positioning_factors), 10.0)
        
        # Score de oferta
        offer_score = 0.0
        if bio_analysis["has_offer"]:
            offer_score += 4.0
        offer_score += (post_analysis.get("offer_percentage", 0) / 30) * 3
        if bio_analysis["has_mechanism"]:
            offer_score += 2.0
        if bio_analysis["cta_strength"] == "strong":
            offer_score += 1.0
        offer_score = min(offer_score, 10.0)
        
        # Score de conversão
        conversion_score = 0.0
        if profile.get("external_url"):
            conversion_score += 2.0
        if bio_analysis["has_cta"]:
            conversion_score += 2.0 if bio_analysis["cta_strength"] == "strong" else 1.0
        conversion_score += (post_analysis.get("cta_percentage", 0) / 30) * 3
        conversion_score += bio_analysis.get("has_desire", False) * 1.5
        conversion_score += bio_analysis.get("has_pain", False) * 1.5
        conversion_score = min(conversion_score, 10.0)
        
        # Score de autoridade
        authority_score = 0.0
        if profile.get("is_verified"):
            authority_score += 3.0
        if bio_analysis["has_authority"]:
            authority_score += 3.0
        authority_score += (post_analysis.get("authority_percentage", 0) / 40) * 4
        authority_score = min(authority_score, 10.0)
        
        # Score de prova social
        proof_score = 0.0
        if bio_analysis["has_proof"]:
            proof_score += 4.0
        proof_score += (post_analysis.get("proof_percentage", 0) / 20) * 6
        proof_score = min(proof_score, 10.0)
        
        # Score de retenção (ganchos, qualidade visual estimada)
        retention_score = 0.0
        posts_with_hooks = sum(1 for p in posts if p.get("first_line_hook"))
        if posts:
            hook_pct = (posts_with_hooks / len(posts)) * 100
            if hook_pct >= 70:
                retention_score += 5.0
            elif hook_pct >= 40:
                retention_score += 2.5
        
        avg_caption_len = post_analysis.get("avg_caption_length", 0)
        if 50 <= avg_caption_len <= 300:
            retention_score += 3.0
        elif avg_caption_len > 0:
            retention_score += 1.5
        
        retention_score = min(retention_score, 10.0)
        
        # Score de estética (estimado - seria melhor com análise de imagem real)
        # Por enquanto baseado em consistência de tipos de conteúdo
        aesthetic_score = 5.0  # Base neutro
        content_types = post_analysis.get("content_types", {})
        if content_types:
            dominant_type = max(content_types.values())
            consistency = dominant_type / sum(content_types.values())
            if consistency >= 0.7:
                aesthetic_score += 3.0
            elif consistency >= 0.5:
                aesthetic_score += 1.5
        
        # Score de consistência
        consistency_score = 0.0
        total_posts = post_analysis.get("total_posts", 0)
        if total_posts >= 12:
            consistency_score += 4.0
        elif total_posts >= 6:
            consistency_score += 2.0
        
        cta_consistency = post_analysis.get("cta_percentage", 0)
        if 15 <= cta_consistency <= 40:
            consistency_score += 3.0
        elif cta_consistency > 0:
            consistency_score += 1.5
        
        hashtag_consistency = (post_analysis.get("posts_with_hashtags", 0) / max(total_posts, 1)) * 100
        if hashtag_consistency >= 70:
            consistency_score += 3.0
        elif hashtag_consistency >= 40:
            consistency_score += 1.5
        
        consistency_score = min(consistency_score, 10.0)
        
        # Score geral (média ponderada)
        weights = {
            "posicionamento": 1.5,
            "bio": 1.2,
            "oferta": 1.3,
            "conversao": 1.3,
            "autoridade": 1.0,
            "prova": 1.0,
            "conteudo": 1.2,
            "retencao": 0.8,
            "estetica": 0.7,
            "consistencia": 1.0
        }
        
        scores_dict = {
            "posicionamento": positioning_score,
            "bio": bio_score,
            "oferta": offer_score,
            "conversao": conversion_score,
            "autoridade": authority_score,
            "prova": proof_score,
            "conteudo": content_score,
            "retencao": retention_score,
            "estetica": aesthetic_score,
            "consistencia": consistency_score
        }
        
        total_weight = sum(weights.values())
        overall_score = sum(scores_dict[k] * weights[k] for k in scores_dict) / total_weight
        
        # Identifica gargalos (3 menores scores)
        sorted_scores = sorted(scores_dict.items(), key=lambda x: x[1])
        bottlenecks = sorted_scores[:3]
        
        # Identifica ganhos rápidos
        quick_wins = []
        if not bio_analysis["has_mechanism"]:
            quick_wins.append("Criar método/mecanismo próprio na bio")
        if not bio_analysis["has_cta"]:
            quick_wins.append("Adicionar CTA claro na bio")
        if post_analysis.get("cta_percentage", 0) < 20:
            quick_wins.append("Aumentar CTAs nos posts")
        if not bio_analysis["has_proof"]:
            quick_wins.append("Adicionar prova social na bio")
        
        return {
            "overall_score": round(overall_score, 2),
            "scores": {k: round(v, 2) for k, v in scores_dict.items()},
            "justifications": {
                "bio": bio_just,
                "conteudo": content_just
            },
            "bottlenecks": [
                {"category": cat, "score": round(score, 2)}
                for cat, score in bottlenecks
            ],
            "quick_wins": quick_wins[:3],
            "analysis_details": {
                "bio": bio_analysis,
                "posts": post_analysis
            }
        }
    
    def score_run(self, run_dir: str) -> Dict[str, Any]:
        """Carrega dados normalizados e gera scores."""
        run_path = Path(run_dir)
        silver_dir = run_path / "silver"
        gold_dir = run_path / "gold"
        
        # Carrega dados normalizados
        normalized_file = silver_dir / "normalized_data.json"
        if not normalized_file.exists():
            raise FileNotFoundError(f"Dados normalizados não encontrados: {normalized_file}")
        
        with open(normalized_file, "r", encoding="utf-8") as f:
            normalized_data = json.load(f)
        
        # Calcula scores
        scoring_result = self.calculate_all_scores(normalized_data)
        
        # Adiciona metadados
        scoring_result["metadata"] = {
            "scored_at": datetime.now().isoformat(),
            "source_run": run_path.name,
            "username": normalized_data.get("profile", {}).get("username")
        }
        
        # Salva scores
        gold_dir.mkdir(parents=True, exist_ok=True)
        scores_file = gold_dir / "scores.json"
        
        with open(scores_file, "w", encoding="utf-8") as f:
            json.dump(scoring_result, f, indent=2, ensure_ascii=False)
        
        print(f"Scores salvos em: {scores_file}")
        
        return scoring_result


def main():
    parser = argparse.ArgumentParser(description="Motor de scoring do Instagram")
    parser.add_argument("--run-dir", required=True, help="Diretório da execução para analisar")
    
    args = parser.parse_args()
    
    scorer = InstagramScorer()
    
    try:
        result = scorer.score_run(args.run_dir)
        
        print(f"\n{'='*60}")
        print(f"SCORES GERADOS - @{result['metadata']['username']}")
        print(f"{'='*60}")
        print(f"\nScore Geral: {result['overall_score']}/10\n")
        
        print("Scores por Categoria:")
        for category, score in result['scores'].items():
            bar = "█" * int(score / 1) + "░" * (10 - int(score / 1))
            print(f"  {category.upper():15} [{bar}] {score}/10")
        
        print(f"\nPrincipais Gargalos:")
        for i, bottleneck in enumerate(result['bottlenecks'], 1):
            print(f"  {i}. {bottleneck['category'].upper()}: {bottleneck['score']}/10")
        
        print(f"\nGanhos Rápidos:")
        for i, win in enumerate(result['quick_wins'], 1):
            print(f"  {i}. {win}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Erro no scoring: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
