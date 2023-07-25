
# Omega Ω
![](https://github.com/AyanantaDatta/Omega/blob/master/giphy.gif)


Omega is a voice-controlled assistant built in Python that uses various APIs and services to perform tasks based on voice commands. It leverages OpenAI's GPT-3.5 language model for generating responses to user queries.

## Features

- Speech recognition to capture user commands.
- Interaction with OpenAI's GPT-3.5 model for generating responses.
- Opening websites like YouTube, Wikipedia, and Google in the default web browser.
- Playing local music files.
- Telling the current time and date.
- Opening Visual Studio Code or Spotify or any applications.
- Using artificial intelligence to generate responses for specific prompts.


## Dependencies
The project relies on the following dependencies, which you need to install before running the script:

- SpeechRecognition: Library for speech recognition using various APIs (e.g., Google Web Speech API).
- OpenAI: Python library for interacting with OpenAI GPT-3.5.
- pywin32: Required for text-to-speech functionality on Windows (for the say() function).
You can install the dependencies using pip:


```bash
  pip install SpeechRecognition
  pip install openai
  pip install pywin32
```
## Getting Started

- 1.Clone the repository or download the project files.
- 2.Obtain an API key from OpenAI by signing up on their platform.
- 3.Replace "YOUR_OPENAI_API_KEY_HERE" in the script with your actual OpenAI API key.
- 4.Ensure your microphone is working correctly and accessible by the SpeechRecognition library.
- 5.If you are using Windows, make sure you have Visual Studio Code and Spotify installed and added to the system PATH or you can copy the path as required.

## Usage
- Run the `main.py` script using Python:
```bash
  python main.py
```

- Upon starting, the assistant will greet you and await your commands.
- You can issue voice commands or type the prompts directly in the terminal.
- Examples of commands you can use:
- "Open YouTube"
- "Play music"
- "What is the time?"
- "Using artificial intelligence, tell me a joke."
- "Omega Quit"
- "Reset chat history"
## Important Notes

- Ensure you have a stable internet connection for speech recognition and interaction with the GPT-3.5 model.
- The performance of the AI assistant may depend on the quality of your microphone and internet connection.
- Be cautious while granting microphone access to the application.
## Contributions

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
Or,
you can mail me at- ayandatta11@gmail.com
