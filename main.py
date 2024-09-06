import tkinter as tk
import pyttsx3
from vosk import Model, KaldiRecognizer
import json
import pyaudio
import sys
import os
from pynput.keyboard import Key, Controller

def run_setup():
    subprocess.check_call([sys.executable, 'setup.py'])

run_setup()

# ------------------------------------------------------------------------------------------------------------------
# ----------------------------------------EDIT THESE LINES----------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# The `vosk_model` variable (line 16) should be set to the name of the model directory you are using.
# For example, if you downloaded the "vosk-model-small-en-us-0.15" model, set it like this:
vosk_model = "vosk-model-small-en-us-0.15"

# To download a Vosk model:
# 1. Visit the official Vosk models page: https://alphacephei.com/vosk/models
# 2. Choose and download the model that suits your needs. Models are available in various languages and sizes.
#           For most purposes, the "small" model will be sufficient.
# 3. Extract the downloaded model folder.
# 4. Set the `vosk_model` variable to match the name of the extracted model folder.
#           For example, if the folder is named "vosk-model-small-en-us-0.15", set `vosk_model` to "vosk-model-small-en-us-0.15".
# 5. Ensure this folder is located in the same directory this `main.py` script.

# ------------------------------------------------------------------------------------------------------------------

# You have a downloaded a Vosk model and put it in the same directory as this script. (main.py)
# What now?

# 1. Open the command line or PowerShell
#    - On Windows: Press `Win + R`, type `cmd` for Command Prompt or `powershell` for PowerShell, and press Enter.
#    - On macOS: Press `Cmd + Space`, type `Terminal`, and press Enter.
#    - On Linux: Press `Ctrl + Alt + T` to open the terminal.

# 2. Change the directory to the directory with this script. (main.py)
#    - Use the `cd` command to change the directory. For example:
#           cd Desktop/VoskProject
#    - If you need to move back one directory, use:
#           cd ..
#    - If you need to move into a specific folder, use:
#           cd {folder_name}
#    - To list the files and folders in the current directory:
#      - On macOS/Linux/Powershell: use ls
#      - On Windows Command Prompt: use dir

# 3. Ensure `main.py` and the Vosk model folder are in the directory.
#    - After navigating to the correct directory, run the following command to list the files and folders:
#      - On macOS/Linux: use ls
#      - On Windows: use dir
#    - You should see the `main.py` file and the Vosk model folder (e.g., `vosk-model-small-en-us-0.15`).

# 4. Install the required Python libraries:
#    - Run this command to install the necessary packages:
#           pip install pyttsx3 vosk pyaudio pynput tkinter
#    - If the installation fails for `pyaudio` on Windows, download the appropriate `.whl` file 
#      from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install it with:
#           pip install path_to_wheel_file.whl

# 5. Run the Python script:
#    - Once everything is set up, run the script with:
#           python main.py
#    - If using Python 3 specifically, you might need to use:
#           python3 main.py

# 6. If you encounter any errors:
#    - Check your Python version with:
#           python --version
#    - If necessary, upgrade `pip` with:
#           python -m pip install --upgrade pip

# ------------------------------------------------------------------------------------------------------------------

# Actions dictionary: Customize your actions here
# Each entry in this dictionary maps an action name to a lambda function.
# The lambda function should specify the actions to be performed (e.g., pressing keys, speaking).
# Example:
# "action one": lambda: keyboard.press(Key.f1), keyboard.release(Key.f1), engine.say("Running Action One."))
# - This will press then release the 'f1' key and say "Running Action One."
actions = {
    "action one": lambda: (keyboard.press(Key.f1), keyboard.release(Key.f1), engine.say("Running Action One.")),
    "action two": lambda: (keyboard.press(Key.f2), keyboard.release(Key.f2), engine.say("Running Action Two.")),
    "action three": lambda: (keyboard.press(Key.f3), keyboard.release(Key.f3), engine.say("Running Action Three.")),
    "action four": lambda: (keyboard.press(Key.f4), keyboard.release(Key.f4), engine.say("Running Action Four.")),
    "stop program": lambda: (stop_program()) # If this command does not stop the program, go into the console and double tap CTRL + C to force it to stop.
}

# ------------------------------------------------------------------------------------------------------------------

