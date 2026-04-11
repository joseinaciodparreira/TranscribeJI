
const { app, BrowserWindow } = require('electron');
const path = require('path');
const isDev = process.env.NODE_ENV === 'development';

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    title: "TrancribeJI",
    icon: path.join(__dirname, 'public/favicon.ico'), // Opcional: adicione um ícone depois
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  // Em desenvolvimento, carrega do servidor local. Em produção, carrega o arquivo index.html
  if (isDev) {
    win.loadURL('http://localhost:3000');
  } else {
    win.loadFile(path.join(__dirname, 'dist/index.html'));
  }

  // Remove o menu padrão (opcional)
  // win.setMenu(null);
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
