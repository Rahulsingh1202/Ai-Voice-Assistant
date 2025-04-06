import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Genesis Sir. How may I help you")

def takeCommad():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Can you say that again please ?")
        return"None"

    return query    


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommad().lower()

        if 'wikipedia' in query:
            speak("Searching on wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open jay ho' in query:
            webbrowser.open("jayho.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'your name' in query:
            speak("Sir!, my name is Genesis")

        elif "your father" in query:
            speak("As I know , i am developed and programmed by Sir Rahul")
        
        elif 'your age' in query:
            speak("I am programmed on 15 November 2022")
        
        elif 'favourite colour' in query:
            speak("I think, i sometimes like black so much")

        elif 'can you change' in query:
            speak(" sorry sir i want to...but my creater is not that genius")
        
        elif 'open opera' in query:
            webbrowser.open("opera.com")

        elif 'what are you' in query:
            speak("i am an A I voice assistant")

        else:
            speak(" ")




