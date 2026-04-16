# Instagram Scanner - Skill do Antigravity

## Visão Geral

Scanner profundo de perfis do Instagram com 5 camadas de processamento:
1. **Ingestão**: Coleta bruta com Playwright
2. **Normalização**: Estruturação em entidades
3. **Enriquecimento**: Features e sinais derivados
4. **Análise Estratégica**: Diagnósticos de negócio
5. **Entrega**: Relatórios acionáveis

## Diferenciais vs InsTrack.app

- ✅ Análise temporal (melhores horários, frequência ideal)
- ✅ Inteligência de hashtags (ranking, shadowban, sugestões)
- ✅ Benchmark competitivo automatizado
- ✅ Predição de performance baseada em histórico
- ✅ Feature Store local com DuckDB
- ✅ Scores explicáveis com justificativas
- ✅ Modo offline com cache inteligente
- ✅ Integração via CLI e API REST

## Estrutura

```
instagram-scanner/
├── SKILL.md                 # Este arquivo
├── requirements.txt         # Dependências Python
├── config.yaml             # Configurações globais
├── scripts/
│   ├── scan_profile.py     # Coletor principal
│   ├── normalize_data.py   # Normalizador
│   ├── enrich_features.py  # Enriquecedor
│   ├── score_engine.py     # Motor de scoring
│   ├── export_report.py    # Gerador de relatórios
│   ├── hashtag_intel.py    # Inteligência de hashtags
│   ├── temporal_analytics.py # Análise temporal
│   └── competitor_benchmark.py # Benchmark competitivo
├── resources/
│   ├── scoring_rules.json  # Regras de scoring
│   ├── content_taxonomy.json # Taxonomia de conteúdo
│   ├── hashtag_blacklist.txt # Hashtags banidas
│   └── report_template.txt # Template de relatório
├── examples/
│   ├── example_input.txt
│   └── example_report.txt
└── tests/
    ├── test_scoring.py
    └── test_normalization.py
```

## Comandos Disponíveis

### Scan Rápido
```bash
python scripts/scan_profile.py --username tanidigital --mode fast
```

### Scan Completo
```bash
python scripts/scan_profile.py --username tanidigital --mode full
```

### Scan Competitivo
```bash
python scripts/competitor_benchmark.py --primary tanidigital --competitors concorrente1 concorrente2 concorrente3
```

### Análise Temporal
```bash
python scripts/temporal_analytics.py --username tanidigital --days 90
```

### Inteligência de Hashtags
```bash
python scripts/hashtag_intel.py --username tanidigital --analyze-top 50
```

## Modos de Execução

| Modo | Posts | Recursos | Tempo Est. | Uso |
|------|-------|----------|------------|-----|
| `fast` | 12 | Bio, CTA, Score básico | 30s | Triagem |
| `full` | 60 | Perfil completo, Reels, Destaques | 2-3min | Consultoria |
| `deep` | 100+ | Histórico 90 dias, Temporal | 5min+ | Estratégia |
| `competitors` | 30 cada | Comparativo 3-10 perfis | 5-10min | Posicionamento |

## Saídas Geradas

### Humanas
- `RELATORIO_INSTAGRAM.txt` - Diagnóstico completo
- `RESUMO_EXECUTIVO.txt` - Visão C-level
- `PLANO_DE_CORRECAO_30_DIAS.txt` - Ações prioritárias
- `MATRIZ_DE_CONTEUDO.txt` - Padrões identificados
- `COMPARATIVO_CONCORRENTES.txt` - Benchmark (se aplicável)

### Técnicas
- `profile.json` - Dados normalizados
- `posts.json` - Posts analisados
- `features.json` - Features derivadas
- `scores.json` - Scores com justificativas
- `temporal_analysis.json` - Séries temporais
- `hashtag_intel.json` - Inteligência de hashtags
- `scan_run.json` - Metadados da execução

### Camadas de Dados
- **Bronze**: HTML bruto, screenshots, JSON cru
- **Silver**: Dados normalizados e limpos
- **Gold**: Features, scores, relatórios

## Scores Implementados

| Score | Descrição | Peso |
|-------|-----------|------|
| POSICIONAMENTO | Clareza de nicho e público | 1.5x |
| BIO | Qualidade do posicionamento na bio | 1.2x |
| OFERTA | Clareza da oferta e mecanismo | 1.5x |
| CONVERSAO | Caminho para ação e CTAs | 1.3x |
| AUTORIDADE | Repertório e expertise | 1.2x |
| PROVA | Depoimentos, resultados, antes/depois | 1.3x |
| CONTEUDO | Qualidade e variedade temática | 1.0x |
| RETENCAO | Ganchos e capacidade de atenção | 1.1x |
| ESTETICA | Consistência visual e profissionalismo | 1.0x |
| CONSISTENCIA | Frequência e regularidade | 1.2x |

**Nota Geral**: Média ponderada com pesos configuráveis

## Features Avançadas

### 1. Análise Temporal
- Melhores horários para postar (por dia da semana)
- Frequência ideal baseada em engajamento
- Crescimento de seguidores (tendência)
- Sazonalidade de conteúdo

### 2. Inteligência de Hashtags
- Ranking de hashtags por performance
- Detecção de hashtags banidas/shadowban
- Sugestões de hashtags relacionadas
- Análise de concorrência por hashtag
- Volume vs competição

### 3. Benchmark Competitivo
- Share of voice por tema
- Comparativo de taxas de engajamento
- Gap analysis de conteúdo
- Mapa de diferenciação
- Ranking relativo

### 4. Predição de Performance
- Score preditivo para novos posts
- Identificação de padrões vencedores
- Recomendações baseadas em histórico

### 5. Feature Store (DuckDB)
- Armazenamento histórico local
- Consultas SQL para análise temporal
- Versionamento de features
- Reprocessamento facilitado

## Requisitos

- Python 3.9+
- Playwright
- DuckDB
- Pandas
- NLTK ou spaCy (NLP leve)
- Pillow (análise de imagem opcional)

Instalação:
```bash
pip install -r requirements.txt
playwright install
```

## Configuração

Edite `config.yaml` para personalizar:
- Paths de saída
- Limites de rate limiting
- Cookies para modo autenticado
- Regras de scoring customizadas
- Templates de relatório

## Observabilidade

- Logs estruturados em JSON
- Data quality checks automáticos
- Dashboard de saúde do scanner (em desenvolvimento)
- Alertas de falha de coleta

## Roadmap

- [x] Fase 1: Scan rápido funcional
- [x] Fase 2: Scan completo + scores
- [x] Fase 3: Análise temporal
- [x] Fase 4: Inteligência de hashtags
- [x] Fase 5: Benchmark competitivo
- [ ] Fase 6: API REST
- [ ] Fase 7: Webhooks e integrações
- [ ] Fase 8: Extensão para autenticação

## Licença

Uso interno Antigravity.
