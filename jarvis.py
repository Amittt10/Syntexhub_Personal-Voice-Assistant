import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# -------- TEXT TO SPEECH --------
engine = pyttsx3.init()   # macOS uses nsss
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# -------- WISH --------
def wishMe():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you")

# -------- TAKE COMMAND --------
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except:
        print("Say that again please...")
        return "none"

# -------- MAIN --------
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = "/Users/amit/Music"
            songs = os.listdir(music_dir)
            os.system(f"open '{os.path.join(music_dir, songs[0])}'")

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif 'open code' in query:
            os.system("open -a 'Visual Studio Code'")

        elif 'open Google Photos' in query:
            webbrowser.open("https://photos.google.com")


        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Sir")
            break

        else:
            print("No query matched")
