
import { GoogleGenAI } from "@google/genai";

const API_KEY = process.env.API_KEY || "";

export const transcribeMedia = async (
  base64Data: string,
  mimeType: string,
  fileName: string
): Promise<string> => {
  if (!API_KEY) {
    throw new Error("API Key is not configured.");
  }

  const ai = new GoogleGenAI({ apiKey: API_KEY });
  
  const prompt = `Transcribe the following ${mimeType.startsWith('audio') ? 'audio' : 'video'} content accurately. 
  If possible, identify different speakers. 
  Maintain the original language and punctuation. 
  If the file contains no speech, state "No speech detected".`;

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
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
    throw new Error("No transcription text returned from the model.");
  }

  return response.text;
};

export const transcribeFromLink = async (url: string): Promise<string> => {
  if (!API_KEY) {
    throw new Error("API Key is not configured.");
  }

  const ai = new GoogleGenAI({ apiKey: API_KEY });
  
  const prompt = `Please analyze the content at this URL: ${url}. 
  If it is a video or audio file link, transcribe its contents accurately. 
  If it is a YouTube link, summarize the video content in detail as a transcription.
  Provide a clean, readable text output.`;

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: prompt,
    config: {
      tools: [{ googleSearch: {} }] // Use search grounding to help if the URL is web-based
    }
  });

  if (!response.text) {
    throw new Error("Failed to generate transcription from the provided link.");
  }

  return response.text;
};
