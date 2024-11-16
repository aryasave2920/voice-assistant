import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am preeti Sir. i love you dhiraj")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            webbrowser.open("https://www.jiosaavn.com/my-music/songs")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

  
        else:
            print("No query matched")

        query = takeCommand().lower()
        if "wake up" in query:  
              speak("Hello sir, how can i help you?")  
        

        query = takeCommand().lower()
        if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break
        elif"hello" in query :
                    speak("Hello sir, How are you?")
        elif"I am fine" in query :
                    speak("That's great ,sir") 
        elif "how are you" in query:
                    speak("I am fine ,sir")
        elif "thank you jarvis" in query :
                    speak("You are welcome ,sir") 
        else:
                    speak("say that again , please")                  












































