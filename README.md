# Skyrim Voice Controller

This Python project allows you to control certain actions in Skyrim using voice commands. The program utilizes the Vosk speech recognition library, along with PyAudio, Pyttsx3, and Pynput for voice feedback and keyboard control.

## Prerequisites

- Python 3.x
- Vosk Model: You will need a Vosk model for speech recognition (e.g., vosk-model-small-en-us-0.15).

## Installation

### Step 1: Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### Step 2: Install Required Packages

Install the necessary Python packages using pip:

pip install pyttsx3 vosk pyaudio pynput tkinter

If you encounter issues installing pyaudio, you may need to manually install a .whl file for your Python version. Visit the PyAudio page (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and download the appropriate wheel file.

pip install path_to_wheel_file.whl

### Step 3: Download the Vosk Model

1. Go to the Vosk models page (https://alphacephei.com/vosk/models) and download the appropriate model.
2. Extract the model into the same directory as this script.
3. Set the vosk_model variable in the main.py script to the name of the extracted model folder. For example:

vosk_model = "vosk-model-small-en-us-0.15"

## Usage

### Step 1: Open Command Line/Terminal

On Windows:
- Press Win + R, type cmd for Command Prompt or powershell for PowerShell, and press Enter.

On macOS:
- Press Cmd + Space, type Terminal, and press Enter.

On Linux:
- Press Ctrl + Alt + T to open the terminal.

### Step 2: Change Directory

Navigate to the directory where the main.py script and Vosk model are located. For example:

cd path_to_your_directory

### Step 3: Run the Script

Once in the correct directory, run the script:

python main.py

If you're using Python 3, you may need to run it as:

python3 main.py

### Step 4: Interact with the Program

Once the program is running, you can use voice commands to trigger the actions. By default, some of the available commands are:
- "one": Presses F1 and gives voice feedback.
- "two": Presses F2 and gives voice feedback.
- "three": Presses F3 and gives voice feedback.
- "four": Presses F4 and gives voice feedback.
- "terminus": Stops the program.

You can customize these actions by editing the actions and keyword_mappings dictionaries in the main.py script.

## Optional: Voice Feedback

When the script starts, you'll be prompted to choose whether or not you want voice feedback. You can set the play_voice variable to skip this prompt:
- Set play_voice = True for voice feedback.
- Set play_voice = False to disable voice feedback.

### Customizing Actions

To add or modify actions:
1. Add an entry in the actions dictionary, mapping an action name to a lambda function defining what the action does.
2. Add a corresponding entry in the keyword_mappings dictionary, mapping the recognized keyword to the action name.

#### Example:

actions = {
    "action one": lambda: (keyboard.press(Key.f1), keyboard.release(Key.f1), engine.say("Running Action One.")),
}
keyword_mappings = {
    "one": "action one",
}

## Troubleshooting

- pyaudio installation issues: If you get an error when installing pyaudio, download the appropriate .whl file from here (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using pip install path_to_wheel_file.whl.

- Model not found: Ensure that the Vosk model folder (e.g., vosk-model-small-en-us-0.15) is in the same directory as the main.py script.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests!

## License

This project is licensed under the MIT License.
