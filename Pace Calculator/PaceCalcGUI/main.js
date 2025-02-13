const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 600,
    height: 600,
    autoHideMenuBar: true,
    // window cant be resized
    resizable: false,
    // favicon
    icon: path.join(__dirname, 'assets/icons/gui/favicon.ico'),
    webPreferences: {
      nodeIntegration: true, // for simplicity
      contextIsolation: false
    }
  });

  win.loadFile('index.html');
}

app.whenReady().then(createWindow);

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
