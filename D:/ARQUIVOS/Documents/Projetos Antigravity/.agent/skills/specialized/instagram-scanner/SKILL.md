# Instagram Scanner Skill

## Visão Geral

Scanner profundo de perfis do Instagram para análise estratégica de:
- Posicionamento
- Bio e oferta
- Conversão e autoridade
- Prova social e conteúdo
- Consistência visual e retenção

## Arquitetura

```
instagram-scanner/
├── SKILL.md                    # Este arquivo
├── scripts/
│   ├── scan_profile.py         # Coleta de dados brutos
│   ├── normalize_data.py       # Normalização das entidades
│   ├── score.py                # Motor de scoring e análise
│   ├── export_report.py        # Geração de relatórios
│   └── scan_competitors.py     # Scan comparativo
├── resources/
│   ├── scoring_rules.json      # Regras de pontuação
│   ├── content_taxonomy.json   # Taxonomia de conteúdo
│   └── report_template.txt     # Template de relatório
├── examples/
│   ├── example_input.txt       # Exemplo de entrada
│   └── example_report.txt      # Exemplo de saída
└── runs/                       // Execuições salvas (bronze/silver/gold)
```

## Modos de Execução

### Modo 1: Scan Rápido
- Bio, link, 12 posts recentes
- Score inicial e gargalos principais
- Uso: triagem comercial e auditoria rápida

### Modo 2: Scan Completo
- Perfil completo, 30-60 posts, reels, destaques
- Matriz de conteúdo e plano de correção
- Uso: diagnóstico profundo e consultoria

### Modo 3: Scan Competitivo
- 1 perfil principal + 3-10 concorrentes
- Benchmark e mapa de diferenciação
- Uso: reposicionamento estratégico

### Modo 4: Scan de Conversão
- Perfil + link da bio + landing page
- Análise de coerência de jornada
- Uso: otimização de funil

## Comandos

```bash
# Scan rápido
python scripts/scan_profile.py --username <username> --mode fast

# Scan completo
python scripts/scan_profile.py --username <username> --mode full

# Scan competitivo
python scripts/scan_competitors.py --main <username> --competitors <user1,user2,user3>

# Gerar relatório
python scripts/export_report.py --run-id <run_id>
```

## Estrutura de Dados

### Entidades Normalizadas

**Profile:**
- profile_id, username, display_name, bio_text
- category, followers_count, following_count, posts_count
- external_url, is_verified, scraped_at

**Post:**
- post_id, profile_id, shortcode, content_type
- caption_text, published_at, likes_count, comments_count
- is_pinned, hashtags, mentions, first_line_hook

### Scores Gerados

- POSICIONAMENTO (0-10)
- BIO (0-10)
- OFERTA (0-10)
- CONVERSAO (0-10)
- AUTORIDADE (0-10)
- PROVA (0-10)
- CONTEUDO (0-10)
- RETENCAO (0-10)
- ESTETICA (0-10)
- CONSISTENCIA (0-10)

## Saídas

**Humanas:**
- RELATORIO_INSTAGRAM.txt
- PLANO_DE_CORRECAO_30_DIAS.txt
- RESUMO_EXECUTIVO.txt
- COMPARATIVO_CONCORRENTES.txt

**Técnicas:**
- profile.json, posts.json, features.json
- scores.json, scan_run.json

## Dependências

```
playwright>=1.40.0
duckdb>=0.9.0
python-dateutil>=2.8.0
```

## Roadmap

- [x] Fase 1: Scan rápido funcional
- [ ] Fase 2: Scan completo com classificação
- [ ] Fase 3: Scan competitivo
- [ ] Fase 4: Scan de conversão
- [ ] Fase 5: Extensão opcional
