# ARQUITETURA DE SKILLS - SISTEMA ANTIGRAVITY
## Inteligência de Negócio, Posicionamento e Estratégia Digital

---

# 1. VISÃO GERAL DO SISTEMA

O **Sistema Antigravity** é um ecossistema modular de skills projetado para transformar dados brutos de um negócio em decisões estratégicas acionáveis. Não é uma ferramenta de análise isolada, mas um motor contínuo de inteligência que opera em 4 camadas fundamentais:

```
┌─────────────────────────────────────────────────────────┐
│                    DECISÃO ESTRATÉGICA                   │
│  (O que fazer, o que priorizar, o que executar)          │
└────────────────────┬────────────────────────────────────┘
                     │ alimenta
┌────────────────────▼────────────────────────────────────┐
│                    INTERPRETAÇÃO                         │
│  (Oportunidades, gargalos, desalinhamentos, brechas)    │
└────────────────────┬────────────────────────────────────┘
                     │ alimenta
┌────────────────────▼────────────────────────────────────┐
│                    ORGANIZAÇÃO                           │
│  (Estruturação em módulos, categorização, conexão)      │
└────────────────────┬────────────────────────────────────┘
                     │ alimenta
┌────────────────────▼────────────────────────────────────┐
│                    COLETA                                │
│  (Dados do negócio, público, mercado, canais)           │
└─────────────────────────────────────────────────────────┘
```

### Princípios Operacionais

- **Fluxo Unidirecional**: Cada skill consome output de skills anteriores e gera input para skills subsequentes
- **Decisão como Produto Final**: Nenhuma skill existe sem gerar insight acionável
- **Base Viva**: A base de conhecimento é atualizada continuamente, não é arquivo morto
- **Escalabilidade Modular**: Skills podem ser ativadas/desativadas conforme necessidade

---

# 1.5 COMO ATIVAR O SISTEMA (COMANDOS)

O sistema foi desenhado para ser acionado de forma extremamente simples. Não é necessário decorar nomes de skills individuais para o uso diário.

## 1.5.1 COMANDO MESTRE (RECOMENDADO)

Para executar todo o fluxo de inteligência automaticamente, use apenas:

```
/scanner-ji [LINK OU NOME DO NEGÓCIO]
```

**Exemplos de uso:**
*   `/scanner-ji https://instagram.com/minhaclinica`
*   `/scanner-ji Dentista Implantes SP`
*   `/scanner-ji Consultoria Financeira Rio`

**O que acontece ao usar este comando:**
O orquestrador dispara automaticamente a **Stack Mínima** (8 skills nucleares) em sequência lógica:
1.  **Triagem:** Entende o nicho e oferta.
2.  **Scan:** Varre site, redes e Google.
3.  **Base:** Organiza os dados coletados.
4.  **Interpretação:** Identifica padrões do cenário.
5.  **Mineração:** Encontra oportunidades e gargalos.
6.  **Posicionamento:** Define direção estratégica.
7.  **Priorização:** Ordena o que fazer primeiro.
8.  **Plano:** Gera o plano de ação prático.

**Tempo estimado de resposta:** 2-5 minutos (dependendo da profundidade da varredura).  
**Resultado:** Um relatório estratégico completo com prioridades e próximos passos.

---

## 1.5.2 COMANDOS MODULARES (OPCIONAL)

Caso você já tenha os dados e queira rodar apenas uma etapa específica, pode chamar a skill diretamente:

| Skill | Comando Direto | Quando Usar |
| :--- | :--- | :--- |
| Triagem Rápida | `/skill-triagem` | Apenas para definir o escopo do negócio. |
| Scan Digital | `/skill-scan` | Para auditar presença digital existente. |
| Organizador de Base | `/skill-base` | Para organizar dados já coletados manualmente. |
| Interpretador | `/skill-interpretador` | Para analisar cenário de uma base pronta. |
| Minerador | `/skill-minerador` | Para achar oportunidades em uma base pronta. |
| Posicionamento | `/skill-posicionamento` | Para definir/revisar posicionamento. |
| Priorizador | `/skill-priorizador` | Para ordenar ações de uma lista existente. |
| Plano de Ação | `/skill-plano` | Para transformar insights em tarefas. |

> **Nota:** Para 95% dos casos, use apenas o comando mestre `/scanner-ji`. Os comandos modulares são para ajustes finos ou testes específicos.

---

# 2. LÓGICA DE FUNCIONAMENTO DO ECOSSISTEMA

## 2.1 Ciclo de Inteligência Contínua

```
COLETA → ORGANIZA → INTERPRETA → DECIDE → EXECUTA → (reinicio do ciclo)
   │         │           │           │          │
   ▼         ▼           ▼           ▼          ▼
  Dados   Estrutura   Insights    Ações     Resultados
  Brutos   Lógica      Padrões     Prioritárias Novos Dados
```

## 2.2 Regras de Conexão entre Skills

1. **Toda skill tem upstream e downstream**: Nenhuma skill opera isoladamente
2. **Output padronizado**: Todas as skills geram outputs em formato estruturado
3. **Base central única**: Todas as skills alimentam a mesma base de conhecimento
4. **Priorização por impacto**: Skills nucleares rodam primeiro, opcionais apenas se necessário

## 2.3 Tipos de Função das Skills

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| COLETA | Extrai dados brutos de fontes | Scan Digital, Triagem |
| ORGANIZA | Estrutura e categoriza dados | Organizador de Base |
| INTERPRETA | Identifica padrões e insights | Minerador de Mercado |
| DECIDE | Define prioridades e ações | Priorizador Estratégico |
| EXECUTA | Gera planos e materiais | Gerador de Plano de Ação |

---

# 3. STACK MÍNIMA

## Objetivo: Valor rápido com mínimo de complexidade

**Número de Skills: 8** (incluindo Engenharia Social Básica)

| # | Skill | Função | Impacto |
|---|-------|--------|---------|
| 1 | Triagem Rápida de Negócio | Coleta | Alto |
| 2 | Scan Digital Essencial | Coleta | Alto |
| 3 | Organizador de Base Mínima | Organiza | Alto |
| 4 | Interpretador de Cenário | Interpreta | Alto |
| 5 | Minerador de Oportunidades | Interpreta | Alto |
| 6 | Analista de Engenharia Social Básica | Interpreta | Alto |
| 7 | Definidor de Posicionamento | Decide | Alto |
| 8 | Priorizador de Ações + Plano Simplificado | Decide/Executa | Alto |

### Por que estas 8 skills?

- **Cobrem todo o fluxo**: Da coleta à execução, incluindo gatilhos mentais e influência
- **Eliminam redundância**: Cada uma tem função única
- **Geram valor em < 2 horas**: Processo rápido e direto
- **Servem 80% dos casos**: Negócios locais, especialistas, pequenas empresas

### O que esta stack resolve:

✅ Entende o negócio em profundidade básica  
✅ Escanea presença digital crítica  
✅ Identifica 3-5 oportunidades claras  
✅ Mapeia gatilhos mentais e alavancas de influência aplicáveis  
✅ Define posicionamento essencial  
✅ Entrega plano de ação com 5-7 passos prioritários  

### O que esta stack NÃO faz:

❌ Análise profunda de SEO técnico  
❌ Pesquisa avançada de concorrência  
❌ Segmentação complexa de público  
❌ Automação de conteúdo  
❌ Engenharia social avançada (campanhas coordenadas, manipulação de massa)  

---

# 4. STACK PROFISSIONAL

## Objetivo: Operação consistente com qualidade superior

**Número de Skills: 15**

### Adições à Stack Mínima:

| # | Skill | Função | Impacto |
|---|-------|--------|---------|
| 9 | Pesquisador de Público Profundo | Coleta | Alto |
| 10 | Minerador de Concorrência | Coleta | Médio |
| 11 | Analisador de SEO Básico | Coleta | Médio |
| 12 | Avaliador de Conteúdo Instagram | Interpreta | Médio |
| 13 | Mapeador de Jornada do Cliente | Interpreta | Alto |
| 14 | Validador de Oferta | Interpreta | Alto |
| 15 | Estruturador de Mensagem + Engenharia Social Aplicada | Decide | Alto |

### Por que expandir para 15 skills?

- **Melhora qualidade de leitura**: Mais dados = melhores insights
- **Cobre mais cenários**: Atende consultorias, clínicas, marcas pessoais
- **Aumenta precisão**: Validação cruzada entre skills
- **Permite personalização**: Adaptação a diferentes maturidades
- **Aplica engenharia social estratégica**: Gatilhos mentais integrados à mensagem

### O que esta stack resolve além da mínima:

✅ Pesquisa de dores e desejos do público  
✅ Análise de 3-5 concorrentes diretos  
✅ Avaliação de SEO on-page básico  
✅ Audit de conteúdo do Instagram  
✅ Mapeamento de jornada de compra  
✅ Validação de clareza da oferta  
✅ Estruturação de mensagem-chave com gatilhos mentais  
✅ Aplicação de princípios de influência (Cialdini, Fogg, hooks comportamentais)  

---

# 5. STACK AVANÇADA

## Objetivo: Inteligência contínua, especialização e blindagem estratégica

**Número de Skills: 26** (incluindo Engenharia Social Profunda, Risco Reputacional, Tradutor Operacional e Detector de Pivotagem)

### Adições à Stack Profissional:

| # | Skill | Função | Impacto |
|---|-------|--------|---------|
| 16 | Rastreador de Tendências de Nicho | Coleta | Médio |
| 17 | Analisador de Reviews e Reputação | Coleta | Médio |
| 18 | Pesquisador de Intenção de Busca | Coleta | Alto |
| 19 | Segmentador de Personas | Organiza | Médio |
| 20 | Comparador de Diferenciação | Interpreta | Alto |
| 21 | Detector de Gargalos de Conversão | Interpreta | Alto |
| 22 | Otimizador de Funil | Interpreta | Médio |
| 23 | Planejador de Conteúdo Estratégico | Decide | Alto |
| 24 | Calibrador de Canais | Decide | Médio |
| 25 | Monitor de Evolução de Mercado | Interpreta | Médio |
| 26 | Gerador de Roadmap Trimestral | Executa | Alto |
| 27 | Auditor de Coerência Geral | Interpreta | Alto |
| 28 | Estrategista de Engenharia Social Profunda | Decide/Executa | Alto |
| 29 | **Auditor de Risco Reputacional** | Interpreta/Decide | **CRÍTICO** |
| 30 | **Tradutor Operacional de Estratégia** | Decide/Executa | **CRÍTICO** |
| 31 | **Detector de Estagnação & Pivotagem** | Interpreta/Decide | **ALTO** |
| 32 | **Orquestrador de Inteligência Contínua** | Organiza/Decide | **CRÍTICO** |

### Por que expandir para 26 skills?

- **Inteligência contínua**: Monitoramento constante do mercado
- **Profundidade analítica**: Camadas adicionais de interpretação
- **Especialização**: Suporte a negócios mais complexos
- **Escala futura**: Preparação para crescimento
- **Engenharia social avançada**: Campanhas coordenadas, manipulação ética de comportamento, prova social orquestrada
- **BLINDAGEM ESTRATÉGICA**: Prevenção de riscos reputacionais e legais antes da execução
- **PONTE DE EXECUÇÃO**: Tradução de estratégia abstrata em tarefas operacionais claras
- **ADAPTABILIDADE**: Detecção precoce de estagnação e gatilhos para pivotagem
- **ORQUESTRAÇÃO CONTÍNUA**: Sistema auto-alimentado de melhoria e atualização

### O que esta stack resolve além da profissional:

✅ Detecção de tendências emergentes no nicho  
✅ Análise profunda de reviews e sentimentos do público  
✅ Mapeamento de intenção de busca em múltiplas camadas  
✅ Segmentação avançada de personas por comportamento  
✅ Comparação competitiva com identificação de brechas  
✅ Detecção de gargalos ocultos de conversão  
✅ Otimização de funil com testes estruturados  
✅ Planejamento de conteúdo com calendário estratégico  
✅ Calibração fina de canais por performance  
✅ Monitoramento de evolução de mercado em tempo real  
✅ Roadmap trimestral com marcos claros  
✅ Auditoria de coerência entre todos os elementos da marca  
✅ **Engenharia social profunda**: loops de influência, autoridade construída, validação em cascata  
✅ **AUDITORIA DE RISCO**: Cancelamento, polêmicas, conformidade legal, sensibilidade cultural  
✅ **TRADUÇÃO OPERACIONAL**: Checklist executivo, delegação clara, prazos realistas  
✅ **DETECTOR DE PIVOTAGEM**: Sinais de saturação, métricas de alerta, plano B acionável  
✅ **ORQUESTRAÇÃO CONTÍNUA**: Ciclo automático de coleta-interpretação-decisão-ação  
✅ Análise sistemática de reviews e reputação  
✅ Pesquisa avançada de intenção de busca  
✅ Segmentação detalhada de personas  
✅ Comparação competitiva de diferenciação  
✅ Identificação de gargalos específicos de conversão  
✅ Otimização de funil completo  
✅ Planejamento de conteúdo trimestral  
✅ Alocação estratégica de orçamento por canal  
✅ Monitoramento contínuo de evolução de mercado  
✅ Roadmap estratégico de 90 dias  
✅ Auditoria completa de coerência de marca  
✅ **Engenharia social profunda**: Orquestração de prova social, gatilhos de escassez, autoridade construída, influência em massa ética  

---

# 6. DETALHAMENTO DE CADA SKILL

## STACK MÍNIMA

---

### SKILL 01: Triagem Rápida de Negócio

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Extrair informações fundamentais sobre o negócio em formato estruturado para alimentar todas as skills subsequentes.

**O que ela analisa:**
- Nicho e segmento de atuação
- Oferta principal e secundárias
- Público-alvo declarado
- Estágio de maturidade do negócio
- Canais ativos atualmente
- Objetivo comercial primário
- Faturamento atual (faixa)
- Equipe e recursos disponíveis

**Input Necessário:**
- Questionário inicial (15-20 perguntas)
- URL do site (se existir)
- URLs de redes sociais
- Entrevista rápida de 30 min (opcional)

**Processo Interno:**
1. Aplicar questionário estruturado
2. Categorizar tipo de negócio (local, digital, especialista, etc.)
3. Classificar nível de maturidade (iniciante, intermediário, avançado)
4. Identificar objetivo primário (vendas, leads, autoridade, etc.)
5. Mapear recursos disponíveis (tempo, orçamento, equipe)

**Output Gerado:**
```json
{
  "tipo_negocio": "",
  "nicho": "",
  "oferta_principal": "",
  "publico_declarado": "",
  "maturidade": "",
  "canais_ativos": [],
  "objetivo_comercial": "",
  "recursos_disponiveis": {
    "tempo_semanal_horas": 0,
    "orcamento_mensal": 0,
    "equipe_size": 0
  }
}
```

**Como ela se conecta com as outras:**
- Alimenta: Scan Digital, Organizador de Base, Pesquisador de Público
- Recebe de: Nenhuma (skill de entrada)

**Quando usar:**
- ✅ Início de qualquer projeto
- ✅ Reavaliação trimestral do negócio
- ✅ Mudança significativa de oferta ou público

**Quando NÃO usar:**
- ❌ Negócio já totalmente mapeado nos últimos 30 dias
- ❌ Apenas para ajuste menor de estratégia

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: SOBRE O NEGÓCIO
- Arquivo: `base_negocio.json`

**Impacto no Negócio:** ALTO  
*Sem esta skill, todo o sistema opera sem contexto adequado.*

