
import { GoogleGenAI } from "@google/genai";

const DEFAULT_API_KEY = process.env.API_KEY || "";

export const transcribeMedia = async (
  base64Data: string,
  mimeType: string,
  fileName: string,
  apiKey: string = DEFAULT_API_KEY,
  modelName: string = "gemini-3-flash-preview"
): Promise<string> => {
  if (!apiKey) {
    throw new Error("A chave da API não está configurada.");
  }

  const ai = new GoogleGenAI({ apiKey });
  
  const prompt = `Transcreva o seguinte conteúdo de ${mimeType.startsWith('audio') ? 'áudio' : 'vídeo'} com precisão. 
  Se possível, identifique diferentes falantes. 
  Mantenha o idioma original e a pontuação. 
  Se o arquivo não contiver fala, escreva "Nenhuma fala detectada".`;

  const response = await ai.models.generateContent({
    model: modelName,
    contents: [
      {
        parts: [
          {
            inlineData: {
              data: base64Data,
              mimeType: mimeType,
            },
          },
          { text: prompt },
        ],
      },
    ],
  });

  if (!response.text) {
    throw new Error("Nenhum texto de transcrição retornado pelo modelo.");
  }

  return response.text;
};

export const transcribeFromLink = async (
  url: string,
  apiKey: string = DEFAULT_API_KEY,
  modelName: string = "gemini-3-flash-preview"
): Promise<string> => {
  if (!apiKey) {
    throw new Error("A chave da API não está configurada.");
  }

  const ai = new GoogleGenAI({ apiKey });
  
  const prompt = `Por favor, analise o conteúdo nesta URL: ${url}. 
  Se for um link de arquivo de vídeo ou áudio, transcreva seu conteúdo com precisão. 
  Se for um link do YouTube, resuma o conteúdo do vídeo em detalhes como uma transcrição.
  Forneça uma saída de texto limpa e legível.`;

  const response = await ai.models.generateContent({
    model: modelName,
    contents: prompt,
    config: {
      tools: [{ googleSearch: {} }] // Use search grounding to help if the URL is web-based
    }
  });

  if (!response.text) {
    throw new Error("Falha ao gerar transcrição a partir do link fornecido.");
  }

  return response.text;
};
