NovoarSB — Pro UI
=================

This Electron UI is built to be shipped with your product. It does not include your bot `main.py` or `config.json`.

Features:
- Clean professional UI (compact, intuitive).
- Option to run using a virtualenv activation command (Windows or Unix).
- Persistent UI config saved to `ui-config.json` at app root.
- Start / Stop / Restart and live logs via stdout/stderr.

Windows virtualenv instructions (recommended for customers):
1. Create a venv in the project folder (or anywhere):
   python -m venv .venv
2. To test from command line (Windows):
   .venv\Scripts\activate.bat
   python main.py
3. In the UI Config tab, enable "Use virtualenv activation" and set the command to:
   C:\\full\\path\\to\\project\\.venv\\Scripts\\activate.bat
   (The UI will run: activate.bat && python "<script>" -> so ensure this path is correct)
4. Alternatively you can set the Python executable path directly to the venv python: 
   C:\\full\\path\\to\\project\\.venv\\Scripts\\python.exe
   (this avoids shell activation and is often more robust).

Packaging & distribution notes:
- Run `npm install` (installs electron) and `npm run start` for development.
- Use `electron-builder` or `electron-forge` to package for Windows/macOS/Linux.
- Ensure you do NOT ship user tokens/configs in the distributed bundle.
- For security, consider code signing and an update channel for customers.

Files included in this archive:
- main.js, preload.js
- renderer/index.html, renderer/style.css, renderer/renderer.js
- package.json (dev dependency electron)
- assets/logo.png (placeholder or your logo)
- ui-config.json will be created at runtime when the user saves config through the UI.

If you want, I can:
- Integrate an installer workflow (NSIS) and build scripts.
- Add telemetry opt-in, licensing checks, or a licensing/key system (I can sketch how to implement secure license validation).
- Create a branded theme builder so customers can choose accent colors and fonts.

