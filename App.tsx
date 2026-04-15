
import React, { useState, useEffect, useCallback } from 'react';
import { 
  FileText, 
  Upload, 
  Link as LinkIcon, 
  History, 
  Trash2, 
  Clipboard, 
  Check,
  Play,
  Clock,
  ChevronRight,
  Info,
  Settings as SettingsIcon,
  X
} from 'lucide-react';
import { AppStatus, TranscriptionEntry } from './types';
import { transcribeMedia, transcribeFromLink } from './services/geminiService';
import Button from './components/Button';

const App: React.FC = () => {
  const [status, setStatus] = useState<AppStatus>(AppStatus.IDLE);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [currentTranscription, setCurrentTranscription] = useState<string | null>(null);
  const [linkInput, setLinkInput] = useState('');
  const [history, setHistory] = useState<TranscriptionEntry[]>([]);
  const [copied, setCopied] = useState(false);
  const [activeTab, setActiveTab] = useState<'upload' | 'link'>('upload');
  const [selectedHistoryId, setSelectedHistoryId] = useState<string | null>(null);
  const [showSettings, setShowSettings] = useState(false);
  const [apiKey, setApiKey] = useState('');
  const [modelName, setModelName] = useState('gemini-1.5-flash');
  const [language, setLanguage] = useState('pt-BR');
  const [usageStats, setUsageStats] = useState({ requests: 0, totalChars: 0 });

  // Load history and settings from localStorage
  useEffect(() => {
    const savedHistory = localStorage.getItem('transcription_history');
    if (savedHistory) {
      try {
        setHistory(JSON.parse(savedHistory));
      } catch (e) {
        console.error("Failed to parse history", e);
      }
    }

    const savedApiKey = localStorage.getItem('gemini_api_key');
    if (savedApiKey) setApiKey(savedApiKey);

    const savedModel = localStorage.getItem('gemini_model_name');
    if (savedModel) setModelName(savedModel);

    const savedLanguage = localStorage.getItem('gemini_language');
    if (savedLanguage) setLanguage(savedLanguage);

    const savedStats = localStorage.getItem('transcription_usage_stats');
    if (savedStats) {
      try {
        setUsageStats(JSON.parse(savedStats));
      } catch (e) {
        console.error("Failed to parse stats", e);
      }
    }
  }, []);

  // Save history to localStorage
  useEffect(() => {
    localStorage.setItem('transcription_history', JSON.stringify(history));
  }, [history]);

  // Save stats to localStorage
  useEffect(() => {
    localStorage.setItem('transcription_usage_stats', JSON.stringify(usageStats));
  }, [usageStats]);

  // Save settings to localStorage
  const saveSettings = (newApiKey: string, newModel: string, newLanguage: string) => {
    setApiKey(newApiKey);
    setModelName(newModel);
    setLanguage(newLanguage);
    localStorage.setItem('gemini_api_key', newApiKey);
    localStorage.setItem('gemini_model_name', newModel);
    localStorage.setItem('gemini_language', newLanguage);
    setShowSettings(false);
  };

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    // Basic size check (browser limits for base64 strings)
    if (file.size > 20 * 1024 * 1024) {
      setErrorMessage("Arquivo muito grande. Por favor, limite a 20MB para processamento direto.");
      return;
    }

    setStatus(AppStatus.UPLOADING);
    setErrorMessage(null);

    const reader = new FileReader();
    reader.onload = async (e) => {
      const result = e.target?.result as string;
      const base64Data = result.split(',')[1];
      const mimeType = file.type;

      try {
        setStatus(AppStatus.TRANSCRIBING);
        const text = await transcribeMedia(base64Data, mimeType, file.name, apiKey, modelName, language);
        
        const newEntry: TranscriptionEntry = {
          id: Date.now().toString(),
          name: file.name,
          type: 'file',
          mimeType,
          text,
          timestamp: Date.now(),
        };

        setHistory(prev => [newEntry, ...prev]);
        setCurrentTranscription(text);
        setSelectedHistoryId(newEntry.id);
        setUsageStats(prev => ({
          requests: prev.requests + 1,
          totalChars: prev.totalChars + text.length
        }));
        setStatus(AppStatus.SUCCESS);
      } catch (err: any) {
        setErrorMessage(err.message || "Ocorreu um erro durante a transcrição.");
        setStatus(AppStatus.ERROR);
      }
    };

    reader.onerror = () => {
      setErrorMessage("Falha ao ler o arquivo.");
      setStatus(AppStatus.ERROR);
    };

    reader.readAsDataURL(file);
  };

  const handleLinkSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!linkInput.trim()) return;

    setStatus(AppStatus.TRANSCRIBING);
    setErrorMessage(null);

    try {
      const text = await transcribeFromLink(linkInput, apiKey, modelName, language);
      
      const newEntry: TranscriptionEntry = {
        id: Date.now().toString(),
        name: linkInput.length > 30 ? linkInput.substring(0, 27) + "..." : linkInput,
        type: 'link',
        text,
        timestamp: Date.now(),
      };

      setHistory(prev => [newEntry, ...prev]);
      setCurrentTranscription(text);
      setSelectedHistoryId(newEntry.id);
      setUsageStats(prev => ({
        requests: prev.requests + 1,
        totalChars: prev.totalChars + text.length
      }));
      setStatus(AppStatus.SUCCESS);
      setLinkInput('');
    } catch (err: any) {
      setErrorMessage(err.message || "Falha ao transcrever do link.");
      setStatus(AppStatus.ERROR);
    }
  };

  const copyToClipboard = () => {
    if (currentTranscription) {
      navigator.clipboard.writeText(currentTranscription);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const deleteHistoryItem = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setHistory(prev => prev.filter(item => item.id !== id));
    if (selectedHistoryId === id) {
      setCurrentTranscription(null);
      setSelectedHistoryId(null);
    }
  };

  const selectHistoryItem = (item: TranscriptionEntry) => {
    setCurrentTranscription(item.text);
    setSelectedHistoryId(item.id);
  };

  return (
    <div className="min-h-screen flex flex-col md:flex-row bg-[#fafafa]">
      {/* Sidebar - History */}
      <aside className="w-full md:w-72 border-r border-[#e5e5e5] bg-white flex flex-col shrink-0">
        <div className="p-8 border-b border-[#e5e5e5] flex items-center justify-between">
          <div className="flex items-center gap-3 font-semibold text-xl text-[#1a1a1a] tracking-tight">
            <FileText className="w-5 h-5" />
            <span>TrancribeJI</span>
          </div>
        </div>
        
        <div className="flex-1 overflow-y-auto p-4 space-y-1">
          <h3 className="text-[10px] font-medium text-[#737373] uppercase tracking-widest mb-4 px-3">Histórico</h3>
          {history.length === 0 ? (
            <div className="text-center py-12 px-4">
              <div className="bg-[#fafafa] w-14 h-14 rounded-2xl flex items-center justify-center mx-auto mb-4">
                <History className="w-6 h-6 text-[#d4d4d4]" />
              </div>
              <p className="text-sm text-[#737373] font-light">Nenhuma transcrição ainda</p>
            </div>
          ) : (
            history.map(item => (
              <div 
                key={item.id}
                onClick={() => selectHistoryItem(item)}
                className={`group p-4 rounded-xl cursor-pointer transition-all border ${
                  selectedHistoryId === item.id 
                    ? 'bg-[#f5f5f5] border-[#e5e5e5] text-[#1a1a1a]' 
                    : 'bg-transparent border-transparent hover:bg-[#fafafa] text-[#1a1a1a]'
                }`}>
                <div className="flex items-start justify-between">
                  <div className="flex flex-col gap-2 overflow-hidden">
                    <span className="text-sm font-medium truncate pr-4 tracking-tight">{item.name}</span>
                    <div className="flex items-center gap-2 text-[10px] text-[#a3a3a3]">
                      {item.type === 'file' ? <Upload size={10} /> : <LinkIcon size={10} />}
                      <span>{new Date(item.timestamp).toLocaleDateString('pt-BR')}</span>
                    </div>
                  </div>
                  <button 
                    onClick={(e) => deleteHistoryItem(item.id, e)}
                    className="opacity-0 group-hover:opacity-100 p-1.5 hover:text-red-500 transition-opacity rounded-lg hover:bg-red-50"
                  >
                    <Trash2 size={14} />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
        
        <div className="p-4 border-t border-[#e5e5e5] space-y-3">
          <button 
            onClick={() => setShowSettings(true)}
            className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl text-sm font-medium text-[#1a1a1a] hover:bg-[#fafafa] transition-colors border border-[#e5e5e5]"
          >
            <SettingsIcon size={16} />
            <span>Configurações</span>
          </button>
          <div className="text-center space-y-1.5 pt-2">
            <p className="text-[9px] text-[#a3a3a3] flex items-center justify-center gap-1.5">
              <Info size={10} /> Desenvolvido por Gemini 3 Flash
            </p>
            <p className="text-[10px] font-medium text-[#737373]">
              Criado por José Inácio D. Parreira
            </p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-screen overflow-hidden">
        {/* Header/Inputs */}
        <header className="p-8 md:p-12 max-w-4xl w-full mx-auto space-y-10 overflow-y-auto flex-1 scroll-smooth">
          <div className="space-y-3">
            <h1 className="text-4xl font-semibold tracking-tight text-[#1a1a1a]">Transcreva sua mídia</h1>
            <p className="text-[#737373] font-light text-lg">Converta arquivos de áudio e vídeo ou URLs em texto instantaneamente.</p>
          </div>

          <div className="bg-white rounded-2xl shadow-sm border border-[#e5e5e5] overflow-hidden">
            <div className="flex border-b border-[#e5e5e5]">
              <button 
                onClick={() => setActiveTab('upload')}
                className={`flex-1 py-4 text-sm font-medium transition-colors border-b-2 ${activeTab === 'upload' ? 'border-[#1a1a1a] text-[#1a1a1a]' : 'border-transparent text-[#737373] hover:text-[#1a1a1a]'}`}
              >
                Enviar Arquivo
              </button>
              <button 
                onClick={() => setActiveTab('link')}
                className={`flex-1 py-4 text-sm font-medium transition-colors border-b-2 ${activeTab === 'link' ? 'border-[#1a1a1a] text-[#1a1a1a]' : 'border-transparent text-[#737373] hover:text-[#1a1a1a]'}`}
              >
                Colar Link
              </button>
            </div>

            <div className="p-8">
              {activeTab === 'upload' ? (
                <div className="relative border-2 border-dashed border-[#e5e5e5] rounded-xl p-12 transition-colors hover:border-[#d4d4d4] group">
                  <input 
                    type="file" 
                    accept="audio/*,video/*"
                    onChange={handleFileUpload}
                    className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
                    disabled={status === AppStatus.TRANSCRIBING || status === AppStatus.UPLOADING}
                  />
                  <div className="flex flex-col items-center text-center space-y-5">
                    <div className="w-16 h-16 bg-[#fafafa] text-[#1a1a1a] rounded-2xl flex items-center justify-center group-hover:scale-105 transition-transform">
                      <Upload className="w-7 h-7" />
                    </div>
                    <div className="space-y-2">
                      <p className="font-medium text-[#1a1a1a] tracking-tight">Clique ou arraste para enviar</p>
                      <p className="text-sm text-[#737373] font-light">Áudio (MP3, WAV) ou Vídeo (MP4, MOV)</p>
                      <p className="text-xs text-[#a3a3a3]">Tamanho máximo 20MB</p>
                    </div>
                  </div>
                </div>
              ) : (
                <form onSubmit={handleLinkSubmit} className="space-y-4">
                  <div className="relative">
                    <LinkIcon className="absolute left-4 top-1/2 -translate-y-1/2 text-[#a3a3a3] w-5 h-5" />
                    <input 
                      type="url" 
                      placeholder="https://exemplo.com/video.mp4 ou URL do YouTube"
                      value={linkInput}
                      onChange={(e) => setLinkInput(e.target.value)}
                      className="w-full pl-12 pr-4 py-4 rounded-xl border border-[#e5e5e5] focus:outline-none focus:ring-2 focus:ring-[#1a1a1a] focus:border-transparent transition-all font-light"
                      required
                    />
                  </div>
                  <Button 
                    type="submit" 
                    className="w-full py-4 text-lg" 
                    isLoading={status === AppStatus.TRANSCRIBING}
                  >
                    Transcrever do Link
                  </Button>
                </form>
              )}
            </div>
          </div>

          {/* Loading / Error States */}
          {(status === AppStatus.TRANSCRIBING || status === AppStatus.UPLOADING) && (
            <div className="bg-white rounded-2xl shadow-sm border border-[#e5e5e5] p-12 text-center space-y-6">
              <div className="relative w-24 h-24 mx-auto">
                <div className="absolute inset-0 border-4 border-[#e5e5e5] rounded-full"></div>
                <div className="absolute inset-0 border-4 border-[#1a1a1a] rounded-full border-t-transparent animate-spin"></div>
                <div className="absolute inset-0 flex items-center justify-center">
                  <FileText className="w-8 h-8 text-[#1a1a1a] animate-pulse" />
                </div>
              </div>
              <div className="space-y-2">
                <h2 className="text-xl font-semibold text-[#1a1a1a]">
                  {status === AppStatus.UPLOADING ? "Lendo arquivo..." : "Transcrevendo conteúdo..."}
                </h2>
                <p className="text-[#737373] max-w-sm mx-auto">
                  Nossa IA está processando sua mídia. Isso geralmente leva de alguns segundos a um minuto, dependendo da duração.
                </p>
              </div>
            </div>
          )}

          {status === AppStatus.ERROR && (
            <div className="bg-red-50 border border-red-100 rounded-2xl p-6 flex items-start gap-4">
              <div className="bg-red-100 p-2 rounded-full text-red-600 shrink-0">
                <Info size={20} />
              </div>
              <div className="space-y-1">
                <h3 className="font-semibold text-red-900">Falha na Transcrição</h3>
                <p className="text-sm text-red-700">{errorMessage}</p>
                <Button 
                  variant="ghost" 
                  className="mt-2 text-red-700 hover:bg-red-100 p-0 text-sm font-semibold"
                  onClick={() => setStatus(AppStatus.IDLE)}
                >
                  Tentar novamente
                </Button>
              </div>
            </div>
          )}

          {/* Result Section */}
          {currentTranscription && status !== AppStatus.TRANSCRIBING && (
            <div className="bg-white rounded-2xl shadow-sm border border-[#e5e5e5] overflow-hidden flex flex-col">
              <div className="px-6 py-4 border-b border-[#e5e5e5] flex items-center justify-between bg-[#fafafa]/50">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 bg-[#1a1a1a] rounded-lg flex items-center justify-center text-white">
                    <FileText size={16} />
                  </div>
                  <h3 className="font-semibold text-[#1a1a1a]">Resultado da Transcrição</h3>
                </div>
                <div className="flex items-center gap-2">
                  <Button variant="ghost" className="h-9 px-3" onClick={copyToClipboard}>
                    {copied ? <Check size={16} className="text-green-600" /> : <Clipboard size={16} />}
                    <span className="text-xs">{copied ? 'Copiado' : 'Copiar'}</span>
                  </Button>
                </div>
              </div>
              <div className="p-8 prose prose-neutral max-w-none prose-p:leading-relaxed prose-p:text-[#1a1a1a]">
                <div className="whitespace-pre-wrap font-light text-[#1a1a1a] leading-relaxed">
                  {currentTranscription}
                </div>
              </div>
            </div>
          )}
        </header>
      </main>

      {/* Settings Modal */}
      {showSettings && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#1a1a1a]/50 backdrop-blur-sm">
          <div className="bg-white rounded-2xl shadow-xl border border-[#e5e5e5] w-full max-w-md overflow-hidden animate-in fade-in zoom-in duration-200">
            <div className="px-6 py-4 border-b border-[#e5e5e5] flex items-center justify-between">
              <h3 className="font-semibold text-[#1a1a1a] flex items-center gap-2">
                <SettingsIcon size={18} className="text-[#1a1a1a]" />
                Configurações
              </h3>
              <button 
                onClick={() => setShowSettings(false)}
                className="p-1 hover:bg-[#fafafa] rounded-full transition-colors"
              >
                <X size={20} className="text-[#a3a3a3]" />
              </button>
            </div>
            
            <form 
              onSubmit={(e) => {
                e.preventDefault();
                const formData = new FormData(e.currentTarget);
                saveSettings(
                  formData.get('apiKey') as string,
                  formData.get('modelName') as string,
                  formData.get('language') as string
                );
              }}
              className="p-6 space-y-6"
            >
              <div className="space-y-2">
                <label className="text-sm font-semibold text-[#1a1a1a] block">
                  Chave da API Gemini
                </label>
                <input 
                  type="password" 
                  name="apiKey"
                  defaultValue={apiKey}
                  placeholder="Cole sua chave da API aqui..."
                  className="w-full px-4 py-2 rounded-lg border border-[#e5e5e5] focus:outline-none focus:ring-2 focus:ring-[#1a1a1a] transition-all text-sm"
                />
                <p className="text-[10px] text-[#a3a3a3]">
                  Se deixado em branco, o aplicativo usará a chave padrão do sistema (se configurada).
                </p>
              </div>

              <div className="space-y-2">
                <label className="text-sm font-semibold text-[#1a1a1a] block">
                  Modelo da IA
                </label>
                <select 
                  name="modelName"
                  defaultValue={modelName}
                  className="w-full px-4 py-2 rounded-lg border border-[#e5e5e5] focus:outline-none focus:ring-2 focus:ring-[#1a1a1a] transition-all text-sm bg-white"
                >
                  <option value="gemini-1.5-flash">Gemini 1.5 Flash (Rápido)</option>
                  <option value="gemini-1.5-pro">Gemini 1.5 Pro (Preciso)</option>
                </select>
              </div>

              <div className="space-y-2">
                <label className="text-sm font-semibold text-[#1a1a1a] block">
                  Idioma da Transcrição
                </label>
                <select 
                  name="language" 
                  defaultValue={language}
                  className="w-full px-4 py-2 rounded-lg border border-[#e5e5e5] focus:outline-none focus:ring-2 focus:ring-[#1a1a1a] transition-all text-sm bg-white"
                >
                  <option value="pt-BR">Português (Brasil)</option>
                  <option value="en-US">Inglês (EUA)</option>
                  <option value="es-ES">Espanhol</option>
                  <option value="fr-FR">Francês</option>
                  <option value="de-DE">Alemão</option>
                </select>
              </div>

              <div className="p-4 bg-[#fafafa] rounded-xl space-y-3 border border-[#e5e5e5]">
                <h4 className="text-xs font-semibold text-[#737373] uppercase tracking-wider">Uso Local (Estimado)</h4>
                <div className="grid grid-cols-2 gap-4">
                  <div className="space-y-1">
                    <p className="text-[10px] text-[#a3a3a3]">Total de Pedidos</p>
                    <p className="text-lg font-semibold text-[#1a1a1a]">{usageStats.requests}</p>
                  </div>
                  <div className="space-y-1">
                    <p className="text-[10px] text-[#a3a3a3]">Caracteres Gerados</p>
                    <p className="text-lg font-semibold text-[#1a1a1a]">{usageStats.totalChars.toLocaleString()}</p>
                  </div>
                </div>
                <div className="pt-2 border-t border-[#e5e5e5]">
                  <a 
                    href="https://aistudio.google.com/app/plan_billing" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-[10px] text-[#1a1a1a] hover:text-[#1a1a1a] font-medium flex items-center gap-1"
                  >
                    Ver saldo real no Google AI Studio <ChevronRight size={10} />
                  </a>
                </div>
              </div>

              <div className="pt-4 flex gap-3">
                <Button 
                  type="button" 
                  variant="ghost" 
                  className="flex-1"
                  onClick={() => setShowSettings(false)}
                >
                  Cancelar
                </Button>
                <Button 
                  type="submit" 
                  className="flex-1"
                >
                  Salvar Alterações
                </Button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
