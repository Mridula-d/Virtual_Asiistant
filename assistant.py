import os
import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime

# create engine for text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source, duration=1)
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Sorry, I am having trouble connecting to the internet.")
            return ""

def run_assistant():
    command = take_command()

    if "time" in command:
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    elif "date" in command:
        date = datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system('notepad')

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")

    elif "hey siri" in command:
        query = command.replace("hey siri", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Looking for {query}")
            webbrowser.open(url)
        else:
            speak("Yes, how can I help you?")

    elif "bye" in command or "stop" in command:
        speak("Okay thank you, you may leave")
        return False  # stop loop

    else:
        speak("I am here to assist you. Try saying open YouTube, open Notepad, time, or date.")

    return True

if __name__ == "__main__":
    speak("Hey Buddy! Hi, I am here to assist you.")
    while True:
        if not run_assistant():
            break
