import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initialising Jarvis")
#speak("Initialising Jarvis")
MASTER="Prakhar"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#Speak function will speak string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will wish u as per current time
def wishme():
    hour=int(datetime.datetime.now().hour)
    #print(hour)

    if hour>=0 and hour<12:
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening"+ MASTER)
    
    speak("I am Jarvis. How may I help u ?")

#This function take command from microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language= 'en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that again pls")

#Main Program starts..
speak("Initialising Jarvis...")
wishme()
takeCommand()

