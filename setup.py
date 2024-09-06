import subprocess
import sys
import os

required_packages = [
    'pyttsx3',
    'vosk',
    'pyaudio',
    'pynput',
    'tkinter'
]

def install(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}. Please install it manually using pip.")
        sys.exit(1)

def check_pip():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    if not check_pip():
        print("pip is not installed. Please install pip and run this script again.")
        print("You can install pip by following instructions at https://pip.pypa.io/en/stable/installation/")
        sys.exit(1)
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} not found. Installing...")
            install(package)
        else:
            print(f"{package} is already installed.")

if __name__ == "__main__":
    main()