---

### SKILL 02: Scan Digital Essencial

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Mapear a presença digital atual do negócio e identificar gaps básicos de existência online.

**O que ela analisa:**
- Existência e qualidade do site
- Perfil do Instagram (bio, destaques, feed recente)
- Perfil do Facebook (se relevante)
- Google Meu Negócio (existência e completude)
- Consistência de NAP (Name, Address, Phone)
- Presença em outros canais relevantes (LinkedIn, YouTube, TikTok)

**Input Necessário:**
- Nome do negócio
- URLs fornecidas na Triagem
- Localização física (se aplicável)
- Nicho de atuação

**Processo Interno:**
1. Verificar existência de site e status (ativo/inativo)
2. Analisar bio do Instagram (clareza, CTA, link)
3. Contar posts recentes e frequência (últimos 30 dias)
4. Verificar Google Meu Negócio (reivindicado? completo?)
5. Checar consistência de informações entre canais
6. Identificar canais ausentes mas relevantes para o nicho

**Output Gerado:**
```json
{
  "site": {
    "existe": false,
    "url": "",
    "status": "",
    "qualidade_basica": ""
  },
  "instagram": {
    "existe": false,
    "url": "",
    "bio_clara": false,
    "destaques_organizados": false,
    "frequencia_posts": "",
    "engagement_medio": 0
  },
  "google_meu_negocio": {
    "existe": false,
    "reivindicado": false,
    "completo": false,
    "reviews_count": 0,
    "nota_media": 0
  },
  "outros_canais": [],
  "gaps_identificados": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Interpretador de Cenário, Avaliador de Conteúdo Instagram
- Recebe de: Triagem Rápida de Negócio

**Quando usar:**
- ✅ Início de projeto
- ✅ Antes de definir estratégia de canais
- ✅ Quando há suspeita de presença digital fraca

**Quando NÃO usar:**
- ❌ Negócio 100% offline sem intenção de digitalizar
- ❌ Se scan foi realizado nos últimos 15 dias sem mudanças

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: INSTAGRAM E CONTEÚDO
- Módulo: SEO E BUSCA
- Arquivo: `base_canais.json`

**Impacto no Negócio:** ALTO  
*Identifica onde o negócio está invisível ou mal posicionado.*

---

### SKILL 03: Organizador de Base Mínima

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** ORGANIZA  

**Missão da Skill:**  
Estruturar todos os dados coletados em uma base de conhecimento unificada e acessível.

**O que ela analisa:**
- Dados vindos da Triagem
- Dados vindos do Scan Digital
- Redundâncias entre informações
- Lacunas de informação crítica
- Prioridade de preenchimento de lacunas

**Input Necessário:**
- Output da Triagem Rápida de Negócio
- Output do Scan Digital Essencial

**Processo Interno:**
1. Consolidar dados em estrutura única
2. Identificar campos vazios críticos
3. Marcar informações conflitantes para revisão
4. Criar índice de completude da base (0-100%)
5. Gerar lista de informações faltantes prioritárias

**Output Gerado:**
```json
{
  "base_completa": {},
  "indice_completude": 0,
  "informacoes_faltantes": [],
  "informacoes_conflitantes": [],
  "proximos_dados_necessarios": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Todas as skills de interpretação e decisão
- Recebe de: Triagem, Scan Digital, Pesquisador de Público

**Quando usar:**
- ✅ Após cada rodada de coleta de dados
- ✅ Antes de iniciar interpretação
- ✅ Semanalmente para atualização

**Quando NÃO usar:**
- ❌ Se nenhuma nova informação foi coletada desde a última organização

**Qual base, arquivo ou módulo ela alimenta:**
- TODOS OS MÓDULOS DA BASE
- Arquivo: `base_mestra.json`

**Impacto no Negócio:** ALTO  
*Sem organização, os dados coletados são inúteis para decisão.*

---

### SKILL 04: Interpretador de Cenário

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Transformar dados organizados em insights sobre a situação atual do negócio.

**O que ela analisa:**
- Completude da presença digital
- Consistência de mensagem entre canais
- Alinhamento entre oferta e canais usados
- Maturidade digital vs. maturidade de negócio
- Recursos disponíveis vs. ambições declaradas

**Input Necessário:**
- Output do Organizador de Base Mínima
- Benchmark do nicho (dados gerais)

**Processo Interno:**
1. Comparar presença atual vs. esperado para o nicho
2. Identificar desalinhamentos (ex: produto premium em canal amador)
3. Detectar gargalos óbvios (ex: sem site mas investe em ads)
4. Classificar cenário geral (fraco, regular, bom, excelente)
5. Listar 3-5 problemas centrais a resolver

**Output Gerado:**
```json
{
  "cenario_geral": "",
  "pontos_fortes": [],
  "problemas_centrais": [],
  "desalinhamentos": [],
  "gargalos_obvios": [],
  "nivel_maturidade_digital": "",
  "recomendacoes_gerais": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Minerador de Oportunidades, Priorizador de Ações
- Recebe de: Organizador de Base Mínima

**Quando usar:**
- ✅ Após organizar a base
- ✅ Antes de definir prioridades
- ✅ Em reavaliações de estratégia

**Quando NÃO usar:**
- ❌ Se a base está incompleta (>40% vazia)
- ❌ Se não há dados suficientes para interpretação

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: OPORTUNIDADES
- Arquivo: `base_interpretacao.json`

**Impacto no Negócio:** ALTO  
*Transforma dados brutos em compreensão clara da situação.*

---

### SKILL 05: Minerador de Oportunidades

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Identificar oportunidades concretas de melhoria e crescimento baseadas no cenário interpretado.

**O que ela analisa:**
- Problemas centrais identificados
- Gargalos óbvios
- Desalinhamentos detectados
- Recursos disponíveis
- Objetivos declarados

**Input Necessário:**
- Output do Interpretador de Cenário
- Output da Triagem (recursos e objetivos)

**Processo Interno:**
1. Para cada problema, identificar solução possível
2. Classificar soluções por: impacto x esforço
3. Identificar "quick wins" (alto impacto, baixo esforço)
4. Detectar oportunidades de diferenciação
5. Mapear brechas não exploradas pelo negócio

**Output Gerado:**
```json
{
  "oportunidades": [
    {
      "descricao": "",
      "impacto": "",
      "esforco": "",
      "prioridade": "",
      "prazo_estimado": ""
    }
  ],
  "quick_wins": [],
  "oportunidades_diferenciacao": [],
  "brechas_nao_exploradas": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Priorizador de Ações, Definidor de Posicionamento
- Recebe de: Interpretador de Cenário

**Quando usar:**
- ✅ Após interpretação do cenário
- ✅ Antes de priorizar ações
- ✅ Em sessões de planejamento

**Quando NÃO usar:**
- ❌ Se o cenário ainda não foi interpretado
- ❌ Se não há clareza sobre recursos disponíveis

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: OPORTUNIDADES
- Arquivo: `base_oportunidades.json`

**Impacto no Negócio:** ALTO  
*Transforma problemas em caminhos claros de ação.*

---

### SKILL 06: Analista de Engenharia Social Básica

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Mapear gatilhos mentais, alavancas de influência e princípios de persuasão aplicáveis ao negócio com base no público e cenário identificados.

**O que ela analisa:**
- Perfil psicológico do público-alvo
- Dores e desejos emocionais
- Objeções conscientes e inconscientes
- Comportamentos observados nos canais
- Linguagem utilizada pelo público
- Contexto de decisão de compra

**Input Necessário:**
- Output da Triagem Rápida de Negócio
- Output do Scan Digital Essencial
- Output do Interpretador de Cenário (se disponível)

**Processo Interno:**
1. Identificar os 3-5 gatilhos mentais mais relevantes para o nicho (urgência, escassez, autoridade, prova social, reciprocidade, etc.)
2. Mapear alavancas de influência específicas (Cialdini, Fogg Behavior Model)
3. Detectar padrões de comportamento observáveis nos canais
4. Identificar oportunidades de prova social
5. Sugerir elementos de persuasão ética aplicáveis imediatamente

**Output Gerado:**
```json
{
  "gatilhos_mentais_prioritarios": [
    {
      "gatilho": "",
      "justificativa": "",
      "aplicacao_sugerida": ""
    }
  ],
  "alavancas_influencia": [],
  "oportunidades_prova_social": [],
  "padroes_comportamentais": [],
  "recomendacoes_persuasao_etica": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Definidor de Posicionamento, Estruturador de Mensagem
- Recebe de: Triagem Rápida, Scan Digital, Interpretador de Cenário

**Quando usar:**
- ✅ Após entender o público e o cenário
- ✅ Antes de definir posicionamento e mensagem
- ✅ Em qualquer negócio que precise influenciar decisões

**Quando NÃO usar:**
- ❌ Se não há clareza sobre quem é o público
- ❌ Em contextos onde manipulação antiética seria necessária (a skill foca em persuasão ética)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PÚBLICO E MERCADO (subseção: Psicologia e Influência)
- Módulo: POSICIONAMENTO (subseção: Gatilhos e Persuasão)
- Arquivo: `base_engenharia_social_basica.json`

**Impacto no Negócio:** ALTO  
*Transforma compreensão do público em alavancas práticas de influência e conversão.*

---

### SKILL 07: Definidor de Posicionamento

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** DECIDE  

**Missão da Skill:**  
Estabelecer ou refinar o posicionamento estratégico do negócio baseado nas oportunidades identificadas.

**O que ela analisa:**
- Oferta atual do negócio
- Oportunidades de diferenciação
- Público-alvo
- Concorrência (dados básicos)
- Recursos e capacidades únicas

**Input Necessário:**
- Output da Triagem (oferta, público)
- Output do Minerador de Oportunidades
- Dados básicos de concorrência (se disponíveis)

**Processo Interno:**
1. Identificar atributos únicos do negócio
2. Mapear espaço competitivo disponível
3. Definir promessa central de valor
4. Estabelecer tom de voz e personalidade
5. Criar statement de posicionamento claro

**Output Gerado:**
```json
{
  "posicionamento": {
    "promessa_central": "",
    "diferencial_principal": "",
    "publico_foco": "",
    "tom_de_voz": "",
    "statement_posicionamento": "",
    "palavras_chave_posicionamento": []
  },
  "recomendacoes_alinhamento": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Estruturador de Mensagem, Gerador de Plano Simplificado
- Recebe de: Minerador de Oportunidades, Triagem

**Quando usar:**
- ✅ Negócio sem posicionamento claro
- ✅ Reposicionamento necessário
- ✅ Lançamento de nova oferta

**Quando NÃO usar:**
- ❌ Posicionamento já definido e validado recentemente
- ❌ Se não há clareza sobre oferta e público

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: POSICIONAMENTO
- Arquivo: `base_posicionamento.json`

**Impacto no Negócio:** ALTO  
*Posicionamento claro é pré-requisito para toda comunicação eficaz.*

---

### SKILL 07: Priorizador de Ações

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** DECIDE  

**Missão da Skill:**  
Transformar oportunidades em prioridades claras de ação baseadas em impacto, esforço e recursos.

**O que ela analisa:**
- Lista de oportunidades identificadas
- Recursos disponíveis (tempo, orçamento, equipe)
- Objetivos comerciais declarados
- Quick wins identificados
- Dependências entre ações

**Input Necessário:**
- Output do Minerador de Oportunidades
- Output da Triagem (recursos)
- Output do Definidor de Posicionamento

**Processo Interno:**
1. Classificar todas as ações por matriz impacto x esforço
2. Considerar recursos disponíveis para filtrar viáveis
3. Identificar dependências e sequenciamento lógico
4. Selecionar top 5-7 prioridades para próximo ciclo
5. Estimar prazo realista para cada prioridade

**Output Gerado:**
```json
{
  "prioridades": [
    {
      "acao": "",
      "impacto_esperado": "",
      "esforco_necessario": "",
      "prazo_estimado": "",
      "recursos_necessarios": "",
      "dependencias": [],
      "ordem_execucao": 0
    }
  ],
  "o_que_ignorar_agora": [],
  "o_que_manter_como_esta": [],
  "sequencia_recomendada": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Gerador de Plano Simplificado
- Recebe de: Minerador de Oportunidades, Definidor de Posicionamento

**Quando usar:**
- ✅ Após identificar oportunidades
- ✅ Antes de criar plano de ação
- ✅ Em revisões quinzenais de prioridade

**Quando NÃO usar:**
- ❌ Se não há lista de oportunidades clara
- ❌ Se recursos não foram mapeados

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PRIORIDADES
- Arquivo: `base_prioridades.json`

**Impacto no Negócio:** ALTO  
*Foco é o multiplicador de força mais poderoso em estratégia.*

---

### SKILL 08: Gerador de Plano Simplificado

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** EXECUTA  

**Missão da Skill:**  
Transformar prioridades em um plano de ação concreto, passo a passo, pronto para execução.

**O que ela analisa:**
- Prioridades definidas
- Sequência recomendada
- Recursos disponíveis
- Prazos estimados

**Input Necessário:**
- Output do Priorizador de Ações
- Output da Triagem (recursos detalhados)

**Processo Interno:**
1. Para cada prioridade, quebrar em passos executáveis
2. Atribuir responsáveis (ou "auto-gerido" se solo)
3. Definir métricas de sucesso para cada passo
4. Estabelecer checkpoints de revisão
5. Criar calendário sugerido de execução

**Output Gerado:**
```json
{
  "plano_acao": {
    "ciclo": "30 dias",
    "acoes": [
      {
        "prioridade": 1,
        "titulo": "",
        "passos": [
          {"passo": 1, "descricao": "", "prazo": "", "responsavel": ""}
        ],
        "metrica_sucesso": "",
        "checkpoint_data": ""
      }
    ]
  },
  "calendario_sugerido": [],
  "metricas_gerais_sucesso": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Execução (humana ou automatizada)
- Recebe de: Priorizador de Ações

**Quando usar:**
- ✅ Após priorização concluída
- ✅ Início de cada ciclo de execução
- ✅ Quando há necessidade de clareza operacional

**Quando NÃO usar:**
- ❌ Se não há prioridades definidas
- ❌ Se o plano anterior ainda não foi executado

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PLANO DE AÇÃO
- Arquivo: `base_plano_acao.json`

**Impacto no Negócio:** ALTO  
*Estratégia sem plano de execução é apenas teoria.*

---

## STACK PROFISSIONAL (Skills Adicionais)

---

### SKILL 09: Pesquisador de Público Profundo

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Ir além do público declarado e entender dores reais, desejos, objeções e linguagem do cliente ideal.

**O que ela analisa:**
- Comentários em posts de concorrentes
- Reviews de produtos/serviços similares
- Grupos e comunidades do nicho
- Perguntas frequentes no Google e Reddit
- Linguagem usada pelo público em fóruns

**Input Necessário:**
- Nicho definido (da Triagem)
- Público declarado (da Triagem)
- Lista de concorrentes e comunidades

**Processo Interno:**
1. Coletar 50-100 comentários/posts de públicos reais
2. Extrair dores mencionadas explicitamente
3. Identificar desejos e aspirações
4. Mapear objeções comuns à compra
5. Catalogar palavras e frases usadas pelo público
6. Classificar por frequência e intensidade emocional

**Output Gerado:**
```json
{
  "dores_principais": [],
  "desejos_principais": [],
  "objecoes_comuns": [],
  "linguagem_do_publico": {
    "palavras_frequentes": [],
    "frases_recorrentes": [],
    "tom_emocional": ""
  },
  "sintomas_mencionados": [],
  "estados_consciencia": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Estruturador de Mensagem
- Recebe de: Triagem Rápida de Negócio

**Quando usar:**
- ✅ Lançamento de novo produto/serviço
- ✅ Refinamento de messaging
- ✅ Criação de conteúdo mais conectado

**Quando NÃO usar:**
- ❌ Público já profundamente pesquisado nos últimos 60 dias
- ❌ Nicho muito pequeno sem dados disponíveis

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PÚBLICO E MERCADO
- Arquivo: `base_publico.json`

**Impacto no Negócio:** ALTO  
*Conexão emocional com o público depende de entendimento profundo.*

---

### SKILL 10: Minerador de Concorrência

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Mapear concorrentes diretos e indiretos para identificar padrões do nicho e oportunidades de diferenciação.

**O que ela analisa:**
- Top 5-10 concorrentes diretos
- Posicionamento de cada um
- Ofertas e preços
- Presença digital e canais
- Conteúdo produzido
- Reviews e reputação

**Input Necessário:**
- Nicho definido
- Localização (se negócio local)
- Faixa de preço da oferta

**Processo Interno:**
1. Identificar concorrentes via busca Google e Instagram
2. Analisar site e redes de cada concorrente
3. Extrair oferta, preço e posicionamento
4. Mapear canais ativos e frequência
5. Identificar padrões repetidos no nicho
6. Detectar brechas não exploradas

**Output Gerado:**
```json
{
  "concorrentes": [
    {
      "nome": "",
      "url": "",
      "oferta": "",
      "preco": "",
      "posicionamento": "",
      "canais_ativos": [],
      "pontos_fortes": [],
      "pontos_fracos": []
    }
  ],
  "padroes_nicho": [],
  "repeticoes_comuns": [],
  "brechas_identificadas": [],
  "oportunidades_diferenciacao": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Comparador de Diferenciação
- Recebe de: Triagem Rápida de Negócio

**Quando usar:**
- ✅ Entrada em novo mercado
- ✅ Perda de competitividade percebida
- ✅ Desenvolvimento de nova oferta

**Quando NÃO usar:**
- ❌ Concorrência já mapeada recentemente (< 45 dias)
- ❌ Nicho com menos de 3 players (dados limitados)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: CONCORRÊNCIA
- Arquivo: `base_concorrencia.json`

**Impacto no Negócio:** MÉDIO  
*Entender a concorrência evita erros comuns e revela espaços vazios.*

---

### SKILL 11: Analisador de SEO Básico

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Avaliar a saúde básica de SEO do site e identificar oportunidades de busca orgânica.

**O que ela analisa:**
- Estrutura técnica básica do site
- Palavras-chave atuais (se houver)
- Conteúdo existente e otimização
- Velocidade de carregamento
- Mobile-friendliness
- Intenções de busca relevantes ao nicho

**Input Necessário:**
- URL do site
- Nicho de atuação
- Público-alvo

**Processo Interno:**
1. Verificar indexação no Google
2. Analisar title tags e meta descriptions
3. Identificar palavras-chave alvo potenciais
4. Avaliar qualidade e profundidade do conteúdo
5. Checar performance mobile e velocidade
6. Mapear intenções de busca do público

**Output Gerado:**
```json
{
  "seo_tecnico": {
    "indexado": false,
    "mobile_friendly": false,
    "velocidade": "",
    "ssl": false
  },
  "palavras_chave_oportunidade": [],
  "conteudo_existente": {
    "quantidade_paginas": 0,
    "qualidade_media": "",
    "gaps_conteudo": []
  },
  "intencoes_busca_mapeadas": [],
  "recomendacoes_seo": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Planejador de Conteúdo Estratégico
- Recebe de: Triagem, Pesquisador de Público Profundo

**Quando usar:**
- ✅ Site existente precisa de otimização
- ✅ Planejamento de novo site
- ✅ Queda de tráfego orgânico

**Quando NÃO usar:**
- ❌ Negócio sem site e sem plano de ter um
- ❌ SEO já auditado recentemente por especialista

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: SEO E BUSCA
- Arquivo: `base_seo.json`

**Impacto no Negócio:** MÉDIO  
*SEO bem feito traz tráfego qualificado de forma sustentável.*

---

### SKILL 12: Avaliador de Conteúdo Instagram

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Analisar o conteúdo atual do Instagram e identificar padrões de desempenho e oportunidades de melhoria.

**O que ela analisa:**
- Últimos 30-50 posts do feed
- Destaques organizados
- Bio e link na bio
- Engajamento por tipo de conteúdo
- Consistência visual e de mensagem
- Alinhamento com posicionamento

**Input Necessário:**
- URL do Instagram
- Posicionamento definido
- Público-alvo

**Processo Interno:**
1. Categorizar tipos de conteúdo postados
2. Medir engajamento médio por categoria
3. Identificar top 5 posts (mais engajamento)
4. Analisar coerência visual e de mensagem
5. Verificar alinhamento bio → destaques → feed
6. Detectar conteúdos genéricos vs. diferenciados

**Output Gerado:**
```json
{
  "tipos_conteudo": [],
  "engagement_por_tipo": {},
  "top_posts": [],
  "padroes_sucesso": [],
  "problemas_identificados": [],
  "coerencia_visual": "",
  "coerencia_mensagem": "",
  "alinhamento_posicionamento": "",
  "recomendacoes_conteudo": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Planejador de Conteúdo Estratégico
- Recebe de: Scan Digital, Definidor de Posicionamento

**Quando usar:**
- ✅ Instagram é canal principal
- ✅ Engajamento abaixo do esperado
- ✅ Planejamento de nova fase de conteúdo

**Quando NÃO usar:**
- ❌ Instagram não é relevante para o negócio
- ❌ Conta nova sem histórico suficiente (< 20 posts)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: INSTAGRAM E CONTEÚDO
- Arquivo: `base_conteudo_ig.json`

**Impacto no Negócio:** MÉDIO  
*Conteúdo alinhado e estratégico multiplica resultados no Instagram.*

---

### SKILL 13: Mapeador de Jornada do Cliente

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Entender o caminho completo que o cliente percorre desde a descoberta até a compra e além.

**O que ela analisa:**
- Pontos de contato atuais do negócio
- Etapas de conscientização do público
- Gatilhos de decisão de compra
- Objeções em cada etapa
- Momentos de verdade na experiência

**Input Necessário:**
- Oferta definida
- Público pesquisado
- Canais ativos
- Processo de vendas atual

**Processo Interno:**
1. Mapear etapas de consciência (desconhecido → cliente)
2. Identificar canais de descoberta em cada etapa
3. Mapear informações necessárias em cada fase
4. Detectar pontos de atrito e abandono
5. Identificar momentos críticos de decisão
6. Propor melhorias na jornada

**Output Gerado:**
```json
{
  "jornada_mapeada": {
    "etapas": [
      {
        "nome": "",
        "consciencia_cliente": "",
        "canais_toque": [],
        "informacoes_necessarias": [],
        "objecoes_comuns": [],
        "pontos_atrito": []
      }
    ]
  },
  "momentos_verdade": [],
  "oportunidades_otimizacao": [],
  "gargalos_conversao": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Detector de Gargalos de Conversão
- Recebe de: Pesquisador de Público Profundo, Triagem

**Quando usar:**
- ✅ Taxa de conversão abaixo do esperado
- ✅ Muitas dúvidas repetitivas de clientes
- ✅ Otimização de funil de vendas

**Quando NÃO usar:**
- ❌ Venda simples de impulso (baixa complexidade)
- ❌ Jornada já mapeada e validada recentemente

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: OFERTA E CONVERSÃO
- Arquivo: `base_jornada_cliente.json`

**Impacto no Negócio:** ALTO  
*Jornada otimizada aumenta conversão sem aumentar tráfego.*

---

### SKILL 14: Validador de Oferta

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Avaliar se a oferta atual é clara, atraente e alinhada com as necessidades do público.

**O que ela analisa:**
- Clareza da proposta de valor
- Alinhamento com dores do público
- Diferenciação vs. concorrência
- Preço vs. valor percebido
- Prova social disponível
- Garantia e redução de risco

**Input Necessário:**
- Oferta atual descrita
- Pesquisa de público
- Análise de concorrência
- Posicionamento definido

**Processo Interno:**
1. Avaliar clareza da promessa (teste dos 5 segundos)
2. Verificar conexão com dores principais do público
3. Comparar com ofertas concorrentes
4. Analisar preço em relação ao valor entregue
5. Checar existência e qualidade de prova social
6. Identificar elementos de redução de risco

**Output Gerado:**
```json
{
  "clareza_oferta": "",
  "alinhamento_publico": "",
  "diferenciacao": "",
  "preco_valor_percebido": "",
  "prova_social": {
    "existe": false,
    "qualidade": "",
    "tipos": []
  },
  "reducao_risco": {
    "garantia": false,
    "elementos_confianca": []
  },
  "pontos_fraca_oferta": [],
  "recomendacoes_melhoria": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Definidor de Posicionamento
- Recebe de: Triagem, Pesquisador de Público, Minerador de Concorrência

**Quando usar:**
- ✅ Baixa conversão em vendas
- ✅ Muitas objeções no processo
- ✅ Lançamento de nova oferta
- ✅ Reposicionamento de oferta existente

**Quando NÃO usar:**
- ❌ Oferta recém-lançada sem dados de mercado
- ❌ Validação já realizada recentemente (< 30 dias)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: OFERTA E CONVERSÃO
- Arquivo: `base_oferta.json`

**Impacto no Negócio:** ALTO  
*Oferta clara e alinhada é o coração da conversão.*

---

### SKILL 15: Estruturador de Mensagem + Engenharia Social Aplicada

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** DECIDE  

**Missão da Skill:**  
Criar a estrutura de messaging principal que será usada em todos os canais de comunicação, integrando gatilhos mentais e princípios de influência identificados pela engenharia social.

**O que ela analisa:**
- Posicionamento definido
- Dores e desejos do público
- Diferenciais da oferta
- Linguagem do público
- Tom de voz da marca
- Gatilhos mentais prioritários (da Skill 06)
- Alavancas de influência aplicáveis

**Input Necessário:**
- Output do Definidor de Posicionamento
- Output do Pesquisador de Público Profundo
- Output do Validador de Oferta
- Output do Analista de Engenharia Social Básica

**Processo Interno:**
1. Extrair elementos-chave do posicionamento
2. Conectar com linguagem real do público
3. Integrar gatilhos mentais prioritários na mensagem
4. Criar headline principal (promessa clara + gatilho)
5. Desenvolver sub-headlines de apoio com alavancas de influência
6. Estruturar pilares de mensagem persuasiva
7. Definir CTAs principais e secundários otimizados para conversão
8. Aplicar princípios de Cialdini (prova social, autoridade, escassez, etc.)

**Output Gerado:**
```json
{
  "messaging_principal": {
    "headline": "",
    "sub_headlines": [],
    "promessa_central": "",
    "pilares_mensagem": [],
    "ctas_principais": [],
    "ctas_secundarios": [],
    "gatilhos_integrados": []
  },
  "variacao_por_canal": {},
  "palavras_usar": [],
  "palavras_evitar": [],
  "tom_voz_detalhado": "",
  "elementos_persuasao": {
    "prova_social": [],
    "autoridade": [],
    "urgencia_escassez": [],
    "reciprocidade": []
  }
}
```

**Como ela se conecta com as outras:**
- Alimenta: Gerador de Plano Simplificado, Planejador de Conteúdo Estratégico
- Recebe de: Definidor de Posicionamento, Pesquisador de Público, Validador de Oferta, Analista de Engenharia Social

**Quando usar:**
- ✅ Posicionamento recém-definido
- ✅ Inconsistência de mensagem entre canais
- ✅ Criação de novos materiais de comunicação
- ✅ Otimização de páginas de vendas/landing pages

**Quando NÃO usar:**
- ❌ Messaging já definido e testado com sucesso
- ❌ Se posicionamento ainda não está claro
- ❌ Se não há dados de engenharia social disponíveis

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: POSICIONAMENTO
- Módulo: PÚBLICO E MERCADO (subseção: Psicologia e Influência)
- Arquivo: `base_messaging.json`

**Impacto no Negócio:** ALTO  
*Mensagem clara, consistente e psicologicamente otimizada multiplica eficácia de toda comunicação e conversão.*

---

## STACK AVANÇADA (Skills Adicionais)

---

### SKILL 16: Rastreador de Tendências de Nicho

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Monitorar tendências emergentes no nicho para antecipar movimentos de mercado.

**O que ela analisa:**
- Assuntos em alta no nicho
- Novos players entrando no mercado
- Mudanças de comportamento do consumidor
- Tecnologias ou métodos emergentes
- Conteúdo viral do nicho

**Input Necessário:**
- Nicho definido
- Fontes de monitoramento (Google Trends, Instagram, etc.)
- Período de análise

**Processo Interno:**
1. Consultar Google Trends para termos do nicho
2. Analisar hashtags em crescimento no Instagram
3. Monitorar publicações e notícias do setor
4. Identificar padrões de conteúdo viral
5. Detectar novos concorrentes ganhando tração
6. Sintetizar tendências por relevância e timing

**Output Gerado:**
```json
{
  "tendencias_emergentes": [
    {
      "tema": "",
      "sinal_forca": "",
      "timing_estimado": "",
      "relevancia_negocio": "",
      "acao_recomendada": ""
    }
  ],
  "assuntos_alta": [],
  "novos_players": [],
  "mudancas_comportamento": [],
  "oportunidades_antecipacao": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Monitor de Evolução de Mercado
- Recebe de: Triagem, Minerador de Concorrência

**Quando usar:**
- ✅ Planejamento trimestral ou anual
- ✅ Mercados de rápida evolução
- ✅ Busca por vantagem competitiva

**Quando NÃO usar:**
- ❌ Nichos muito estáveis e maduros
- ❌ Recursos limitados (focar no essencial primeiro)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: MERCADO (apoio)
- Arquivo: `base_tendencias.json`

**Impacto no Negócio:** MÉDIO  
*Antecipar tendências cria vantagem competitiva significativa.*

---

### SKILL 17: Analisador de Reviews e Reputação

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Analisar sistematicamente reviews e menções para entender percepção pública e identificar problemas.

**O que ela analisa:**
- Reviews no Google Meu Negócio
- Reviews em plataformas específicas do nicho
- Menções em redes sociais
- Reclamações recorrentes
- Elogios recorrentes
- Sentimento geral (positivo/negativo/neutro)

**Input Necessário:**
- Nome do negócio
- URLs de perfis (Google, Instagram, etc.)
- Plataformas relevantes do nicho

**Processo Interno:**
1. Coletar todos os reviews disponíveis
2. Classificar por estrela/Nota
3. Extrair temas recorrentes em elogios
4. Extrair temas recorrentes em críticas
5. Analisar sentimento geral
6. Identificar problemas sistêmicos

**Output Gerado:**
```json
{
  "resumo_reviews": {
    "total": 0,
    "nota_media": 0,
    "distribuicao_notas": {}
  },
  "elogios_recurentes": [],
  "criticas_recurentes": [],
  "sentimento_geral": "",
  "problemas_sistemicos": [],
  "oportunidades_melhoria": [],
  "respostas_necessarias": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Interpretador de Cenário
- Recebe de: Scan Digital Essencial

**Quando usar:**
- ✅ Nota abaixo de 4.0 no Google
- ✅ Queda repentina em avaliações
- ✅ Planejamento de melhoria de experiência

**Quando NÃO usar:**
- ❌ Negócio sem reviews suficientes (< 10)
- ❌ Se análise foi feita recentemente (< 30 dias)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: REPUTAÇÃO (apoio)
- Arquivo: `base_reputacao.json`

**Impacto no Negócio:** MÉDIO  
*Reputação online impacta diretamente decisão de compra.*

---

### SKILL 18: Pesquisador de Intenção de Busca

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** COLETA  

**Missão da Skill:**  
Mapear profundamente as intenções de busca do público para orientar estratégia de conteúdo e SEO.

**O que ela analisa:**
- Termos de busca relacionados ao nicho
- Intenção por trás de cada termo (informacional, comercial, transacional)
- Volume de busca estimado
- Dificuldade de rankeamento
- Conteúdo atual rankeando para cada termo

**Input Necessário:**
- Nicho definido
- Palavras-chave semente
- Público-alvo

**Processo Interno:**
1. Expandir palavras-chave semente em lista ampla
2. Classificar cada termo por intenção de busca
3. Estimar volume e dificuldade (ferramentas SEO)
4. Analisar SERP para termos prioritários
5. Identificar gaps de conteúdo
6. Priorizar termos por oportunidade

**Output Gerado:**
```json
{
  "intencoes_mapeadas": [
    {
      "termo": "",
      "intencao": "",
      "volume_estimado": 0,
      "dificuldade": "",
      "conteudo_ranking": [],
      "oportunidade": ""
    }
  ],
  "gaps_conteudo": [],
  "termos_prioritarios": [],
  "recomendacoes_conteudo_seo": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Planejador de Conteúdo Estratégico
- Recebe de: Triagem, Pesquisador de Público Profundo

**Quando usar:**
- ✅ Estratégia de conteúdo SEO-driven
- ✅ Criação de blog ou área de conteúdo
- ✅ Recuperação de tráfego orgânico

**Quando NÃO usar:**
- ❌ Negócio sem site ou sem plano de conteúdo
- ❌ Pesquisa de intenção já realizada recentemente

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: SEO E BUSCA
- Arquivo: `base_intencao_busca.json`

**Impacto no Negócio:** ALTO  
*Conteúdo alinhado à intenção de busca rankeia e converte.*

---

### SKILL 19: Segmentador de Personas

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** ORGANIZA  

**Missão da Skill:**  
Criar segmentos detalhados de personas baseados em dados reais de público.

**O que ela analisa:**
- Dados demográficos do público
- Comportamentos observados
- Dores e desejos por segmento
- Canais preferenciais por segmento
- Estágios de consciência diferentes

**Input Necessário:**
- Pesquisa de público profunda
- Dados de clientes existentes (se disponíveis)
- Analytics de site/redes sociais

**Processo Interno:**
1. Agrupar público por características comuns
2. Criar perfil detalhado para cada segmento
3. Mapear dores específicas por persona
4. Identificar canais preferenciais de cada uma
5. Definir messaging específico por persona
6. Priorizar personas por valor e acessibilidade

**Output Gerado:**
```json
{
  "personas": [
    {
      "nome": "",
      "perfil_demografico": {},
      "dores_principais": [],
      "desejos_principais": [],
      "canais_preferenciais": [],
      "estagio_consciencia": "",
      "mensagem_especifica": "",
      "prioridade": ""
    }
  ],
  "persona_primaria": "",
  "personas_secundarias": [],
  "recomendacoes_por_persona": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Estruturador de Mensagem
- Recebe de: Pesquisador de Público Profundo

**Quando usar:**
- ✅ Público heterogêneo com necessidades distintas
- ✅ Múltiplas ofertas para diferentes segmentos
- ✅ Refinamento de targeting em anúncios

**Quando NÃO usar:**
- ❌ Público extremamente homogêneo
- ❌ Negócio muito pequeno (foco em um segmento só)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PÚBLICO E MERCADO
- Arquivo: `base_personas.json`

**Impacto no Negócio:** MÉDIO  
*Personas bem definidas permitem comunicação mais precisa.*

---

### SKILL 20: Comparador de Diferenciação

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Analisar comparativamente o negócio vs. concorrência para identificar diferenciais reais e percebidos.

**O que ela analisa:**
- Atributos do negócio
- Atributos de cada concorrente
- Percepção do mercado (reviews, comentários)
- Espaço competitivo disponível
- Diferenciais sustentáveis vs. temporários

**Input Necessário:**
- Dados do negócio (Triagem, Validador de Oferta)
- Dados de concorrência (Minerador de Concorrência)
- Pesquisa de público

**Processo Interno:**
1. Listar atributos comparáveis entre players
2. Avaliar desempenho em cada atributo
3. Identificar onde o negócio é superior
4. Identificar onde o negócio é inferior
5. Detectar atributos não explorados pela concorrência
6. Classificar diferenciais por sustentabilidade

**Output Gerado:**
```json
{
  "matriz_comparativa": {},
  "diferenciais_reais": [],
  "diferenciais_percebidos": [],
  "pontos_inferioridade": [],
  "espacos_vazios": [],
  "diferenciais_sustentaveis": [],
  "recomendacoes_diferenciacao": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Definidor de Posicionamento
- Recebe de: Minerador de Concorrência, Validador de Oferta

**Quando usar:**
- ✅ Commoditização percebida no nicho
- ✅ Dificuldade em comunicar valor único
- ✅ Reposicionamento estratégico

**Quando NÃO usar:**
- ❌ Concorrência não mapeada adequadamente
- ❌ Diferenciação já clara e validada

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: POSICIONAMENTO
- Arquivo: `base_diferenciacao.json`

**Impacto no Negócio:** ALTO  
*Diferenciação clara é pré-requisito para pricing power e preferência.*

---

### SKILL 21: Detector de Gargalos de Conversão

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Identificar pontos específicos onde potenciais clientes abandonam o processo de compra.

**O que ela analisa:**
- Funil de vendas atual
- Taxas de conversão por etapa
- Pontos de atrito identificados
- Objeções não resolvidas
- Complexidade desnecessária

**Input Necessário:**
- Mapeamento de jornada do cliente
- Dados de analytics (se disponíveis)
- Relatos de equipe de vendas/atendimento

**Processo Interno:**
1. Mapear taxas de conversão por etapa do funil
2. Identificar quedas bruscas de conversão
3. Investigar causas prováveis de abandono
4. Classificar gargalos por impacto potencial
5. Propor hipóteses de teste para cada gargalo

**Output Gerado:**
```json
{
  "funil_atual": {
    "etapas": [
      {"nome": "", "taxa_conversao": 0, "volume": 0}
    ]
  },
  "gargalos_identificados": [
    {
      "etapa": "",
      "queda_percentual": 0,
      "causa_provavel": "",
      "impacto_estimado": "",
      "hipotese_teste": ""
    }
  ],
  "prioridade_otimizacao": [],
  "recomendacoes_testes": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Otimizador de Funil
- Recebe de: Mapeador de Jornada do Cliente

**Quando usar:**
- ✅ Tráfego bom mas conversão baixa
- ✅ Abandono alto em etapa específica
- ✅ Otimização de ROI de marketing

**Quando NÃO usar:**
- ❌ Volume insuficiente para análise estatística
- ❌ Funil não implementado ou não mensurado

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: OFERTA E CONVERSÃO
- Arquivo: `base_gargalos.json`

**Impacto no Negócio:** ALTO  
*Resolver gargalos aumenta receita sem aumentar custos de aquisição.*

---

### SKILL 22: Otimizador de Funil

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Propor otimizações específicas para cada etapa do funil baseadas em gargalos identificados.

**O que ela analisa:**
- Gargalos de conversão
- Melhores práticas do nicho
- Testes possíveis por etapa
- Recursos disponíveis para implementação

**Input Necessário:**
- Output do Detector de Gargalos de Conversão
- Recursos disponíveis (Triagem)
- Melhores práticas do nicho

**Processo Interno:**
1. Para cada gargalo, listar soluções possíveis
2. Classificar soluções por impacto x esforço
3. Desenhar testes A/B viáveis
4. Estimar uplift potencial de cada otimização
5. Priorizar otimizações por ROI esperado

**Output Gerado:**
```json
{
  "otimizacoes_propostas": [
    {
      "etapa_funil": "",
      "gargalo_enderecado": "",
      "solucao": "",
      "tipo_teste": "",
      "impacto_estimado": "",
      "esforco": "",
      "prioridade": ""
    }
  ],
  "roadmap_testes": [],
  "metricas_monitorar": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Gerador de Plano Simplificado, Planejador de Conteúdo
- Recebe de: Detector de Gargalos de Conversão

**Quando usar:**
- ✅ Após identificação de gargalos
- ✅ Planejamento de testes de conversão
- ✅ Otimização contínua de funil

**Quando NÃO usar:**
- ❌ Sem gargalos identificados claramente
- ❌ Sem recursos para implementar testes

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: OFERTA E CONVERSÃO
- Arquivo: `base_otimizacao_funil.json`

**Impacto no Negócio:** ALTO  
*Otimização sistemática de funil é alavanca poderosa de crescimento.*

---

### SKILL 23: Planejador de Conteúdo Estratégico

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** DECIDE  

**Missão da Skill:**  
Criar plano de conteúdo alinhado com posicionamento, SEO e jornada do cliente.

**O que ela analisa:**
- Posicionamento e messaging
- Intenções de busca mapeadas
- Jornada do cliente
- Tipos de conteúdo que funcionam no nicho
- Capacidade de produção disponível

**Input Necessário:**
- Output do Estruturador de Mensagem
- Output do Pesquisador de Intenção de Busca
- Output do Mapeador de Jornada do Cliente
- Recursos disponíveis (tempo/equipe)

**Processo Interno:**
1. Mapear tópicos por etapa da jornada
2. Conectar tópicos com intenções de busca
3. Definir formatos adequados por canal
4. Criar calendário editorial realista
5. Estabelecer pilares de conteúdo
6. Definir métricas de sucesso por tipo de conteúdo

**Output Gerado:**
```json
{
  "pilares_conteudo": [],
  "calendario_editorial": {
    "periodo": "30 dias",
    "posts_planejados": [
      {
        "data_sugerida": "",
        "topico": "",
        "formato": "",
        "canal": "",
        "etapa_jornada": "",
        "intencao_busca": "",
        "cta": ""
      }
    ]
  },
  "recomendacoes_producao": [],
  "metricas_sucesso": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Gerador de Plano Simplificado
- Recebe de: Estruturador de Mensagem, Pesquisador de Intenção de Busca

**Quando usar:**
- ✅ Planejamento mensal/trimestral de conteúdo
- ✅ Inconsistência na publicação
- ✅ Conteúdo desconectado da estratégia

**Quando NÃO usar:**
- ❌ Sem posicionamento claro definido
- ❌ Sem capacidade mínima de produção

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: INSTAGRAM E CONTEÚDO
- Módulo: SEO E BUSCA
- Arquivo: `base_conteudo_planejado.json`

**Impacto no Negócio:** ALTO  
*Conteúdo estratégico atrai, engaja e converte de forma previsível.*

---

### SKILL 24: Calibrador de Canais

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** DECIDE  

**Missão da Skill:**  
Definir alocação ideal de esforços e orçamento entre canais baseada em desempenho e potencial.

**O que ela analisa:**
- Canais atuais e desempenho
- Potencial de cada canal para o nicho
- Recursos disponíveis (tempo e orçamento)
- Objetivos comerciais
- Sinergias entre canais

**Input Necessário:**
- Scan Digital (canais ativos)
- Dados de desempenho por canal (se disponíveis)
- Objetivos comerciais
- Recursos disponíveis

**Processo Interno:**
1. Avaliar desempenho atual de cada canal
2. Estimar potencial não explorado
3. Classificar canais por ROI atual e potencial
4. Identificar sinergias e redundâncias
5. Propor alocação ideal de recursos
6. Recomendar canais para entrar ou sair

**Output Gerado:**
```json
{
  "canais_atuais": [
    {
      "nome": "",
      "desempenho_atual": "",
      "roi_estimado": "",
      "potencial": "",
      "recomendacao": ""
    }
  ],
  "alocacao_recomendada": {
    "tempo": {},
    "orcamento": {}
  },
  "canais_sugeridos_entrada": [],
  "canais_sugeridos_saida": [],
  "sinergias_explorar": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Gerador de Plano Simplificado
- Recebe de: Scan Digital, Triagem

**Quando usar:**
- ✅ Múltiplos canais ativos sem clareza de foco
- ✅ Orçamento limitado precisa de alocação inteligente
- ✅ Avaliação trimestral de performance de canais

**Quando NÃO usar:**
- ❌ Apenas um canal relevante para o negócio
- ❌ Sem dados mínimos de desempenho

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: CANAIS (apoio)
- Arquivo: `base_canais_estrategia.json`

**Impacto no Negócio:** MÉDIO  
*Alocação correta de recursos maximiza retorno de marketing.*

---

### SKILL 25: Monitor de Evolução de Mercado

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Acompanhar mudanças no mercado ao longo do tempo para ajustar estratégia continuamente.

**O que ela analisa:**
- Tendências previamente identificadas
- Movimentos de concorrentes
- Mudanças no comportamento do público
- Novas tecnologias ou plataformas
- Variações sazoniais do nicho

**Input Necessário:**
- Linha de base de mercado (análises anteriores)
- Dados de rastreamento contínuo
- Alertas e novidades do nicho

**Processo Interno:**
1. Comparar estado atual com linha de base
2. Identificar mudanças significativas
3. Classificar mudanças por impacto potencial
4. Detectar sinais fracos de transformação
5. Propor ajustes de estratégia

**Output Gerado:**
```json
{
  "mudancas_identificadas": [
    {
      "tipo": "",
      "descricao": "",
      "impacto_potencial": "",
      "urgencia_resposta": "",
      "acao_sugerida": ""
    }
  ],
  "sinais_fracos": [],
  "ajustes_estrategia_sugeridos": [],
  "alertas_atencao": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Interpretador de Cenário
- Recebe de: Rastreador de Tendências, Minerador de Concorrência

**Quando usar:**
- ✅ Revisão mensal ou trimestral de estratégia
- ✅ Mercados de rápida mudança
- ✅ Sinais de perda de competitividade

**Quando NÃO usar:**
- ❌ Primeira análise de mercado (sem linha de base)
- ❌ Nichos extremamente estáveis

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: MERCADO (apoio)
- Arquivo: `base_evolucao_mercado.json`

**Impacto no Negócio:** MÉDIO  
*Adaptação contínua mantém relevância e competitividade.*

---

### SKILL 26: Gerador de Roadmap Trimestral

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** EXECUTA  

**Missão da Skill:**  
Transformar prioridades em roadmap estratégico de 90 dias com marcos claros.

**O que ela analisa:**
- Prioridades definidas
- Objetivos de longo prazo
- Capacidade de execução
- Dependências entre iniciativas
- Marcos importantes do negócio

**Input Necessário:**
- Output do Priorizador de Ações
- Objetivos estratégicos (Triagem)
- Recursos disponíveis
- Calendário do negócio (lançamentos, sazonalidade)

**Processo Interno:**
1. Distribuir prioridades ao longo de 12 semanas
2. Identificar dependências e sequenciamento
3. Definir marcos de progresso (milestones)
4. Alocar recursos por semana/mês
5. Estabelecer checkpoints de revisão
6. Criar visão macro e micro do trimestre

**Output Gerado:**
```json
{
  "roadmap_trimestral": {
    "trimestre": "Q1 2026",
    "objetivos_trimestre": [],
    "semanas": [
      {
        "semana": 1,
        "foco": "",
        "acoes_previstas": [],
        "marcos": []
      }
    ],
    "milestones": [
      {"data": "", "marco": "", "metrica_sucesso": ""}
    ],
    "checkpoints_revisao": []
  },
  "recursos_alocados": {},
  "riscos_identificados": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Execução e acompanhamento
- Recebe de: Priorizador de Ações, Triagem

**Quando usar:**
- ✅ Planejamento trimestral
- ✅ Necessidade de visibilidade de longo prazo
- ✅ Coordenação de múltiplas iniciativas

**Quando NÃO usar:**
- ❌ Sem prioridades claras definidas
- ❌ Ambiente de extrema incerteza (planejar ciclos curtos)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PLANO DE AÇÃO
- Arquivo: `base_roadmap.json`

**Impacto no Negócio:** ALTO  
*Roadmap claro transforma estratégia em execução consistente.*

---

### SKILL 27: Auditor de Coerência Geral

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** INTERPRETA  

**Missão da Skill:**  
Avaliar a coerência geral entre todos os elementos do negócio (posicionamento, oferta, conteúdo, canais).

**O que ela analisa:**
- Posicionamento declarado
- Mensaging em uso
- Conteúdo produzido
- Experiência em cada canal
- Oferta e precificação
- Atendimento e pós-venda

**Input Necessário:**
- Todos os módulos da base de conhecimento
- Amostras de conteúdo e comunicação
- Experiência completa do cliente (se possível)

**Processo Interno:**
1. Mapear promessa em cada ponto de contato
2. Comparar promessa vs. entrega real
3. Identificar inconsistências de mensagem
4. Detectar gaps entre posicionamento e experiência
5. Classificar incoerências por gravidade
6. Propor alinhamentos necessários

**Output Gerado:**
```json
{
  "indice_coerencia_geral": 0,
  "incoerencias_identificadas": [
    {
      "area": "",
      "promessa": "",
      "realidade": "",
      "gravidade": "",
      "correcao_sugerida": ""
    }
  ],
  "pontos_alinhamento_exemplar": [],
  "prioridades_alinhamento": [],
  "recomendacoes_gerais": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Organizador de Base, Interpretador de Cenário
- Recebe de: TODOS OS MÓDULOS DA BASE

**Quando usar:**
- ✅ Revisão estratégica trimestral ou anual
- ✅ Sensação de "algo não está certo"
- ✅ Antes de grandes investimentos em marketing

**Quando NÃO usar:**
- ❌ Base de conhecimento incompleta
- ❌ Negócio em fase muito inicial (< 3 meses)

**Qual base, arquivo ou módulo ela alimenta:**
- TODOS OS MÓDULOS (auditoria transversal)
- Arquivo: `base_coerencia.json`

**Impacto no Negócio:** ALTO  
*Coerência constrói confiança e acelera decisão de compra.*

---

### SKILL 28: Estrategista de Engenharia Social Profunda

**Nível de Prioridade:** OPCIONAL  
**Tipo de Função:** DECIDE/EXECUTA  

**Missão da Skill:**  
Orquestrar campanhas coordenadas de influência, prova social construída e manipulação ética de comportamento em escala, aplicando princípios avançados de engenharia social para acelerar autoridade e conversão.

**O que ela analisa:**
- Base completa de engenharia social básica (Skill 06)
- Histórico de interações e respostas do público
- Padrões de comportamento em massa observáveis
- Redes de influência do nicho
- Timing e contexto cultural
- Elementos de prova social disponíveis e faltantes

**Input Necessário:**
- Output do Analista de Engenharia Social Básica
- Output do Pesquisador de Público Profundo
- Output do Minerador de Concorrência
- Output do Monitor de Evolução de Mercado
- Dados de performance de conteúdos anteriores

**Processo Interno:**
1. Mapear rede de influenciadores e formadores de opinião do nicho
2. Identificar oportunidades de prova social orquestrada (depoimentos, cases, endorsements)
3. Desenhar sequência de gatilhos mentais ao longo do tempo (campanha coordenada)
4. Aplicar modelo Fogg (Motivação x Habilidade x Trigger) para comportamentos-alvo
5. Criar estratégia de autoridade construída (parcerias, appearances, associações)
6. Planejar escassez e urgência éticas com timing preciso
7. Desenhar loops de reciprocidade (conteúdo gratuito → valor percebido → conversão)
8. Estabelecer sistema de validação social em cascata
9. Definir métricas de sucesso para cada elemento de influência

**Output Gerado:**
```json
{
  "estrategia_engenharia_social": {
    "campanha_coordenada": {
      "objetivo_comportamental": "",
      "sequencia_gatilhos": [],
      "timeline": "",
      "canais_prioritarios": []
    },
    "prova_social_orquestrada": {
      "depoimentos_planejados": [],
      "cases_a_produzir": [],
      "endorsements_possiveis": [],
      "metricas_validacao": []
    },
    "autoridade_construida": {
      "parcerias_estrategicas": [],
      "appearances_sugeridas": [],
      "associacoes_relevantes": [],
      "credenciais_a_destacar": []
    },
    "escassez_urgencia": {
      "oportunidades_legitimas": [],
      "timing_aplicacao": [],
      "limites_reais": []
    },
    "loops_reciprocidade": {
      "conteudo_gratuito": [],
      "valor_entregue": "",
      "call_to_action_reciproco": ""
    },
    "validacao_social_cascata": {
      "primeiros_adotantes": [],
      "multiplicadores": [],
      "prova_massa_critica": ""
    }
  },
  "metricas_sucesso": {},
  "riscos_eticos_alertas": [],
  "plano_execucao_90_dias": []
}
```

**Como ela se conecta com as outras:**
- Alimenta: Planejador de Conteúdo Estratégico, Gerador de Roadmap Trimestral
- Recebe de: Analista de Engenharia Social Básica, Pesquisador de Público, Monitor de Mercado

**Quando usar:**
- ✅ Negócios estabelecidos buscando escala rápida
- ✅ Lançamentos de produtos/serviços de alto ticket
- ✅ Reposicionamento de marca necessário
- ✅ Competição acirrada onde diferenciação é crítica

**Quando NÃO usar:**
- ❌ Negócios em fase inicial (< 6 meses de operação)
- ❌ Quando não há produto/serviço validado
- ❌ Se a equipe não consegue executar com consistência
- ❌ Em contextos onde manipulação antiética seria necessária (foco em influência ética)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PÚBLICO E MERCADO (subseção: Engenharia Social Avançada)
- Módulo: POSICIONAMENTO (subseção: Autoridade e Prova Social)
- Módulo: PLANO DE AÇÃO (subseção: Campanhas Coordenadas)
- Arquivo: `base_engenharia_social_profunda.json`

**Impacto no Negócio:** ALTO  
*Engenharia social bem executada pode acelerar construção de autoridade em 6-12 meses para 6-12 semanas, com aumento exponencial de conversão.*

---

### SKILL 29: Auditor de Risco Reputacional

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** INTERPRETA/DECIDE  

**Missão da Skill:**  
Analisar estratégias, mensagens e ações planejadas quanto ao risco de dano reputacional, cancelamento, polêmicas desnecessárias, conformidade legal e sensibilidade cultural ANTES da execução, atuando como um "freio de segurança" estratégico.

**O que ela analisa:**
- Mensagens e headlines planejadas
- Campanhas de marketing propostas
- Posicionamentos públicos da marca
- Respostas a críticas ou crises
- Conformidade com regulamentações do nicho (saúde, direito, finanças, etc.)
- Sensibilidade cultural e contextual
- Histórico de polêmicas do nicho
- Tom de voz e linguagem utilizada

**Input Necessário:**
- Output do Estruturador de Mensagem + Engenharia Social Aplicada
- Output do Planejador de Conteúdo Estratégico
- Output do Estrategista de Engenharia Social Profunda
- Regulamentações específicas do nicho (se aplicável)
- Base de casos de cancelamento do setor

**Processo Interno:**
1. Escanear todas as mensagens e campanhas planejadas
2. Identificar palavras/frases de alto risco (polêmicas, sensíveis, ambíguas)
3. Avaliar conformidade legal (ANVISA, CFP, CVM, PROCON, etc.)
4. Analisar sensibilidade cultural (gênero, raça, religião, orientação, etc.)
5. Verificar histórico de polêmicas similares no nicho
6. Classificar risco em níveis: BAIXO, MÉDIO, ALTO, CRÍTICO
7. Sugerir alternativas de mensagem com menor risco
8. Criar plano de contingência para cenários de crise
9. Definir gatilhos de alerta para monitoramento pós-execução

**Output Gerado:**
```json
{
  "auditoria_risco_reputacional": {
    "nivel_risco_geral": "BAIXO|MÉDIO|ALTO|CRÍTICO",
    "mensagens_analisadas": [],
    "riscos_identificados": [
      {
        "tipo": "legal|cultural|etico|polemico",
        "descricao": "",
        "gravidade": "baixa|media|alta|critica",
        "probabilidade_ocorrencia": "baixa|media|alta",
        "mensagem_problema": "",
        "alternativa_sugerida": "",
        "plano_mitigacao": ""
      }
    ],
    "conformidade_legal": {
      "regulamentacoes_aplicaveis": [],
      "pontos_atencao": [],
      "recomendacoes_juridicas": []
    },
    "sensibilidade_cultural": {
      "pontos_verificados": [],
      "alertas": [],
      "recomendacoes_inclusivas": []
    },
    "plano_contingencia": {
      "cenario_critico": "",
      "acoes_imediatas": [],
      "porta_voz_designado": "",
      "timeline_resposta": ""
    },
    "gatilhos_monitoramento": [],
    "parecer_final": "APROVADO | APROVADO COM RESSALVAS | REPROVADO"
  }
}
```

**Como ela se conecta com as outras:**
- Alimenta: Tradutor Operacional de Estratégia, Gerador de Plano de Ação
- Recebe de: Todas as skills de decisão e execução (mensagem, conteúdo, engenharia social)

**Quando usar:**
- ✅ SEMPRE antes de executar qualquer campanha de grande escala
- ✅ Antes de lançamentos de produtos/serviços
- ✅ Em respostas a crises ou críticas públicas
- ✅ Em nichos altamente regulamentados (saúde, direito, finanças)
- ✅ Quando o negócio tem visibilidade pública significativa

**Quando NÃO usar:**
- ❌ Nunca deixar de usar em contextos de alto risco
- ⚠️ Pode ser simplificado em negócios muito pequenos e locais sem visibilidade

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: POSICIONAMENTO (subseção: Gestão de Risco Reputacional)
- Módulo: PLANO DE AÇÃO (subseção: Contingências e Crises)
- Arquivo: `auditoria_risco_reputacional.json`
- Arquivo: `plano_contingencia_crise.json`

**Impacto no Negócio:** CRÍTICO  
*Um único erro reputacional pode destruir anos de construção de marca em horas. Esta skill é o seguro estratégico do negócio.*

---

### SKILL 30: Tradutor Operacional de Estratégia

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** DECIDE/EXECUTA  

**Missão da Skill:**  
Converter estratégias abstratas e planos conceituais em tarefas operacionais claras, acionáveis e delegáveis, com prazos realistas, responsáveis definidos e critérios de sucesso mensuráveis. É a ponte entre "o que fazer" e "como fazer".

**O que ela analisa:**
- Planos estratégicos gerados pelas skills de decisão
- Recursos disponíveis (equipe, tempo, orçamento, ferramentas)
- Capacidade operacional atual do negócio
- Complexidade de cada tarefa proposta
- Dependências entre tarefas
- Prioridades conflitantes

**Input Necessário:**
- Output do Gerador de Plano de Ação Simplificado
- Output do Planejador de Conteúdo Estratégico
- Output do Gerador de Roadmap Trimestral
- Output do Auditor de Risco Reputacional
- Inventário de recursos (equipe, tempo, orçamento)
- Ferramentas disponíveis (software, plataformas, etc.)

**Processo Interno:**
1. Desmontar estratégias em componentes atômicos
2. Transformar cada componente em tarefa executável
3. Definir critério de "pronto" claro para cada tarefa
4. Estimar tempo realista de execução (com margem de erro)
5. Identificar dependências e sequência lógica
6. Atribuir responsabilidades (ou perfis necessários)
7. Priorizar por impacto x esforço (matriz Eisenhower)
8. Criar checklist executivo para cada frente
9. Definir métricas de acompanhamento semanal
10. Estabelecer rituais de revisão e ajuste

**Output Gerado:**
```json
{
  "traducao_operacional": {
    "checklist_executivo": [
      {
        "frente_estrategica": "",
        "tarefas": [
          {
            "id": "",
            "descricao_acao": "",
            "criterio_pronto": "",
            "tempo_estimado_horas": 0,
            "prazo_limite": "",
            "responsavel_sugerido": "",
            "perfil_necessario": "",
            "dependencias": [],
            "prioridade": "P1|P2|P3",
            "impacto_esperado": "alto|medio|baixo",
            "esforco": "alto|medio|baixo",
            "ferramentas_necessarias": [],
            "metrica_sucesso": "",
            "status": "pendente|em_progresso|concluida"
          }
        ]
      }
    ],
    "cronograma_semanal": {
      "semana_1": [],
      "semana_2": [],
      "semana_3": [],
      "semana_4": []
    },
    "matriz_priorizacao": {
      "fazer_agora": [],
      "agendar": [],
      "delegar": [],
      "eliminar": []
    },
    "recursos_necessarios": {
      "humanos": [],
      "financeiros": 0,
      "ferramentas": [],
      "tempo_total_semanal_horas": 0
    },
    "rituais_gestao": {
      "revisao_semanal": "dia_da_semana",
      "metricas_acompanhamento": [],
      "gatilhos_ajuste": []
    }
  }
}
```

**Como ela se conecta com as outras:**
- Alimenta: Execução direta pela equipe, Orquestrador de Inteligência Contínua
- Recebe de: Todas as skills de decisão (Plano de Ação, Roadmap, Conteúdo, etc.)

**Quando usar:**
- ✅ SEMPRE que uma estratégia for aprovada e precisar sair do papel
- ✅ Na transição entre planejamento e execução
- ✅ Quando há equipe envolvida na implementação
- ✅ Para evitar que estratégias morram na gaveta

**Quando NÃO usar:**
- ❌ Nunca pular esta etapa se houver equipe envolvida
- ⚠️ Pode ser simplificado para profissionais solo, mas ainda é essencial

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PLANO DE AÇÃO (subseção: Checklist Operacional)
- Módulo: PRIORIDADES (subseção: Matriz de Execução)
- Arquivo: `checklist_executivo.json`
- Arquivo: `cronograma_operacional.json`
- Arquivo: `matriz_priorizacao.json`

**Impacto no Negócio:** CRÍTICO  
*Estratégias sem tradução operacional são apenas sonhos. Esta skill transforma visão em realidade executável.*

---

### SKILL 31: Detector de Estagnação & Pivotagem

**Nível de Prioridade:** IMPORTANTE  
**Tipo de Função:** INTERPRETA/DECIDE  

**Missão da Skill:**  
Monitorar sinais de estagnação, saturação de estratégia, queda de performance e ineficiência crescente, identificando o momento exato para pivotar (mudar direção radicalmente) em vez de apenas otimizar. Atua como um "sistema de alerta precoce" contra a irrelevância.

**O que ela analisa:**
- Métricas de performance ao longo do tempo (tendências, não pontos isolados)
- Taxa de engajamento e conversão em declínio
- Saturação de audiência (mesmo público, mesmas mensagens)
- Mudanças no comportamento do mercado
- Emergência de novos concorrentes ou modelos
- Fadiga de conteúdo (queda orgânica consistente)
- Custo de aquisição crescente com retorno decrescente
- Feedback qualitativo do público (tédio, desinteresse)

**Input Necessário:**
- Histórico de métricas (mínimo 3-6 meses)
- Output do Monitor de Evolução de Mercado
- Output do Otimizador de Funil
- Output do Pesquisador de Intenção de Busca
- Feedback direto do público (comentários, DMs, pesquisas)
- Dados de concorrência emergente

**Processo Interno:**
1. Analisar tendências de métricas-chave (não valores absolutos)
2. Identificar padrões de declínio consistente (3+ períodos consecutivos)
3. Detectar sinais de saturação de audiência/mensagem
4. Comparar performance com benchmarks do nicho
5. Avaliar custo de oportunidade de continuar vs. pivotar
6. Identificar direções alternativas viáveis (novos públicos, ofertas, canais)
7. Calcular "ponto de inflexão" recomendado
8. Gerar cenário de "continuar otimizando" vs "pivotar radicalmente"
9. Criar plano de transição se pivotagem for recomendada
10. Definir métricas de alerta para monitoramento contínuo

**Output Gerado:**
```json
{
  "detector_estagnacao_pivotagem": {
    "status_geral": "SAUDAVEL | ATENCAO | ALERTA | CRITICO",
    "sinais_estagnacao": [
      {
        "tipo": "engagement_decline|conversion_drop|saturation|market_shift|content_fatigue",
        "descricao": "",
        "gravidade": "baixa|media|alta",
        "periodo_detectado": "",
        "tendencia": "piorando|estavel|melhorando"
      }
    ],
    "metricas_alerta": {
      "engajamento_queda_percentual": 0,
      "conversao_queda_percentual": 0,
      "custo_aquisicao_alta_percentual": 0,
      "saturacao_audiencia_percentual": 0
    },
    "recomendacao": "CONTINUAR_OTIMIZANDO | PREPARAR_PIVOT | PIVOTAR_AGORA",
    "direcoes_pivotagem": [
      {
        "tipo": "novo_publico|nova_oferta|novo_canal|reposicionamento",
        "descricao": "",
        "viabilidade": "baixa|media|alta",
        "esforco_estimado": "baixo|medio|alto",
        "impacto_potencial": "baixo|medio|alto",
        "timeline_recomendada": ""
      }
    ],
    "plano_transicao": {
      "acoes_imediatas": [],
      "acoes_30_dias": [],
      "acoes_60_dias": [],
      "metricas_sucesso_transicao": []
    },
    "cenario_nao_acao": {
      "projecao_6_meses": "",
      "riscos": []
    }
  }
}
```

**Como ela se conecta com as outras:**
- Alimenta: Orquestrador de Inteligência Contínua, Gerador de Roadmap Trimestral
- Recebe de: Monitor de Evolução de Mercado, Otimizador de Funil, Todas as skills de métrica

**Quando usar:**
- ✅ Quando métricas mostram declínio consistente por 3+ meses
- ✅ Antes de investir pesado em otimizações incrementais
- ✅ Em revisões trimestrais de estratégia
- ✅ Quando há sensação de "teto" ou estagnação
- ✅ Ao identificar novos concorrentes disruptivos

**Quando NÃO usar:**
- ❌ Em negócios com menos de 6 meses de operação (ainda é cedo)
- ❌ Para quedas sazonais esperadas e temporárias
- ❌ Quando a queda é causada por fatores externos pontuais (ex: crise global)

**Qual base, arquivo ou módulo ela alimenta:**
- Módulo: PRIORIDADES (subseção: Alertas de Estagnação)
- Módulo: PLANO DE AÇÃO (subseção: Planos de Pivotagem)
- Módulo: EVOLUÇÃO DE MERCADO (subseção: Tendências de Longo Prazo)
- Arquivo: `detector_estagnacao.json`
- Arquivo: `plano_pivotagem.json`

**Impacto no Negócio:** ALTO  
*Identificar o momento de pivotar pode salvar um negócio da irrelevância. Continuar otimizando uma estratégia morta é desperdício de recursos.*

---

### SKILL 32: Orquestrador de Inteligência Contínua

**Nível de Prioridade:** NUCLEAR  
**Tipo de Função:** ORGANIZA/DECIDE  

**Missão da Skill:**  
Coordenar o ciclo automático de coleta-interpretação-decisão-ação, garantindo que o sistema se auto-alimente, atualize a base de conhecimento, dispare reavaliações periódicas e mantenha a inteligência sempre fresca e acionável. É o "cérebro" que orquestra todo o ecossistema.

**O que ela analisa:**
- Estado atual de todos os módulos da base
- Gatilhos de reavaliação (tempo, performance, mercado)
- Outputs de todas as skills executadas
- Lacunas de informação na base
- Prioridades conflitantes entre diferentes frentes
- Necessidade de novas rodadas de análise

**Input Necessário:**
- Outputs de TODAS as skills executadas anteriormente
- Base de conhecimento consolidada
- Calendário de revisões periódicas
- Gatilhos de evento (lançamentos, crises, mudanças de mercado)

**Processo Interno:**
1. Consolidar outputs de todas as skills em visão unificada
2. Atualizar base de conhecimento com novas informações
3. Identificar lacunas ou inconsistências nos dados
4. Disparar gatilhos para re-execução de skills específicas quando necessário
5. Priorizar próximas ações com base em impacto x urgência
6. Agendar revisões periódicas (semanal, mensal, trimestral)
7. Manter histórico de evolução das decisões e resultados
8. Gerar resumo executivo do estado atual do negócio
9. Sinalizar necessidade de intervenção humana em pontos críticos

**Output Gerado:**
```json
{
  "orquestracao_inteligencia_continua": {
    "estado_atual_sistema": {
      "ultima_atualizacao": "",
      "modulos_atualizados": [],
      "lacunas_identificadas": [],
      "confiabilidade_dados": "baixa|media|alta"
    },
    "ciclo_proximo": {
      "skills_a_executar": [],
      "gatilho_disparo": "tempo|performance|evento",
      "data_prevista": "",
      "prioridade": "baixa|media|alta"
    },
    "resumo_executivo": {
      "status_geral_negocio": "",
      "principais_oportunidades": [],
      "principais_riscos": [],
      "proximas_acoes_criticas": []
    },
    "historico_decisoes": [
      {
        "data": "",
        "decisao": "",
        "base_skill": "",
        "resultado_esperado": "",
        "resultado_real": "",
        "aprendizado": ""
      }
    ],
    "gatilhos_alerta": [
      {
        "condicao": "",
        "skill_relacionada": "",
        "acao_disparada": ""
      }
    ],
    "agenda_revisoes": {
      "semanal": {
        "dia": "",
        "foco": []
      },
      "mensal": {
        "dia": "",
        "foco": []
      },
      "trimestral": {
        "semana": "",
        "foco": []
      }
    }
  }
}
```

**Como ela se conecta com as outras:**
- **Conecta-se com TODAS as skills** (é o hub central)
- Recebe outputs de todas as skills
- Dispara re-execução de skills específicas quando necessário
- Mantém a base de conhecimento atualizada

**Quando usar:**
- ✅ CONTINUAMENTE - é uma skill de execução permanente
- ✅ Após cada rodada de análise estratégica
- ✅ Em revisões periódicas (semanal, mensal, trimestral)
- ✅ Quando há mudanças significativas no negócio ou mercado

**Quando NÃO usar:**
- ❌ Nunca desativar em negócios que buscam inteligência contínua
- ⚠️ Pode ser simplificado para operações muito pequenas, mas ainda é essencial

**Qual base, arquivo ou módulo ela alimenta:**
- **TODOS OS MÓDULOS DA BASE** (é o principal alimentador)
- Arquivo: `orquestracao_estado.json`
- Arquivo: `historico_decisoes.json`
- Arquivo: `agenda_revisoes.json`
- Arquivo: `base_conhecimento_consolidada.json`

**Impacto no Negócio:** CRÍTICO  
*Sem orquestração contínua, a inteligência fica obsoleta em semanas. Esta skill garante que o sistema viva e evolua com o negócio.*

---

# 7. ESTRUTURA DA BASE DE INFORMAÇÕES

Estes módulos devem existir em QUALQUER configuração do sistema:

### Módulo 1: SOBRE O NEGÓCIO
**Finalidade:** Contexto fundamental do negócio  
**Dados armazenados:**
- Tipo de negócio
- Nicho e segmento
- Oferta principal e secundárias
- Maturidade atual
- Recursos disponíveis
- Objetivos comerciais

**Alimentado por:** Triagem Rápida de Negócio  
**Usado por:** Todas as skills

---

### Módulo 2: PÚBLICO E MERCADO
**Finalidade:** Entendimento profundo de quem compra e do contexto  
**Dados armazenados:**
- Perfil demográfico
- Dores principais
- Desejos e aspirações
- Objeções comuns
- Linguagem usada
- Estágios de consciência
- Personas (se aplicável)

**Alimentado por:** Pesquisador de Público Profundo, Segmentador de Personas  
**Usado por:** Estruturador de Mensagem, Validador de Oferta, Planejador de Conteúdo

---

### Módulo 3: OFERTA E CONVERSÃO
**Finalidade:** Clareza sobre o que é vendido e como se vende  
**Dados armazenados:**
- Descrição da oferta
- Proposta de valor
- Preço e estrutura
- Processo de vendas
- Jornada do cliente
- Gargalos de conversão
- Taxas por etapa

**Alimentado por:** Validador de Oferta, Mapeador de Jornada, Detector de Gargalos  
**Usado por:** Definidor de Posicionamento, Otimizador de Funil

---

### Módulo 4: POSICIONAMENTO
**Finalidade:** Diferenciação clara no mercado  
**Dados armazenados:**
- Promessa central
- Diferencial principal
- Statement de posicionamento
- Tom de voz
- Messaging principal
- Matriz de diferenciação
- Palavras-chave de posicionamento

**Alimentado por:** Definidor de Posicionamento, Estruturador de Mensagem, Comparador de Diferenciação  
**Usado por:** Todas as skills de execução

---

### Módulo 5: INSTAGRAM E CONTEÚDO
**Finalidade:** Estratégia e execução de conteúdo  
**Dados armazenados:**
- Status atual do Instagram
- Análise de conteúdo existente
- Padrões de engajamento
- Pilares de conteúdo
- Calendário editorial
- Métricas de desempenho

**Alimentado por:** Scan Digital, Avaliador de Conteúdo Instagram, Planejador de Conteúdo  
**Usado por:** Gerador de Plano de Ação

---

### Módulo 6: SEO E BUSCA
**Finalidade:** Visibilidade orgânica no Google  
**Dados armazenados:**
- Status técnico do site
- Palavras-chave alvo
- Intenções de busca mapeadas
- Conteúdo existente
- Gaps de conteúdo
- Performance orgânica

**Alimentado por:** Analisador de SEO Básico, Pesquisador de Intenção de Busca  
**Usado por:** Planejador de Conteúdo Estratégico

---

### Módulo 7: CONCORRÊNCIA
**Finalidade:** Inteligência competitiva  
**Dados armazenados:**
- Lista de concorrentes
- Oferta e preço de cada um
- Posicionamento observado
- Canais ativos
- Pontos fortes e fracos
- Padrões do nicho

**Alimentado por:** Minerador de Concorrência  
**Usado por:** Comparador de Diferenciação, Definidor de Posicionamento

---

### Módulo 8: OPORTUNIDADES
**Finalidade:** Caminhos de crescimento identificados  
**Dados armazenados:**
- Lista de oportunidades
- Classificação impacto x esforço
- Quick wins
- Oportunidades de diferenciação
- Brechas não exploradas

**Alimentado por:** Minerador de Oportunidades  
**Usado por:** Priorizador de Ações

---

### Módulo 9: PRIORIDADES
**Finalidade:** Foco claro do que executar  
**Dados armazenados:**
- Top 5-7 prioridades do ciclo
- Ordem de execução
- Dependências
- O que ignorar agora
- O que manter como está

**Alimentado por:** Priorizador de Ações  
**Usado por:** Gerador de Plano de Ação

---

### Módulo 10: PLANO DE AÇÃO
**Finalidade:** Execução concreta  
**Dados armazenados:**
- Ações detalhadas por prioridade
- Passos executáveis
- Responsáveis
- Prazos
- Métricas de sucesso
- Checkpoints

**Alimentado por:** Gerador de Plano Simplificado, Gerador de Roadmap Trimestral  
**Usado por:** Execução (humana ou automatizada)

---

## 7.2 Módulos de Apoio (Stack Profissional e Avançada)

### Módulo 11: REPUTAÇÃO
**Finalidade:** Monitoramento de percepção pública  
**Dados armazenados:** Reviews, notas, sentimentos, problemas sistêmicos  
**Alimentado por:** Analisador de Reviews e Reputação

---

### Módulo 12: TENDÊNCIAS
**Finalidade:** Antecipação de movimentos de mercado  
**Dados armazenados:** Tendências emergentes, assuntos em alta, novos players  
**Alimentado por:** Rastreador de Tendências de Nicho

---

### Módulo 13: EVOLUÇÃO DE MERCADO
**Finalidade:** Acompanhamento contínuo de mudanças  
**Dados armazenados:** Mudanças identificadas, sinais fracos, ajustes sugeridos  
**Alimentado por:** Monitor de Evolução de Mercado

---

### Módulo 14: CANAIS (ESTRATÉGIA)
**Finalidade:** Alocação inteligente de recursos  
**Dados armazenados:** Desempenho por canal, alocação recomendada, sinergias  
**Alimentado por:** Calibrador de Canais

---

### Módulo 15: COERÊNCIA
**Finalidade:** Auditoria transversal de alinhamento  
**Dados armazenados:** Índice de coerência, incoerências identificadas, prioridades de alinhamento  
**Alimentado por:** Auditor de Coerência Geral

---

## 7.3 Como Evitar Duplicidade

**Regra 1: Um dado, uma fonte**  
Cada tipo de dado tem uma skill responsável primária por coletá-lo. Outras skills apenas consomem, não duplicam a coleta.

**Regra 2: Módulos mutuamente exclusivos**  
Cada módulo tem escopo claro. Se um dado poderia ficar em dois módulos, define-se regra de alocação:
- Dados sobre "quem compra" → PÚBLICO
- Dados sobre "o que vendemos" → OFERTA
- Dados sobre "como nos diferenciamos" → POSICIONAMENTO

**Regra 3: IDs únicos para registros**  
Cada registro na base tem ID único. Skills que atualizam dados usam o mesmo ID, não criam novos registros.

**Regra 4: Versionamento de atualizações**  
Quando um dado é atualizado, mantém-se histórico com timestamp. Isso permite auditoria e rollback se necessário.

---

## 7.4 Como Manter a Base Leve e Útil

**Princípio 1: Só armazena o que vira decisão**  
Se um dado coletado não influencia nenhuma decisão estratégica, não deve ser armazenado.

**Princípio 2: Resumo executivo em cada módulo**  
Cada módulo começa com um resumo de 3-5 bullets com o essencial. Detalhes ficam em subcampos.

**Princípio 3: Data de validade implícita**  
Dados têm "meia-vida". Pesquisa de público > 90 dias deve ser refrescada. Scan digital > 30 dias deve ser revalidado.

**Princípio 4: Formato máquina + humano**  
Base é estruturada (JSON) para processamento automático, mas inclui campos de "resumo humano" para leitura rápida.

**Princípio 5: Indexação por prioridade**  
Campos são marcados como: CRÍTICO, IMPORTANTE, COMPLEMENTAR. Leitura rápida foca apenas em CRÍTICO.

---

## 7.5 Como Garantir que a Base Vire Decisão

**Mecanismo 1: Campo "Decisões Habilitadas" em cada módulo**  
Cada módulo deve responder explicitamente: "Que decisões este dado habilita?"

**Mecanismo 2: Gatilhos de ação**  
Quando certos thresholds são atingidos (ex: nota de reputação < 4.0), gatilhos automáticos sugerem ações.

**Mecanismo 3: Link explícito para Plano de Ação**  
Cada insight na base deve ter campo opcional: "Ação derivada" → link para item no Módulo PLANO DE AÇÃO.

**Mecanismo 4: Revisão obrigatória em checkpoints**  
Em datas pré-definidas (semanal/quinzenal), a base deve ser revisitada para extrair novas decisões.

**Mecanismo 5: Score de "acionabilidade"**  
Cada registro recebe score 0-10 de quão acionável é. Registros com score < 3 são candidatos a arquivamento.

---

# 8. FLUXO IDEAL ENTRE AS SKILLS

## 8.1 Fluxo Completo (Stack Avançada)

```
┌──────────────────────────────────────────────────────────────────┐
│                        FASE 1: COLETA                            │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────┐                                            │
│  │ 01. Triagem     │────────────────────────┐                   │
│  │     Rápida      │                        │                   │
│  └────────┬────────┘                        │                   │
│           │                                 ▼                   │
│           │                          ┌─────────────────┐        │
│           ├─────────────────────────►│ 02. Scan Digital│        │
│           │                          │     Essencial   │        │
│           │                          └────────┬────────┘        │
│           │                                   │                 │
│           │                          ┌────────▼────────┐        │
│           │                          │ 09. Pesquisador │        │
│           │                          │     Público     │        │
│           │                          │    Profundo     │        │
│           │                          └────────┬────────┘        │
│           │                                   │                 │
│           │                          ┌────────▼────────┐        │
│           │                          │ 10. Minerador   │        │
│           │                          │  Concorrência   │        │
│           │                          └────────┬────────┘        │
│           │                                   │                 │
│           │                          ┌────────▼────────┐        │
│           │                          │ 11. Analisador  │        │
│           │                          │    SEO Básico   │        │
│           │                          └────────┬────────┘        │
│           │                                   │                 │
│           │                          ┌────────▼────────┐        │
│           │                          │ 16. Rastreador  │        │
│           │                          │   Tendências    │        │
│           │                          └────────┬────────┘        │
│           │                                   │                 │
│           │                          ┌────────▼────────┐        │
│           │                          │ 17. Analisador  │        │
│           │                          │    Reviews      │        │
│           │                          └────────┬────────┘        │
│           │                                   │                 │
│           │                          ┌────────▼────────┐        │
│           │                          │ 18. Pesquisador │        │
│           │                          │  Intenção Busca │        │
│           │                          └────────┬────────┘        │
│           │                                   │                 │
│           ▼                                   │                 │
│  ┌─────────────────┐                          │                 │
│  │ 03. Organizador │◄─────────────────────────┘                 │
│  │   de Base       │                                            │
│  │     Mínima      │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
└───────────┼──────────────────────────────────────────────────────┘
            │
┌───────────▼──────────────────────────────────────────────────────┐
│                      FASE 2: INTERPRETAÇÃO                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────┐                                            │
│  │ 04. Interpret.  │                                            │
│  │    Cenário      │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│  ┌────────▼────────┐                                            │
│  │ 05. Minerador   │                                            │
│  │  Oportunidades  │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│  ┌────────▼────────┐     ┌─────────────────┐                    │
│  │ 12. Avaliador   │     │ 13. Mapeador    │                    │
│  │  Conteúdo IG    │     │   Jornada       │                    │
│  └────────┬────────┘     │   Cliente       │                    │
│           │              └────────┬────────┘                    │
│           │                       │                              │
│  ┌────────▼────────┐     ┌────────▼────────┐                    │
│  │ 14. Validador   │     │ 21. Detector    │                    │
│  │     Oferta      │     │  Gargalos       │                    │
│  └────────┬────────┘     └────────┬────────┘                    │
│           │                       │                              │
│  ┌────────▼────────┐     ┌────────▼────────┐                    │
│  │ 20. Comparador  │     │ 22. Otimizador  │                    │
│  │ Diferenciação   │     │     Funil       │                    │
│  └────────┬────────┘     └────────┬────────┘                    │
│           │                       │                              │
│  ┌────────▼────────┐     ┌────────▼────────┐                    │
│  │ 25. Monitor     │     │ 27. Auditor     │                    │
│  │ Evolução Mercado│     │  Coerência      │                    │
│  └─────────────────┘     └─────────────────┘                    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
            │
┌───────────▼──────────────────────────────────────────────────────┐
│                        FASE 3: DECISÃO                           │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────┐                                            │
│  │ 06. Definidor   │                                            │
│  │ Posicionamento  │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│  ┌────────▼────────┐                                            │
│  │ 15. Estruturador│                                            │
│  │    Mensagem     │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│  ┌────────▼────────┐                                            │
│  │ 07. Priorizador │                                            │
│  │     Ações       │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│  ┌────────▼────────┐                                            │
│  │ 23. Planejador  │                                            │
│  │  Conteúdo       │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│  ┌────────▼────────┐                                            │
│  │ 24. Calibrador  │                                            │
│  │     Canais      │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
└───────────┼──────────────────────────────────────────────────────┘
            │
┌───────────▼──────────────────────────────────────────────────────┐
│                        FASE 4: EXECUÇÃO                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────┐                                            │
│  │ 08. Gerador     │                                            │
│  │  Plano          │                                            │
│  │  Simplificado   │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│  ┌────────▼────────┐                                            │
│  │ 26. Gerador     │                                            │
│  │  Roadmap        │                                            │
│  │  Trimestral     │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│           ▼                                                      │
│  ┌─────────────────┐                                            │
│  │    EXECUÇÃO     │                                            │
│  │      (Humano    │                                            │
│  │   ou Automat.)  │                                            │
│  └────────┬────────┘                                            │
│           │                                                      │
│           │ (Novos dados)                                        │
│           └──────────────────────────────────┐                   │
│                                              │                   │
└──────────────────────────────────────────────┼───────────────────┘
                                               │
                                    (reinicia ciclo de coleta)
```

## 8.2 Fluxo Mínimo (Stack Mínima - 8 Skills)

```
01. Triagem → 02. Scan Digital → 03. Organizador de Base
                                          │
                                          ▼
                              04. Interpretador de Cenário
                                          │
                                          ▼
                              05. Minerador de Oportunidades
                                          │
                                          ▼
                              06. Definidor de Posicionamento
                                          │
                                          ▼
                              07. Priorizador de Ações
                                          │
                                          ▼
                              08. Gerador de Plano Simplificado
                                          │
                                          ▼
                                     EXECUÇÃO
```

## 8.3 Regras de Fluxo

1. **Nenhuma skill pula etapas**: Interpretação só ocorre após organização, decisão só após interpretação.
2. **Feedback loop obrigatório**: Execução gera novos dados que reiniciam o ciclo.
3. **Paralelismo permitido**: Skills de coleta podem rodar em paralelo se não houver dependência direta.
4. **Checkpoint de qualidade**: Antes de entrar em Interpretação, validar completude da base (>60%).
5. **Timeboxing**: Cada fase tem tempo máximo definido para evitar paralisia por análise.

---

# 9. MATRIZ FINAL DAS SKILLS

| # | Nome da Skill | Nível | Função | Input Principal | Output Principal | Impacto | Base que Alimenta |
|---|---------------|-------|--------|-----------------|------------------|---------|-------------------|
| 1 | Triagem Rápida de Negócio | NUCLEAR | COLETA | Questionário + URLs | Perfil estruturado do negócio | ALTO | SOBRE O NEGÓCIO |
| 2 | Scan Digital Essencial | NUCLEAR | COLETA | Nome + URLs do negócio | Mapa de presença digital | ALTO | INSTAGRAM, SEO |
| 3 | Organizador de Base Mínima | NUCLEAR | ORGANIZA | Outputs de coleta | Base unificada e indexada | ALTO | TODOS OS MÓDULOS |
| 4 | Interpretador de Cenário | NUCLEAR | INTERPRETA | Base organizada | Insights sobre situação atual | ALTO | OPORTUNIDADES |
| 5 | Minerador de Oportunidades | NUCLEAR | INTERPRETA | Cenário interpretado | Lista de oportunidades classificadas | ALTO | OPORTUNIDADES |
| 6 | Definidor de Posicionamento | NUCLEAR | DECIDE | Oportunidades + oferta | Statement de posicionamento | ALTO | POSICIONAMENTO |
| 7 | Priorizador de Ações | NUCLEAR | DECIDE | Oportunidades + recursos | Top 5-7 prioridades | ALTO | PRIORIDADES |
| 8 | Gerador de Plano Simplificado | NUCLEAR | EXECUTA | Prioridades | Plano passo a passo | ALTO | PLANO DE AÇÃO |
| 9 | Pesquisador de Público Profundo | IMPORTANTE | COLETA | Nicho + público declarado | Dores, desejos, linguagem | ALTO | PÚBLICO E MERCADO |
| 10 | Minerador de Concorrência | IMPORTANTE | COLETA | Nicho + localização | Perfil de 5-10 concorrentes | MÉDIO | CONCORRÊNCIA |
| 11 | Analisador de SEO Básico | IMPORTANTE | COLETA | URL do site + nicho | Saúde SEO + palavras-chave | MÉDIO | SEO E BUSCA |
| 12 | Avaliador de Conteúdo Instagram | IMPORTANTE | INTERPRETA | URL Instagram + posicionamento | Análise de conteúdo e engajamento | MÉDIO | INSTAGRAM E CONTEÚDO |
| 13 | Mapeador de Jornada do Cliente | IMPORTANTE | INTERPRETA | Oferta + público + canais | Jornada completa por etapas | ALTO | OFERTA E CONVERSÃO |
| 14 | Validador de Oferta | IMPORTANTE | INTERPRETA | Oferta + público + concorrência | Avaliação de clareza e alinhamento | ALTO | OFERTA E CONVERSÃO |
| 15 | Estruturador de Mensagem | IMPORTANTE | DECIDE | Posicionamento + público | Messaging principal estruturado | ALTO | POSICIONAMENTO |
| 16 | Rastreador de Tendências de Nicho | OPCIONAL | COLETA | Nicho + fontes monitoramento | Tendências emergentes | MÉDIO | TENDÊNCIAS |
| 17 | Analisador de Reviews e Reputação | OPCIONAL | COLETA | Nome do negócio + URLs | Análise de reviews e sentimento | MÉDIO | REPUTAÇÃO |
| 18 | Pesquisador de Intenção de Busca | OPCIONAL | COLETA | Nicho + palavras semente | Intenções de busca mapeadas | ALTO | SEO E BUSCA |
| 19 | Segmentador de Personas | OPCIONAL | ORGANIZA | Pesquisa de público + dados | Personas detalhadas | MÉDIO | PÚBLICO E MERCADO |
| 20 | Comparador de Diferenciação | OPCIONAL | INTERPRETA | Negócio + concorrência | Matriz comparativa + diferenciais | ALTO | POSICIONAMENTO |
| 21 | Detector de Gargalos de Conversão | OPCIONAL | INTERPRETA | Jornada + analytics | Gargalos identificados por etapa | ALTO | OFERTA E CONVERSÃO |
| 22 | Otimizador de Funil | OPCIONAL | INTERPRETA | Gargalos + melhores práticas | Otimizações propostas por etapa | ALTO | OFERTA E CONVERSÃO |
| 23 | Planejador de Conteúdo Estratégico | OPCIONAL | DECIDE | Messaging + SEO + jornada | Calendário editorial estratégico | ALTO | INSTAGRAM, SEO |
| 24 | Calibrador de Canais | OPCIONAL | DECIDE | Canais ativos + desempenho | Alocação recomendada de recursos | MÉDIO | CANAIS (ESTRATÉGIA) |
| 25 | Monitor de Evolução de Mercado | OPCIONAL | INTERPRETA | Linha de base + dados contínuos | Mudanças identificadas + ajustes | MÉDIO | EVOLUÇÃO DE MERCADO |
| 26 | Gerador de Roadmap Trimestral | OPCIONAL | EXECUTA | Prioridades + objetivos | Roadmap de 90 dias com marcos | ALTO | PLANO DE AÇÃO |
| 27 | Auditor de Coerência Geral | OPCIONAL | INTERPRETA | Todos os módulos da base | Índice de coerência + incoerências | ALTO | COERÊNCIA |
| 28 | Estrategista de Engenharia Social Profunda | IMPORTANTE | DECIDE/EXECUTA | Base engenharia social + público | Campanhas coordenadas de influência | ALTO | POSICIONAMENTO, PLANO DE AÇÃO |
| 29 | **Auditor de Risco Reputacional** | **NUCLEAR** | **INTERPRETA/DECIDE** | **Mensagens + campanhas planejadas** | **Parecer de risco + plano contingência** | **CRÍTICO** | **POSICIONAMENTO, PLANO DE AÇÃO** |
| 30 | **Tradutor Operacional de Estratégia** | **NUCLEAR** | **DECIDE/EXECUTA** | **Planos estratégicos + recursos** | **Checklist executivo + cronograma** | **CRÍTICO** | **PLANO DE AÇÃO, PRIORIDADES** |
| 31 | **Detector de Estagnação & Pivotagem** | **IMPORTANTE** | **INTERPRETA/DECIDE** | **Histórico métricas + mercado** | **Recomendação pivotar + direções** | **ALTO** | **PRIORIDADES, PLANO DE AÇÃO** |
| 32 | **Orquestrador de Inteligência Contínua** | **NUCLEAR** | **ORGANIZA/DECIDE** | **Todos outputs + base consolidada** | **Ciclo próximo + resumo executivo** | **CRÍTICO** | **TODOS OS MÓDULOS** |

---

# 10. MENOR CONJUNTO DE SKILLS CAPAZ DE GERAR VALOR RAPIDO

## Resposta Direta: **5 Skills**

Para gerar valor rápido, entender o negócio e entregar estratégia prática sem inchar o sistema, o **mínimo viável absoluto** é:

### As 5 Skills Essenciais:

1. **Triagem Rápida de Negócio** (COLETA)
2. **Scan Digital Essencial** (COLETA)
3. **Organizador de Base Mínima** (ORGANIZA)
4. **Minerador de Oportunidades** (INTERPRETA)
5. **Gerador de Plano Simplificado** (EXECUTA)

### Por que estas 5?

| Skill | Razão da Inclusão | O que seria perdido sem ela |
|-------|-------------------|----------------------------|
| Triagem | Sem contexto do negócio, tudo é achismo | Não saberia tipo de negócio, oferta, público, recursos |
| Scan Digital | Sem saber onde o negócio está presente, não há como diagnosticar | Ignoraria gaps críticos de presença online |
| Organizador | Dados soltos não viram decisão | Informação coletada seria inutilizável |
| Minerador de Oportunidades | Transforma problemas em caminhos | Teria diagnóstico mas não direções de ação |
| Gerador de Plano | Estratégia sem plano é teoria | Não haveria próximos passos executáveis |

### O que este conjunto de 5 skills entrega em 2-3 horas:

✅ **Entendimento do negócio**: nicho, oferta, público, maturidade, recursos  
✅ **Diagnóstico digital**: onde está presente, onde está ausente, qualidade básica  
✅ **3-5 oportunidades claras**: quick wins e ações de maior impacto  
✅ **Plano de ação com 5-7 passos**: o que fazer, em que ordem, prazos sugeridos  
✅ **Direção estratégica**: foco claro para os próximos 30 dias  

### O que este conjunto NÃO entrega (e por que não importa no início):

❌ Pesquisa profunda de público → *Pode esperar 30 dias*  
❌ Análise de concorrência detalhada → *Oportunidades óbvias não exigem isso*  
❌ SEO técnico avançado → *Primeiro precisa existir e ser claro*  
❌ Planejamento de conteúdo trimestral → *Primeiro defina o que fazer nos próximos 7 dias*  
❌ Roadmap de 90 dias → *Comece com 30 dias bem executados*  

### Tempo estimado de execução:

- Triagem: 30 min (questionário + entrevista rápida)
- Scan Digital: 20 min (verificação manual ou semi-automatizada)
- Organizador: 15 min (consolidação em estrutura)
- Minerador de Oportunidades: 30 min (análise e classificação)
- Gerador de Plano: 25 min (detalhamento de passos)

**Total: ~2 horas** para estratégia completa e acionável.

### Esta é a resposta para: "Por onde começo?"

Se você tem que escolher apenas um conjunto para validar o sistema, gerar valor imediato e provar eficácia: **comece com estas 5 skills**.

Depois que o básico estiver rodando e gerando resultados, expanda para as 8 da Stack Mínima, depois 15 da Profissional, e finalmente 22 da Avançada.

---

# 11. CAMINHO DE EVOLUÇÃO

## 11.1 Da Stack Mínima (8 skills) para a Profissional (15 skills)

### Quando fazer essa transição:

- ✅ Sistema mínimo rodando consistentemente há 60+ dias
- ✅ Primeiros resultados positivos validados
- ✅ Necessidade de maior profundidade em áreas específicas
- ✅ Recursos disponíveis para operar mais skills

### O que adicionar nesta ordem:

**Semana 1-2:** Adicionar Skill 09 (Pesquisador de Público Profundo)  
→ *Justificativa:* Entender melhor o público melhora todas as decisões subsequentes

**Semana 3-4:** Adicionar Skill 10 (Minerador de Concorrência)  
→ *Justificativa:* Com público entendido, agora entenda o espaço competitivo

**Semana 5-6:** Adicionar Skill 14 (Validador de Oferta)  
→ *Justificativa:* Com público e concorrência mapeados, valide se a oferta está alinhada

**Semana 7-8:** Adicionar Skill 13 (Mapeador de Jornada do Cliente)  
→ *Justificativa:* Agora otimize o caminho desde descoberta até compra

**Semana 9-10:** Adicionar Skill 15 (Estruturador de Mensagem)  
→ *Justificativa:* Com jornada mapeada, refine a mensagem para cada etapa

**Semana 11-12:** Adicionar Skills 11 (SEO Básico) + 12 (Avaliador de Conteúdo IG)  
→ *Justificativa:* Agora otimize canais específicos com mais profundidade

### O que muda na operação:

| Aspecto | Stack Mínima | Stack Profissional |
|---------|--------------|-------------------|
| Tempo de ciclo | 2-3 horas | 4-6 horas |
| Profundidade de insight | Básica | Intermediária |
| Tipos de negócio atendidos | 80% dos casos | 95% dos casos |
| Precisão de recomendações | Boa | Muito boa |
| Necessidade de dados | Mínimos | Moderados |

### Riscos a evitar nesta transição:

❌ **Adicionar todas de uma vez**: Perde-se clareza do que está funcionando  
❌ **Pular a validação da mínima**: Não sabe se complexidade adicional é necessária  
❌ **Não documentar aprendizado**: Cada nova skill deve gerar learnings documentados  
❌ **Esquecer de desligar o desnecessário**: Se uma skill nova substitui uma antiga, desative a antiga  

---

## 11.2 Da Stack Profissional (15 skills) para a Avançada (22 skills)

### Quando fazer essa transição:

- ✅ Stack profissional operando há 90+ dias
- ✅ Negócio(s) atendido(s) em estágio de escala
- ✅ Necessidade de inteligência contínua, não pontual
- ✅ Recursos dedicados para manutenção do sistema
- ✅ Complexidade do mercado exige monitoramento constante

### O que adicionar nesta ordem:

**Mês 1:** Skills de monitoramento contínuo  
- Skill 16 (Rastreador de Tendências)  
- Skill 25 (Monitor de Evolução de Mercado)  
→ *Justificativa:* Comece mantendo-se atualizado sobre mudanças externas

**Mês 2:** Skills de especialização em conversão  
- Skill 21 (Detector de Gargalos)  
- Skill 22 (Otimizador de Funil)  
→ *Justificativa:* Com tráfego estabelecido, maximize conversão

**Mês 3:** Skills de refinamento de segmentação  
- Skill 18 (Pesquisador de Intenção de Busca)  
- Skill 19 (Segmentador de Personas)  
→ *Justificativa:* Afine targeting para melhorar ROI

**Mês 4:** Skills de diferenciação competitiva  
- Skill 20 (Comparador de Diferenciação)  
- Skill 17 (Analisador de Reviews)  
→ *Justificativa:* Em mercados competitivos, diferenciação é crucial

**Mês 5:** Skills de planejamento de longo prazo  
- Skill 23 (Planejador de Conteúdo Estratégico)  
- Skill 26 (Gerador de Roadmap Trimestral)  
→ *Justificativa:* Agora planeje trimestres, não apenas semanas

**Mês 6:** Skill de auditoria transversal  
- Skill 27 (Auditor de Coerência Geral)  
- Skill 24 (Calibrador de Canais)  
→ *Justificativa:* Garanta que tudo permanece alinhado em escala

### O que muda na operação:

| Aspecto | Stack Profissional | Stack Avançada |
|---------|-------------------|----------------|
| Frequência de execução | Pontual (por projeto) | Contínua (monitoramento) |
| Tempo de ciclo | 4-6 horas | 8-12 horas (ou distribuído) |
| Automação necessária | Baixa | Média a Alta |
| Tipos de negócio | Pequenas e médias empresas | Empresas em escala |
| Valor gerado | Estratégia clara | Inteligência competitiva sustentável |

### Infraestrutura necessária para Stack Avançada:

- **Ferramentas de automação**: Coleta automática de dados (APIs, scrapers éticos)
- **Dashboard de monitoramento**: Visualização em tempo real de métricas-chave
- **Alertas configurados**: Notificações automáticas quando thresholds são atingidos
- **Processos documentados**: Playbooks claros para cada skill
- **Revisão periódica**: Checkpoints semanais/mensais obrigatórios

### Riscos a evitar nesta transição:

❌ **Complexidade prematura**: Só avance se a profissional estiver dominada  
❌ **Automação antes do processo**: Não automatize o que ainda não está claro manualmente  
❌ **Monitoramento sem ação**: Dados contínuos exigem processos de decisão ágeis  
❌ **Esquecer o essencial**: Skills avançadas não substituem as nucleares, apenas complementam  
❌ **Inchaço por ego**: Não adicione skills por "parecer sofisticado", apenas se gerarem valor mensurável  

---

## 11.3 Princípios de Evolução Sustentável

### Regra 70-20-10 da Evolução:

- **70% do tempo**: Operar e refinar o stack atual
- **20% do tempo**: Testar 1-2 novas skills em ambiente controlado
- **10% do tempo**: Pesquisar e planejar próxima camada de evolução

### Gatilhos para Evoluir:

| Gatilho | Ação Recomendada |
|---------|------------------|
| Mesma pergunta surgindo repetidamente | Adicionar skill que responde essa pergunta sistematicamente |
| Decisão sendo adiada por falta de dado | Adicionar skill de coleta desse dado |
| Resultado estagnado há 60+ dias | Adicionar skill de interpretação mais profunda |
| Escala aumentando (mais negócios/clientes) | Adicionar skills de automação e monitoramento |
| Concorrência acelerando | Adicionar skills de inteligência competitiva |

### Gatilhos para **NÃO** Evoluir:

| Sinal | Ação Recomendada |
|-------|------------------|
| Sistema atual ainda não gerou resultado mensurável | Não evolua, otimize o atual |
| Equipe sobrecarregada com stack atual | Não evolua, simplifique ou automatize |
| Nova skill resolve problema que não existe | Não adicione |
| Complexidade crescendo sem valor proporcional | Volte uma camada, consolide |

---

# 12. O QUE EVITAR NA IMPLEMENTAÇÃO

## 12.1 Erros de Arquitetura

### ❌ Skills Bonitas e Inúteis
**Erro:** Criar skills que geram relatórios impressionantes mas não habilitam decisões.  
**Exemplo:** Skill que analisa 50 métricas de Instagram mas não diz o que mudar no conteúdo.  
**Como evitar:** Toda skill deve terminar com campo "Decisões Habilitadas" ou "Ações Sugeridas".

---

### ❌ Skills Redundantes
**Erro:** Duas skills coletando o mesmo dado ou respondendo a mesma pergunta.  
**Exemplo:** Skill A e Skill B ambas analisando concorrência com metodologia similar.  
**Como evitar:** Matriz de responsabilidades clara. Um dado, uma skill responsável.

---

### ❌ Skills sem Input/Output Claros
**Erro:** Skill que "analisa coisas" sem especificar o que entra e o que sai.  
**Exemplo:** "Skill de Análise de Mercado" sem definição de quais dados entram nem qual formato de saída.  
**Como evitar:** Template obrigatório para cada skill com campos: Input, Processo, Output.

---

### ❌ Processos Inchados
**Erro:** Skill que requer 20 inputs diferentes e 3 horas para rodar.  
**Exemplo:** Triagem com 100 perguntas em vez de 15-20 essenciais.  
**Como evitar:** Regra: nenhuma skill deve levar >30 min para executar manualmente. Se levar, quebre em sub-skills.

---

## 12.2 Erros de Operação

### ❌ Análises que Não Viram Ação
**Erro:** Rodar skills, gerar insights, arquivar em pasta e não executar nada.  
**Exemplo:** Identificar 10 oportunidades, implementar 0.  
**Como evitar:** Regra obrigatória: toda sessão de análise termina com compromisso de 3 ações para os próximos 7 dias.

---

### ❌ Bases que Só Viram Arquivo Morto
**Erro:** Construir base de conhecimento linda que ninguém consulta depois.  
**Exemplo:** Base com 500 páginas de dados, zero uso em decisões.  
**Como evitar:** 
- Dashboard de 1 página com o essencial
- Revisão obrigatória semanal da base
- Links explícitos entre dados e decisões tomadas

---

### ❌ Sistemas Difíceis de Manter
**Erro:** Arquitetura tão complexa que requer PhD para operar.  
**Exemplo:** Base com 50 tabelas relacionais, queries SQL complexas para extrair insights simples.  
**Como evitar:** 
- Teste da "pessoa inteligente leiga": ela consegue entender em 10 min?
- Documentação visual (fluxogramas, não apenas texto)
- Scripts de manutenção automatizados

---

### ❌ Pular a Stack Mínima
**Erro:** Querer começar já na Advanced porque "é mais completa".  
**Exemplo:** Implementar 22 skills no dia 1 sem dominar as 8 básicas.  
**Como evitar:** Regra de progressão obrigatória. Só evolua após 60 dias de operação consistente da camada atual.

---

### ❌ Ignorar o Feedback Loop
**Erro:** Sistema unidirecional que não aprende com execução.  
**Exemplo:** Rodar análise, executar plano, mas não alimentar resultados de volta na base.  
**Como evitar:** 
- Campo obrigatório "Resultados Observados" em cada ciclo
- Comparação mensal: previsto vs. realizado
- Ajuste de pesos e prioridades baseado em dados reais

---

### ❌ Superengenheirar desde o Dia 1
**Erro:** Tentar prever todos os cenários futuros e construir para todos eles.  
**Exemplo:** Criar 50 campos "caso precise no futuro" na base de dados.  
**Como evitar:** 
- Princípio YAGNI (You Ain't Gonna Need It)
- Adicione campos apenas quando uma skill específica precisar
- Refatore a cada 30 dias: remova o não-usado

---

### ❌ Esquecer o Humano no Loop
**Erro:** Automatizar tudo e remover julgamento humano de decisões importantes.  
**Exemplo:** Sistema decide sozinho prioridades sem revisão humana.  
**Como evitar:** 
- Skills de DECIDE geram recomendações, não ordens
- Checkpoint humano obrigatório antes de execução
- Sistema apoia decisão, não substitui decisor

---

### ❌ Não Medir o Próprio Sistema
**Erro:** Usar o sistema para gerar estratégias mas não medir se o sistema está funcionando.  
**Exemplo:** Zero métricas sobre eficácia das próprias skills.  
**Como evitar:** 
- Meta-métricas: "Quantas decisões foram habilitadas por esta skill?"
- "Qual % de recomendações foram implementadas?"
- "Qual resultado gerou cada implementação?"

---

## 12.3 Checklist Anti-Erros

Antes de implementar qualquer skill, responda:

- [ ] Esta skill resolve um problema real ou é "nice to have"?
- [ ] O input e output estão claramente definidos?
- [ ] Esta skill duplica função de outra já existente?
- [ ] Uma pessoa inteligente consegue operar esta skill em <30 min?
- [ ] O output desta skill habilita pelo menos 1 decisão concreta?
- [ ] Existe processo para alimentar resultados de volta na base?
- [ ] Esta skill é necessária AGORA ou pode esperar 60 dias?
- [ ] O valor gerado justifica o tempo de operação?
- [ ] Existe documentação clara de como operar esta skill?
- [ ] Há métrica para medir eficácia desta skill?

**Se alguma resposta for "não" ou "não sei":** não implemente ainda. Refine a proposta.

---

## 12.4 Princípios Finais de Implementação

### Princípio da Navalha de Occam Digital:
> "Entre duas architectures de skills que geram o mesmo valor, escolha a mais simples."

### Princípio do Valor Comprovado:
> "Nenhuma skill nova entra em produção sem prova de valor em ambiente controlado."

### Princípio da Manutenção Sustentável:
> "Se você não pode manter este sistema operando consistentemente por 12 meses, ele é complexo demais."

### Princípio da Decisão como Produto:
> "O produto final deste sistema não é relatório, não é dashboard, não é base de dados. O produto final é **decisão melhor tomada mais rápido**."

---

# CONCLUSÃO

Esta arquitetura de skills foi projetada para ser:

✅ **Modular**: Ative/desative skills conforme necessidade  
✅ **Escalável**: Evolua de 5 para 22 skills sem refazer tudo  
✅ **Acionável**: Cada skill termina em decisão ou ação concreta  
✅ **Sustentável**: Mantenha operando por anos sem burnout  
✅ **Adaptável**: Funciona para negócios locais, digitais, especialistas, clínicas, etc.  

O sistema não é um fim em si mesmo. É um **meio para gerar clareza estratégica e execução consistente**.

**Comece pequeno. Valide rápido. Escale com disciplina.**

---

*Documento criado para o Sistema Antigravity de Inteligência de Negócio*  
*Versão 1.0 - Pronto para implementação*
