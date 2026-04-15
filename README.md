# Transcritor - App de Transcrição de Áudio e Vídeo

Aplicativo minimalista para transcrição de arquivos de áudio e vídeo usando a API do Google Gemini.

## ✨ Funcionalidades

- **Upload de Arquivos**: Arraste e solte arquivos MP3, WAV, MP4, MOV, WebM (até 20MB)
- **Transcrição via Link**: Suporte para links diretos de arquivos de áudio/vídeo
- **Design Minimalista**: Interface limpa com fonte Space Grotesk
- **Histórico Local**: Suas transcrições ficam salvas no navegador
- **Exportação**: Baixe transcrições em formato .txt ou copie para área de transferência
- **Multi-idioma**: Português, Inglês, Espanhol, Francês e Alemão
- **Configurações Persistidas**: API Key, modelo e idioma salvos localmente

## 🚀 Como Usar

### Opção 1: Navegador (Mais Simples)

1. Baixe o arquivo `transcritor.html` deste repositório
2. Abra diretamente no seu navegador (Chrome, Edge, Firefox)
3. Configure sua API Key do Google Gemini
4. Arraste seu arquivo de áudio/vídeo e clique em "Transcrever"

### Opção 2: Aplicativo Desktop (.exe Portátil)

#### Pré-requisitos
- Node.js 18+ instalado
- npm ou yarn

#### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/SEU-USUARIO/transcritor-app.git
cd transcritor-app
```

2. **Instale as dependências:**
```bash
npm install
```

3. **Teste em modo desenvolvimento:**
```bash
npm run dev
```

4. **Compile o executável portátil:**
```bash
npm run build:exe
```

O arquivo `.exe` será gerado na pasta `dist-electron/`.

## 🔑 Obtendo API Key do Google Gemini

1. Acesse [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada
5. Cole no campo de configurações do app

**Importante:** A API Key é salva apenas no seu navegador/computador e não é compartilhada.

## 📁 Estrutura do Projeto

```
transcritor-app/
├── transcritor.html          # App standalone (funciona só com navegador)
├── index.html                # App React + Electron
├── App.tsx                   # Componente principal
├── electron-main.cjs         # Configuração do Electron
├── package.json              # Dependências e scripts
└── services/
    └── geminiService.ts      # Integração com API Gemini
```

## 🎨 Design

- **Fonte**: Space Grotesk (Google Fonts)
- **Cores**: Paleta monocromática (#fafafa, #1a1a1a, #737373)
- **Estilo**: Minimalista, cantos arredondados, sombras sutis

## 📝 Formatos Suportados

- **Áudio**: MP3, WAV, OGG, M4A
- **Vídeo**: MP4, MOV, WebM
- **Tamanho máximo**: 20MB

## ⚠️ Limitações

- Links do YouTube requerem download prévio do arquivo devido a restrições CORS
- Arquivos acima de 20MB não são suportados na versão browser
- Requer conexão com internet para funcionar (chamadas à API Gemini)

## 🛠️ Tecnologias

- **Frontend**: React 19, TypeScript, Vite
- **Desktop**: Electron
- **IA**: Google Gemini API
- **Estilização**: Tailwind CSS

## 📄 Licença

MIT

---

**Dica**: Para melhores resultados, use arquivos de áudio claros e sem muito ruído de fundo.
