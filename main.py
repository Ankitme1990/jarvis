import pyttsx3
import datetime
import speech_recognition
import wikipedia
import os
from requests import get
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def Speak(audio):
    print("    ")
    engine.say(audio)
    print("      ")
    engine.runAndWait()


def wish_me():
    hour_variable = int(datetime.datetime.now().hour)

    if hour_variable >= 0 and hour_variable < 12:
        Speak("good morning!")

    elif hour_variable >= 12 and hour_variable < 18:
        Speak("Good Afternoon")

    else:
        Speak("Good Evening")

    Speak("I Am Jarvis Sir. Please tell me how may I help you")


def takecommand():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        Speak("listening")

        r.pause_threshold = 1
        audio = r.listen(source, timeout=18, phrase_time_limit=8)
    try:
        print("recognising...")
        Speak("Recognising")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")

    except Exception as e:
        # print(e)

        print("say that again please")
        Speak("say that again please")
        return "None"
    return query


def task():
    wish_me()
    while True:

        query = takecommand().lower()

        if 'wikipedia' in query:
            Speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)

        elif 'open notepad' in query:
            Speak('Should i type something for you on notepad')
            import automatic
            automatic.auto_type()

        # elif 'save' in query:bye bye
        #     import automatic_sving_a_file
        #     automatic_sving_a_file.auto_save()

        elif 'close notepad' in query:
            subprocess.call(["taskkill", "/f", "/im", "notepad.exe"])



        elif 'calculate' in query:
            path = "C:\\Windows\\System32\\calc.exe"
            os.startfile(path)



        elif 'close calculator' in query:
            subprocess.call(["taskkill", "/f", "/im", "calc.exe"])

        elif 'open adobe reader' in query:
            path = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(path)

        elif 'close adobe reader' in query:
            subprocess.call(["taskkill", "/f", "/im", "AcroRd32.exe"])

        elif 'open command prompt' in query:
            path = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(path)

        elif 'close command prompt' in query:
            subprocess.call(["taskkill", "/f", "/im", "cmd.exe"])

        elif 'play music' in query:
            music_dir = "G:\\ALL VIDEO,S SONG\\hd videos shivam\\"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            Speak(f'your IP address is {ip}')

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            Speak("what should i search on google")
            cm = takecommand().lower()
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open facebook' in query:

            import facebook_login
            facebook_login.auto_log()

        elif 'search youtube' in query:
            query = query.replace("jarvis", "")
            query = query.replace("search youtube", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak('done sir')

        elif 'exit' in query:
            quit()


task()
