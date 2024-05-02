import subprocess
import os
import pyshortcuts  
import sys

def add_venv_to_path():
    venv_path = os.path.abspath("venv\\Scripts")
    os.environ["PATH"] += os.pathsep + venv_path

def create_virtual_environment():
    subprocess.run(["python", "-m", "venv", "venv"])

def activate_virtual_environment():
    if os.name == 'posix':  # For Unix/Linux/Mac
        venv_path = os.path.abspath("venv")
        bin_path = os.path.join(venv_path, "bin")
        os.environ["PATH"] = bin_path + os.pathsep + os.environ["PATH"]

    elif os.name == 'nt':  # For Windows
        venv_path = os.path.abspath("venv")
        os.environ["VIRTUAL_ENV"] = venv_path
        os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]

def install_python_requirements():
    subprocess.run(["pip", "install", "uvicorn", "streamlit"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def create_desktop_shortcut():    
    script_path = os.path.abspath("APP.PY")  # Path to fragiti.py in the same directory
    shortcut_path = os.path.join(os.path.expanduser("~"), "Desktop", "APP")
    start_in_path = os.path.abspath("")
    target_path = ("APP.PY")+'"'
    pyshortcuts.make_shortcut(target_path, shortcut_path, working_dir=start_in_path)
    
def main():
    add_venv_to_path()
    create_virtual_environment()
    activate_virtual_environment()  
    install_python_requirements()  
    create_desktop_shortcut()
    
    print("Setup complete.")

if __name__ == "__main__":
    main()
