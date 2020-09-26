import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import smtplib
import subprocess 
import requests
import wikipedia
import ctypes
import time

engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def timeda():
    Time = datetime.datetime.now().strftime("%I:%M:%S")   
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)    
    month = int(datetime.datetime.now().month) 
    date = int(datetime.datetime.now().day) 
    speak(date)
    speak(month)
    speak(year)
    
def check():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour <12:
        speak("Good Morning ")
    elif hour >=12 and hour <18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")
            
def greetings():
    check()
    speak("Welcome back,Sir. Mark here")
    speak("Let me know what can i do for you sir!!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sunnykumar12928@gmail.com', '25929031')
    server.sendmail('sunnykumar12928@gmail.com', to, content)
    server.close()

def changeWallpaper():
    imgage=r"C:\Users\91800\Desktop\Mark\image\mark.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20,0,imgage,0)

def changeScreen():
    app = r"C:\Users\91800\Desktop\Mark\Rainmeter\rainmeter.exe"
    os.startfile(app)
    changeWallpaper()
    
speak("Hello;This is Mark ,version1 point o;  Your personal , AI assistant")
speak("Its")
timeda()


while True:
    comm = takeCommand().lower()
    if "hello" in comm:
        greetings()
    elif "open youtube" in comm:
        speak("opening youtube")
        webbrowser.open("www.youtube.com")

    
    elif "close youtube" in comm:
        speak("closing it")
        os.system("taskkill /f /im chrome.exe")

    elif "activate" in comm:
        changeScreen()
        time.sleep(3)

    elif "open college" in comm:
        speak("opening college portal")
        webbrowser.open("https://ipec.codetantra.com/login.jsp")
    
    elif "offline" in comm:
        speak("Starting all application shutdown sequence")
        os.system("taskkill /f /im rainmeter.exe")
        speak("I am going offline,Sir;have a nice day")
        image=r"C:\Users\91800\Dekstop\Mark\image\windows.jpg"
        ctypes.windll.user32.SystemParametersInfoW(20,0,image,0)
        exit()

    elif "shutdown" in comm:
        speak("shutting down;sir,have a nice day")
        os.system('shutdown -s')

    elif 'open gmail' in comm:
        speak('openning gmail')
        webbrowser.open('www.gmail.com')

    elif 'search' in comm:
        speak("Searching...")
        webbrowser.open(comm)
        
    elif "wikipedia" in comm:
        try: 
            speak("Searching on Wikipedia...")
            query = comm.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            speak("Thank You sir ;Anything else i can do for you?")
        except Exception as e:
            speak("There is no results found for it sir ;Anything else i can do for you?")   

    elif 'email to me' and 'send email' in comm:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whom i should send this email")
                to = takeCommand()    
                sendEmail(to, content)
                speak("Email has been sent!")
                speak("Want me to open gmail")
                if "Yes" in comm:
                    webbrowser.open('www.gmail.com')
                else:
                    speak("Thank you sir ,Anthying More sir?")  
            except Exception as e:
                print(e)
                speak("Sorry buddy .I am not able to send this email")
    
    elif "buddy" in comm:
        speak("Yes sir!!")
    
    elif "tell me about you" in comm:
        speak("I am Mark 1 .o created by Mister Aneesh . I have been created on A I M L and can develop with my last mistakes . Want to test me?")

    elif "play some songs" in comm: 
        speak("Opening Songs")
        appli = r"C:\Users\91800\Desktop\Spotify.lnk"
        os.startfile(appli) 

    elif "close it" in comm:
        os.system("taskkill /f /im Spotify.lnk")


    else:
        speak("Can you speak it again,sir")


