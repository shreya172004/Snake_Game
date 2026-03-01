import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import datetime

engine=pyttsx3.init('sapi5')
voice=engine.getProperty("voices")
engine.setProperty('voice',voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.phrase_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said...{query}\n")
    except Exception :
        print("please say that again")
        speak("please say that again")
        return 'none'
    return query



def greet():
    speak("hello how can i help you")



if __name__=="__main__":
    greet()
    while True:
        query=takeCommand().lower()

        if 'shreya' in query:
            speak("hello shreya you are very beautiful")

        elif 'quit running' in query:
            quit()



    
