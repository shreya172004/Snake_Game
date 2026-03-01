import pyttsx3  # Importing the pyttsx3 library for text-to-speech conversion
import speech_recognition as sr  # Importing the speech_recognition library for speech recognition
import wikipedia  # Importing the wikipedia library for accessing Wikipedia articles
import webbrowser  # Importing the webbrowser library for opening web browsers
import os  # Importing the os module for interacting with the operating system
import datetime  # Importing the datetime module for working with dates and times

# Initializing the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # Getting the available voices
engine.setProperty('voice', voices[1].id)  # Setting the voice to the second voice in the list

# Function to speak the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def greet():
    speak("Hello Shreya! How may I help you?")

# Function to listen to user commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_threshold = 1  # Setting the phrase threshold for recognizing speech
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognizing speech using Google's speech recognition
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        speak("Please say that again...")
        return "none"
    return query

# Main program execution starts here
if __name__ == "__main__":
    greet()  # Greeting the user
    while True:
        query = takeCommand().lower()  # Taking user command and converting it to lowercase

        # Performing tasks based on user commands
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





