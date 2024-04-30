import subprocess
import os

def create_virtual_environment():
    subprocess.run(["python", "-m", "venv", "venv"])

def activate_virtual_environment():
    if os.name == 'posix':  # For Unix/Linux/Mac
        subprocess.run(["source", "venv/bin/activate"], shell=True)
    elif os.name == 'nt':  # For Windows
        subprocess.run(["venv\\Scripts\\activate.bat"], shell=True)

def install_requirements():
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def add_venv_to_path():
    venv_path = os.path.abspath("venv\\Scripts")
    os.environ["PATH"] += os.pathsep + venv_path

def main():
    create_virtual_environment()
    activate_virtual_environment()
    install_requirements()
    add_venv_to_path()
    print("Setup complete.")

if __name__ == "__main__":
    main()
