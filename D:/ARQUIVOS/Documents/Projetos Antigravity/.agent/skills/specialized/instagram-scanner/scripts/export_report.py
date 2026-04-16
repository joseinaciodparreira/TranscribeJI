"""
Instagram Report Exporter - Camada de Entrega

Gera relatórios humanos e arquivos técnicos a partir dos scores e dados analisados.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
import argparse


class InstagramReportExporter:
    """Exporta relatórios e diagnósticos do Instagram."""
    
    def __init__(self):
        pass
    
    def generate_executive_summary(self, scoring_result: Dict[str, Any]) -> str:
        """Gera resumo executivo do perfil."""
        profile = scoring_result.get("analysis_details", {}).get("bio", {})
        scores = scoring_result.get("scores", {})
        overall = scoring_result.get("overall_score", 0)
        bottlenecks = scoring_result.get("bottlenecks", [])
        quick_wins = scoring_result.get("quick_wins", [])
        
        summary = []
        summary.append("=" * 70)
        summary.append("RESUMO EXECUTIVO - ANÁLISE DE INSTAGRAM")
        summary.append("=" * 70)
        summary.append("")
        summary.append(f"Score Geral: {overall}/10")
        summary.append("")
        
        # Classificação
        if overall >= 8:
            classification = "EXCELENTE - Perfil bem posicionado e otimizado"
        elif overall >= 6:
            classification = "BOM - Possui fundamentos mas precisa de ajustes"
        elif overall >= 4:
            classification = "REGULAR - Necessita melhorias significativas"
        else:
            classification = "CRÍTICO - Requer revisão completa da estratégia"
        
        summary.append(f"Classificação: {classification}")
        summary.append("")
        
        # Top 3 gargalos
        summary.append("-" * 70)
        summary.append("PRINCIPAIS GARGALOS")
        summary.append("-" * 70)
        for i, bottleneck in enumerate(bottlenecks[:3], 1):
            score = bottleneck["score"]
            category = bottleneck["category"].upper()
            
            if score < 4:
                severity = "🔴 CRÍTICO"
            elif score < 6:
                severity = "🟡 ATENÇÃO"
            else:
                severity = "🟢 OK"
            
            summary.append(f"{i}. {category}: {score}/10 - {severity}")
        
        summary.append("")
        
        # Ganhos rápidos
        summary.append("-" * 70)
        summary.append("GANHOS RÁPIDOS (Quick Wins)")
        summary.append("-" * 70)
        for i, win in enumerate(quick_wins[:3], 1):
            summary.append(f"{i}. {win}")
        
        summary.append("")
        
        # Análise da bio
        summary.append("-" * 70)
        summary.append("ANÁLISE DA BIO")
        summary.append("-" * 70)
        
        bio_flags = [
            ("Nicho claro", profile.get("has_niche")),
            ("Oferta presente", profile.get("has_offer")),
            ("Mecanismo próprio", profile.get("has_mechanism")),
            ("CTA definido", profile.get("has_cta")),
            ("Autoridade", profile.get("has_authority")),
            ("Prova social", profile.get("has_proof"))
        ]
        
        for label, value in bio_flags:
            status = "✓" if value else "✗"
            summary.append(f"  [{status}] {label}")
        
        summary.append("")
        summary.append(f"  Palavras: {profile.get('word_count', 0)}")
        summary.append(f"  CTA Strength: {profile.get('cta_strength', 'none')}")
        
        return "\n".join(summary)
    
    def generate_correction_plan(self, scoring_result: Dict[str, Any], days: int = 30) -> str:
        """Gera plano de correção para 30 dias."""
        scores = scoring_result.get("scores", {})
        bottlenecks = scoring_result.get("bottlenecks", [])
        analysis = scoring_result.get("analysis_details", {})
        bio_analysis = analysis.get("bio", {})
        post_analysis = analysis.get("posts", {})
        
        plan = []
        plan.append("=" * 70)
        plan.append(f"PLANO DE CORREÇÃO - {days} DIAS")
        plan.append("=" * 70)
        plan.append("")
        
        # Semana 1: Bio e Posicionamento
        plan.append("SEMANA 1 - FUNDAÇÃO E POSICIONAMENTO")
        plan.append("-" * 70)
        
        if not bio_analysis.get("has_niche"):
            plan.append("Dia 1-2: Definir nicho específico")
            plan.append("  → Revisar público-alvo principal")
            plan.append("  → Identificar especialidade única")
            plan.append("  → Atualizar bio com foco no nicho")
            plan.append("")
        
        if not bio_analysis.get("has_mechanism"):
            plan.append("Dia 3-4: Criar método/mecanismo próprio")
            plan.append("  → Documentar processo único de trabalho")
            plan.append("  → Nomear o método (ex: Método XYZ)")
            plan.append("  → Incluir na bio e materiais")
            plan.append("")
        
        if not bio_analysis.get("has_cta"):
            plan.append("Dia 5-7: Implementar CTA forte")
            plan.append("  → Definir ação principal desejada")
            plan.append("  → Criar link de destino otimizado")
            plan.append("  → Adicionar CTA claro na bio")
            plan.append("")
        
        # Semana 2: Conteúdo e Autoridade
        plan.append("\nSEMANA 2 - CONTEÚDO E AUTORIDADE")
        plan.append("-" * 70)
        
        cta_pct = post_analysis.get("cta_percentage", 0)
        if cta_pct < 20:
            plan.append("Dia 8-10: Aumentar CTAs nos posts")
            plan.append("  → Revisar últimos 12 posts")
            plan.append("  → Adicionar CTA em 30% dos posts")
            plan.append("  → Variar tipos de CTA (link, DM, comentário)")
            plan.append("")
        
        auth_pct = post_analysis.get("authority_percentage", 0)
        if auth_pct < 30:
            plan.append("Dia 11-14: Fortalecer conteúdo de autoridade")
            plan.append("  → Criar 3 posts educativos profundos")
            plan.append("  → Compartilhar cases/resultados")
            plan.append("  → Mostrar bastidor do trabalho")
            plan.append("")
        
        # Semana 3: Prova Social
        plan.append("\nSEMANA 3 - PROVA SOCIAL E CONVERSÃO")
        plan.append("-" * 70)
        
        if not bio_analysis.get("has_proof"):
            plan.append("Dia 15-17: Adicionar prova social na bio")
            plan.append("  → Coletar 3-5 depoimentos fortes")
            plan.append("  → Quantificar resultados (ex: +500 alunos)")
            plan.append("  → Incluir números na bio")
            plan.append("")
        
        proof_pct = post_analysis.get("proof_percentage", 0)
        if proof_pct < 15:
            plan.append("Dia 18-21: Aumentar prova social nos posts")
            plan.append("  → Postar 2-3 antes/depois")
            plan.append("  → Compartilhar testimonials em vídeo")
            plan.append("  → Mostrar métricas de clientes")
            plan.append("")
        
        # Semana 4: Consistência e Otimização
        plan.append("\nSEMANA 4 - CONSISTÊNCIA E OTIMIZAÇÃO")
        plan.append("-" * 70)
        plan.append("Dia 22-25: Auditoria de consistência visual")
        plan.append("  → Revisar padrão de cores e fontes")
        plan.append("  → Criar templates para posts")
        plan.append("  → Definir estilo de capas")
        plan.append("")
        plan.append("Dia 26-28: Otimizar legenda e ganchos")
        plan.append("  → Analisar hooks dos top posts")
        plan.append("  → Testar novos formatos de abertura")
        plan.append("  → Melhorar primeiras linhas")
        plan.append("")
        plan.append("Dia 29-30: Reavaliação completa")
        plan.append("  → Rodar scanner novamente")
        plan.append("  → Comparar scores antes/depois")
        plan.append("  → Planejar próximo ciclo")
        plan.append("")
        
        # Métricas de sucesso
        plan.append("-" * 70)
        plan.append("MÉTRICAS DE SUCESSO ESPERADAS")
        plan.append("-" * 70)
        
        current_scores = list(scores.values())
        avg_current = sum(current_scores) / len(current_scores) if current_scores else 0
        
        plan.append(f"Score atual médio: {avg_current:.1f}/10")
        plan.append(f"Score alvo (30 dias): {min(avg_current + 2, 10):.1f}/10")
        plan.append("")
        plan.append("Metas específicas:")
        plan.append("  • Bio score: +2 pontos")
        plan.append("  • Conteúdo score: +1.5 pontos")
        plan.append("  • Conversão score: +2 pontos")
        plan.append("  • Posts com CTA: 30%+")
        plan.append("  • Posts com prova social: 20%+")
        
        return "\n".join(plan)
    
    def generate_full_report(self, scoring_result: Dict[str, Any]) -> str:
        """Gera relatório completo de análise."""
        lines = []
        
        # Cabeçalho
        lines.append("#" * 70)
        lines.append("# RELATÓRIO COMPLETO - ANÁLISE DE INSTAGRAM")
        lines.append("#" * 70)
        lines.append("")
        lines.append(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        lines.append(f"Perfil: @{scoring_result.get('metadata', {}).get('username', 'N/A')}")
        lines.append("")
        
        # Resumo executivo
        lines.append(self.generate_executive_summary(scoring_result))
        lines.append("")
        
        # Scores detalhados
        lines.append("=" * 70)
        lines.append("SCORES DETALHADOS POR CATEGORIA")
        lines.append("=" * 70)
        lines.append("")
        
        scores = scoring_result.get("scores", {})
        justifications = scoring_result.get("justifications", {})
        
        categories_order = [
            "posicionamento", "bio", "oferta", "conversao",
            "autoridade", "prova", "conteudo", "retencao",
            "estetica", "consistencia"
        ]
        
        category_labels = {
            "posicionamento": "POSICIONAMENTO",
            "bio": "BIO",
            "oferta": "OFERTA",
            "conversao": "CONVERSÃO",
            "autoridade": "AUTORIDADE",
            "prova": "PROVA SOCIAL",
            "conteudo": "CONTEÚDO",
            "retencao": "RETENÇÃO",
            "estetica": "ESTÉTICA",
            "consistencia": "CONSISTÊNCIA"
        }
        
        for cat in categories_order:
            score = scores.get(cat, 0)
            label = category_labels.get(cat, cat.upper())
            
            bar_len = int(score)
            bar = "█" * bar_len + "░" * (10 - bar_len)
            
            lines.append(f"{label:20} [{bar}] {score:.1f}/10")
        
        lines.append("")
        
        # Justificativas
        if justifications:
            lines.append("-" * 70)
            lines.append("JUSTIFICATIVAS")
            lines.append("-" * 70)
            
            if "bio" in justifications:
                lines.append("\nBio:")
                for just in justifications["bio"]:
                    lines.append(f"  • {just}")
            
            if "conteudo" in justifications:
                lines.append("\nConteúdo:")
                for just in justifications["conteudo"]:
                    lines.append(f"  • {just}")
            
            lines.append("")
        
        # Plano de correção
        lines.append(self.generate_correction_plan(scoring_result))
        lines.append("")
        
        # Diagnóstico de conversão
        lines.append("=" * 70)
        lines.append("DIAGNÓSTICO DE CONVERSÃO")
        lines.append("=" * 70)
        lines.append("")
        
        bio_analysis = scoring_result.get("analysis_details", {}).get("bio", {})
        conv_score = scores.get("conversao", 0)
        
        lines.append(f"Score de Conversão: {conv_score:.1f}/10")
        lines.append("")
        
        conversion_checks = [
            ("Perfil tem link externo", bool(scoring_result.get("external_url", bio_analysis.get("has_external_url")))),
            ("Bio tem CTA claro", bio_analysis.get("has_cta", False)),
            ("CTA é forte", bio_analysis.get("cta_strength") == "strong"),
            ("Bio comunica desejo", bio_analysis.get("has_desire", False)),
            ("Bio comunica dor", bio_analysis.get("has_pain", False)),
            ("Posts têm CTA", scoring_result.get("analysis_details", {}).get("posts", {}).get("cta_percentage", 0) > 15)
        ]
        
        for check, result in conversion_checks:
            status = "✓" if result else "✗"
            lines.append(f"  [{status}] {check}")
        
        lines.append("")
        
        # Recomendações finais
        lines.append("=" * 70)
        lines.append("RECOMENDAÇÕES FINAIS")
        lines.append("=" * 70)
        lines.append("")
        
        overall = scoring_result.get("overall_score", 0)
        
        if overall >= 8:
            lines.append("✓ Perfil em excelente estado")
            lines.append("→ Foco: Manter consistência e testar otimizações finas")
            lines.append("→ Considerar: Escalar tráfego pago")
        elif overall >= 6:
            lines.append("~ Perfil com boa base")
            lines.append("→ Foco: Resolver gargalos específicos identificados")
            lines.append("→ Prioridade: Bio e prova social")
        elif overall >= 4:
            lines.append("! Perfil precisa de melhorias")
            lines.append("→ Foco: Seguir plano de 30 dias rigorosamente")
            lines.append("→ Prioridade: Posicionamento e oferta clara")
        else:
            lines.append("🔴 Perfil crítico")
            lines.append("→ Foco: Revisão completa de estratégia")
            lines.append("→ Prioridade: Nicho, oferta e mecanismo")
        
        lines.append("")
        lines.append("#" * 70)
        lines.append("FIM DO RELATÓRIO")
        lines.append("#" * 70)
        
        return "\n".join(lines)
    
    def export_run(self, run_dir: str) -> Dict[str, str]:
        """Exporta todos os relatórios de uma execução."""
        run_path = Path(run_dir)
        gold_dir = run_path / "gold"
        
        # Carrega scores
        scores_file = gold_dir / "scores.json"
        if not scores_file.exists():
            raise FileNotFoundError(f"Scores não encontrados: {scores_file}")
        
        with open(scores_file, "r", encoding="utf-8") as f:
            scoring_result = json.load(f)
        
        # Gera relatórios
        gold_dir.mkdir(parents=True, exist_ok=True)
        
        outputs = {}
        
        # Relatório completo
        full_report = self.generate_full_report(scoring_result)
        full_report_path = gold_dir / "RELATORIO_INSTAGRAM.txt"
        with open(full_report_path, "w", encoding="utf-8") as f:
            f.write(full_report)
        outputs["full_report"] = str(full_report_path)
        
        # Resumo executivo
        exec_summary = self.generate_executive_summary(scoring_result)
        exec_summary_path = gold_dir / "RESUMO_EXECUTIVO.txt"
        with open(exec_summary_path, "w", encoding="utf-8") as f:
            f.write(exec_summary)
        outputs["executive_summary"] = str(exec_summary_path)
        
        # Plano de correção
        correction_plan = self.generate_correction_plan(scoring_result)
        correction_plan_path = gold_dir / "PLANO_DE_CORRECAO_30_DIAS.txt"
        with open(correction_plan_path, "w", encoding="utf-8") as f:
            f.write(correction_plan)
        outputs["correction_plan"] = str(correction_plan_path)
        
        print(f"\nRelatórios exportados em: {gold_dir}")
        for name, path in outputs.items():
            print(f"  • {name}: {path}")
        
        return outputs


def main():
    parser = argparse.ArgumentParser(description="Exportador de relatórios do Instagram")
    parser.add_argument("--run-dir", required=True, help="Diretório da execução")
    
    args = parser.parse_args()
    
    exporter = InstagramReportExporter()
    
    try:
        outputs = exporter.export_run(args.run_dir)
        
        print(f"\n✅ Relatórios gerados com sucesso!")
        return 0
        
    except Exception as e:
        print(f"\n❌ Erro ao exportar relatórios: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
