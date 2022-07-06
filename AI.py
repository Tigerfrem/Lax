from sqlite3 import Time
from time import time
from unittest import result
import webbrowser
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import os
import subprocess
import ecapture as ec 
import wolframalpha
import json
import requests

engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.9)
engine.setProperty('voice', voice[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greeting():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello, Good Morning Rachid")
        speak("Hello, Good Morning Rachid")
    elif hour>= 12 and hour<18:
        print("Hello, Good afternoon Rachid")
        speak("Hello, Good afternoon Rachid")
    else:   
        print("Hello, Good evening Rachid")
        speak("Hello, Good evening Rachid")

def takeInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        statement=r.recognize_google (audio, language = 'en-US')
        print(f"you said:{statement}\n")

    except Exception as e:
        speak("Pardon me, please say that again")
        return "None"
    return statement


print("Loading your AI personal assistant: Lax")
speak("Loading your AI personal assistant: Lax")
greeting() 


if __name__=='__main__':
    while True:
        speak("Tell me Rachid, how can I help you today?")
        statement = takeInput().lower()
        if statement==0:
            continue
        if 'goodbye' in statement or 'bye' in statement or 'stop' in statement:
            print('Your personal assistant Lax is shutting down. Good bye Rachid, take care!')
            speak('Your personal assistant Lax is shutting down. Good bye Rachid, take care!')
            break
        #else:
            #speak('I do not have the answer to your question at the moment')
            #print('I do not have the answer to your question at the moment')
            #continue
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        if 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is now open")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is now open")
            #time.sleep(5)
        elif 'open outlook' in statement:
            webbrowser.open_new_tab("outlook.com")
            speak("Outlook is now open")
            time.sleep(5)
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.cnn.com")
            speak('Here are some headlines from cnn')
            time.sleep(6)
        elif 'camera' in statement or 'take a photo' in statement:
            ec.capture(0,"robo camera","img.jpg")
        elif 'search' in statement:
            statement = statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'ask' in statement:
            speak('I have the answers to some questions. So, what do you want to know?')
            question=takeInput()
            app_id="Paste your unique ID here"
            client = wolframalpha.Client('7XUVG9-RUPL2G5EKT')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