# Keyword mappings dictionary: Map keywords to action names
# This dictionary maps recognized keywords to the action names defined in the `actions` dictionary.
# When a keyword is recognized, the corresponding action from the `actions` dictionary will be executed.
# Example:
# "one": "action one"
# - When the keyword "one" is recognized, the "action one" lambda function will be called.
# We will need to be aware that the voice recognition is not perfect and may need mutliple keywords.
# Example:
# "two", "to", and "too"
# - Depending on your accent, you may need more and/or different keywords.
# - Always test the commands in the console and see what the voice recognition is getting.
keyword_mappings = {
    "one": "action one",
    "two": "action two",
    "to": "action two",
    "too": "action two",
    "three": "action three",
    "four": "action four",
    "for": "action four",
    "terminus": "stop program",
    "terminals": "stop program"
}

# ------------------------------------------------------------------------------------------------------------------

# To add a new action:
# 1. Add an entry in the `actions` dictionary with a unique action name and a lambda function defining what the action does.
# 2. Add a corresponding entry in the `keyword_mappings` dictionary with the keyword that should trigger this action.

# To remove an action:
# 1. Delete the entry from the `actions` dictionary.
# 2. Remove the corresponding keyword entry from the `keyword_mappings` dictionary.

# To adjust an action:
# 1. Modify the lambda function in the `actions` dictionary.
# 2. Update the `keyword_mappings` dictionary if you also need to change the keyword associated with this action.

# ------------------------------------------------------------------------------------------------------------------

# Configure whether the voice feedback should be played or not.
# Set the `play_voice` variable to control this behavior.

# Options:
# - True: The program will play voice feedback.
# - False: The program will not play voice feedback.
# - None: The program will ask you if you want the voice feedback at start up.

# If you want to bypass the initial window that asks whether to enable voice feedback, 
# you can directly set this variable. For example:
#   - Set `play_voice = True` if you want voice feedback.
#   - Set `play_voice = False` if you do not want voice feedback.
#   - Set `play_voice = None` if you want to be asked at start up.
play_voice = None
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------



# !Warning!
# Stop right there!
# Do not pass Go, do not collect $200. 
# Unless you're a code wizard, leave the section below alone. 
# Changing this might summon code gremlins or cause unexpected chaos.




def press_keybind(keyword):
    print(f"Checking for Keyword: {keyword}")
    action_key = keyword_mappings.get(keyword)

    if action_key:
        action = actions.get(action_key);

        if action:
            print(f"Found Keyword: {keyword}")
            action()
            if play_voice:
                engine.runAndWait()
    
def stop_program():
    print("Goodbye!")       
    exit() 
    
def show_popup():
    global play_voice

    def set_no_voice():
        global play_voice
        play_voice = False
        root.destroy()

    def set_voice():
        global play_voice
        play_voice = True
        root.destroy()

    root = tk.Tk()
    root.title("Skyrim Voice Controller")
    
    label = tk.Label(root, width=100, height=4, text=f"Do you want voice feedback?\nChoosing 'No Voice' will make the system more responsive, as it won't wait for the voice feedback to finish.")                 
    label.pack(padx=10)
    
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10) 
    
    no_voice_button = tk.Button(button_frame, text="No feedback", width=10, height=2, command=set_no_voice)
    no_voice_button.pack(side=tk.LEFT, padx=10) 

    voice_button = tk.Button(button_frame, text="Feedback", width=10, height=2, command=set_voice)
    voice_button.pack(side=tk.LEFT, padx=10) 

    root.mainloop()

if play_voice == None:
    show_popup()
    
engine = pyttsx3.init()

this_dir = os.path.dirname(os.path.abspath(__file__))
current_path = os.path.join(this_dir, vosk_model)


model_path = current_path
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

keyboard = Controller()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

voices = engine.getProperty('voices')
for voice in voices:
    if "Zira" in voice.name:
        engine.setProperty('voice', voice.id)
        break

def listen_for_keyword():
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        recognized_text = json.loads(result).get('text', '')

        words = recognized_text.split()
        
        for word in words:
            press_keybind(word)

if __name__ == "__main__":
    if play_voice is None:
            print("play_voice is not set. Exiting the program.")
            sys.exit()
    else:
        print("I am ready for your commands.")
    
        if(play_voice):
            engine.say("I am ready for your commands.")
            engine.runAndWait()
            
    while True:
        listen_for_keyword()
