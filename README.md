🗣️ Virtual Voice Assistant

A Python-based virtual voice assistant that can understand voice commands and respond using speech. This assistant uses speech recognition and text-to-speech to make human-computer interaction easier and more natural.

🚀 Features

🎤 Voice Command Recognition – Listens to user input through the microphone.

🗣️ Text-to-Speech (TTS) – Responds to commands with speech.

⏰ Tells Time & Date – Provides the current time and today’s date.

📝 Open Applications – Can open Notepad or other applications.

📺 Open Websites – Opens YouTube or any requested site in the browser.

🔍 Google Search – Performs quick Google searches using voice queries.

👋 Exit Gracefully – Stops running when the user says "bye" or "stop".

🛠️ Tech Stack

Python 3.8+

pyttsx3
 – Text-to-speech conversion library

SpeechRecognition
 – Speech-to-text conversion

PyAudio
 – Capturing voice input from the microphone

Webbrowser module – To open websites

OS module – To launch system applications

📦 Installation

Clone this repository or download the script:

git clone https://github.com/your-username/virtual-assistant.git
cd virtual-assistant


Install required dependencies:

pip install pyttsx3 SpeechRecognition pyaudio


Run the assistant:

python assistant.py

🎯 Usage

Start the assistant, and it will greet you.

Speak commands like:

"time" → Tells the current time

"date" → Tells today’s date

"open notepad" → Opens Notepad

"open youtube" → Opens YouTube in browser

"hey siri cats" → Searches Google for "cats"

"bye" / "stop" → Exits the assistant

📌 Future Improvements

Add weather updates 🌤️

Play local music or videos 🎶

Integrate with APIs (e.g., news, calendar, email)

More voice commands and personalization
