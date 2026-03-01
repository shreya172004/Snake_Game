import pyttsx3  
import speech_recognition as sr  
import wikipedia  
import webbrowser 
import os 
import datetime 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    speak("Hello Shreya! How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        speak("Please say that again...")
        return "none"
    return query


if __name__ == "__main__":
    greet()  
    while True:
        query = takeCommand().lower() 

        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia...")
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open vs code' in query:
            myPath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(myPath)
        
        
        elif 'what is the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {time}")
            speak(f"The time is {time}")
        elif 'functions can you perform' in query:
            functions_list = ["search Wikipedia", "open Google", "open YouTube", "open applications such as VS Code, MS Word, PowerPoint", "and tell the time"]
            functions_str = ", ".join(functions_list)
            speak(f"I can {functions_str}")
        elif 'quit running' in query:
            quit()
        else:
            print("Sorry, this function is not supported at the moment...")
            speak("Sorry, this function is not supported at the moment...")

            quit()





