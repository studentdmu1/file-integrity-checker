import os
import subprocess

def run_frontend():
    venv_python = os.path.join("venv", "Scripts", "python.exe")
    subprocess.Popen([venv_python, "-m", "streamlit", "run", "frontend-main/main.py"])

def run_backend():
    venv_python = os.path.join("venv", "Scripts", "python.exe")
    subprocess.Popen([venv_python, "-m", "uvicorn", "backend-main.app.main:app", "--reload"])

def main():
    run_frontend()
    run_backend()

if __name__ == "__main__":
    main()
