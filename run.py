import subprocess
import sys
import os
import time
import shutil

def main():
    print("\033[92mStarting FuelTrack AI...\033[0m")
    
    root_dir = os.path.dirname(os.path.abspath(__file__))
    client_dir = os.path.join(root_dir, "client")
    
    # Check if we're in a virtual environment
    in_venv = sys.prefix != sys.base_prefix
    if not in_venv:
        print("\033[93mWarning: You don't seem to be running this within a virtual environment.\033[0m")
        print("\033[93mMake sure you have activated your venv and installed dependencies before proceeding.\033[0m")
    
    print("\033[96mStarting FastAPI Backend on http://localhost:8080\033[0m")
    backend_cmd = [sys.executable, "-m", "uvicorn", "server.main:app", "--reload", "--port", "8080"]
    backend_process = subprocess.Popen(backend_cmd, cwd=root_dir)
    
    print("\033[96mStarting Vite Frontend on http://localhost:5173\033[0m")
    npm_path = shutil.which("npm")
    if not npm_path:
        print("\033[91mError: npm is not installed or not in PATH.\033[0m")
        backend_process.terminate()
        sys.exit(1)
        
    frontend_cmd = [npm_path, "run", "dev"]
    frontend_process = subprocess.Popen(frontend_cmd, cwd=client_dir)
    
    print("\033[92mBoth servers started.\033[0m")
    print("Frontend: http://localhost:5173")
    print("Backend:  http://localhost:8080")
    print("Press Ctrl+C to stop both servers.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[91mShutting down servers...\033[0m")
        backend_process.terminate()
        frontend_process.terminate()
        backend_process.wait()
        frontend_process.wait()
        print("\033[92mServers stopped successfully.\033[0m")

if __name__ == "__main__":
    main()
