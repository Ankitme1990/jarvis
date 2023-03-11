import os
import pyautogui
import speech_recognition as sr
import subprocess

def auto_type():
    r = sr.Recognizer()
    paused = False
    file_saved = False
    filename = ""
    exit_flag = False

    # Open Notepad using subprocess
    subprocess.Popen(["notepad.exe"])

    while not exit_flag:
        if not paused:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak now!")
                audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print("You said:", text)
                pyautogui.typewrite(text)
                if "pause" in text:
                    paused = True
                    print("Paused.")
                elif "exit" in text or "stop" in text:
                    exit_flag = True
                    print("Exiting from auto_type() function.")
                elif "save" in text:
                    file_saved = True
                    if not filename:
                        # Ask for the filename if it hasn't been set yet
                        print("What should I name the file?")
                        filename = input()
                        print("File will be saved as:", filename)
                    pyautogui.hotkey('ctrl', 's')
                    pyautogui.typewrite(filename)
                    pyautogui.press('enter')
                    print("File saved as:", filename)
            except sr.UnknownValueError:
                print("Could not understand audio.")
