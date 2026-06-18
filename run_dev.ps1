# PowerShell script to start the FuelTrack AI development environment

Write-Host "Starting FuelTrack AI..." -ForegroundColor Green

# ── Backend ───────────────────────────────────────────────────────
# IMPORTANT: Run uvicorn from the PROJECT ROOT with `server.main:app`
# NOT from inside the server/ folder with `main:app`
Write-Host "Starting FastAPI Backend on http://localhost:8080" -ForegroundColor Cyan
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", ".\venv\Scripts\Activate.ps1; .\venv\Scripts\python.exe -m uvicorn server.main:app --reload --port 8080" -WorkingDirectory $PSScriptRoot

# ── Frontend ──────────────────────────────────────────────────────
Write-Host "Starting Vite Frontend on http://localhost:5173" -ForegroundColor Cyan
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "npm run dev" -WorkingDirectory "$PSScriptRoot\client"

Write-Host "Both servers started. Open http://localhost:5173 in your browser." -ForegroundColor Green
