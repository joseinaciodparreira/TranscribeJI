
export interface TranscriptionEntry {
  id: string;
  name: string;
  type: 'file' | 'link';
  mimeType?: string;
  text: string;
  timestamp: number;
  duration?: string;
}

export enum AppStatus {
  IDLE = 'idle',
  UPLOADING = 'uploading',
  TRANSCRIBING = 'transcribing',
  ERROR = 'error',
  SUCCESS = 'success'
}
