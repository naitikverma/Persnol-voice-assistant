import pyttsx3
import datetime
import wikipedia
import sys
import webbrowser
import os
import pyjokes
import pyautogui
import random
import wolframalpha
import speech_recognition as sr
from password import Pass
from time import sleep
from pyautogui import click
from keyboard import write
from keyboard import press
from keyboard import press_and_release

app = wolframalpha.Client("75PQK7-QXUYK85EL9")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0 ].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("may i help you boss?")
def tellday():
    day=datetime.datetime.today().weekday()+1
    Day_dict={1:"Monday",2:"Tuesday",3:"Wednsday",4:"Thruday",5:"Friday",6:"Satuarday",7:"Sunday"}
    if day in Day_dict.keys():
        day_of_the_week=Day_dict[day]
        print(day_of_the_week)
        speak("the day is"+day_of_the_week)\
        
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")   
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query=r.recognize_google(audio,language="en-in")  
        print(query)
    except Exception as e:
        print(e)
        return "None"
    query=query.lower()
    return query
#def TaskExicution():
if __name__=="__main__":
    speak("this system is not for all, so.... say my name")
   # passs=takecommand()
    passs= input("Enter the name.....?")
    Pass(passs)
    wishMe()
    tellday()
    speak("this is optimus")
    while True:
        query = takecommand()
        if "wikipedia" in query.lower():
            speak("Sure")
            speak("searching wikipidea")
            query=query.replace("wikipidea","")
            results = wikipedia.summary(query,sentences =2)
            speak("according to wikipidea...")
            print(results)
            speak(results)
            speak("i am optimus, please tell me how may i help you ")
        if ".com" in query or ".co.in" in query or ".org" in query or ".nic.in" in query:
            query=query.replace("open","")
            query=query.replace("open","")
            query=query.replace("search","")
            query=query.replace(" ","")
            speak("opening sir.....")
            webbrowser.open(f"https://www.{query}")
        elif "open google" in query:
            speak("sir! what should i search on it")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("sir hear is your result")
        elif "open window" in query:
            speak("opening window...")
            pyautogui.hotkey("win")
            sleep(0.5)
            speak("which application should i open sir...?")
            cm=takecommand()
            write(f"{cm}")
            speak("opening...")
            pyautogui.hotkey("enter")
            print(cm)
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
            speak("here is the result")

        elif "open bluetooth" in query:
            speak("opening bluetooth")
            pyautogui.click(x=1640, y=1027)
            sleep(1)
            pyautogui.click(x=1659, y=381)
            sleep(0.5)
            pyautogui.click(x=1837, y=331)
            sleep(0.8)
            pyautogui.click(x=1640, y=1027)
        elif "close bluetooth" in query:
            speak("closing bluetooth")
            pyautogui.click(x=1640, y=1027)
            sleep(1)
            pyautogui.click(x=1659, y=381)
            sleep(0.5)
            pyautogui.click(x=1837, y=331)
            sleep(0.8)
            pyautogui.click(x=1640, y=1027)
        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/")
            speak("here is the result")
        elif "open whatsapp in browser" in query:
            speak("opening whatsapp")
            webbrowser.open("https://www.whatsapp.com/")
            speak("here is the result")
        elif "open whatsapp" in query:
            speak("opening whatsapp")
            pyautogui.click(x=1225, y=1047)
            speak("here is the result")
        elif "open reddit" in query:
            speak("opening reddit")
            webbrowser.open("https://www.reddit.com")
            speak("here is the result")
        elif "open notepad" in query: 
            speak("opening notepade")
            apath="C:\\Users\\NAITIK\\OneDrive\\Documents\\notepad.txt"
            os.startfile(apath)
            speak("here is your notepad")
        elif "open cmd" in query.lower():
            speak("opening CMD") 
            os.system("start cmd")
            speak("here is the result")
        
        elif "play music" in query:
            speak("playing music")
            music_dir ="D:\\music"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
            speak("here is your music enjoy sir")
        elif "change music" in query:
            speak("ok sir")
            music_dir ="D:\\music"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
        elif "play my music on youtube" in query:
            speak("sure sir")
            webbrowser.open("https://youtu.be/1sRaLqtHXQU?si=GZYf6d8hrw60EFhI")
            speak(" here is the result ")
        elif "new tab" in query :
            pyautogui.hotkey('ctrl','t')
            speak("here is the your new tab")
        elif "close the tab"in query:
            pyautogui.hotkey('ctrl','w')
            speak ("ok sir.....")
        elif "close all tab"in query:
            pyautogui.hotkey('ctrl','w')
            sleep(0.5)
            pyautogui.hotkey('ctrl','w')
            sleep(0.5)
            pyautogui.hotkey('ctrl','w')
            speak ("closing the tab sir.....")
        elif "restore the window" in query:
            pyautogui.hotkey('win','d')
            speak("window is restored")
        elif "minimise the window" in query:
            pyautogui.hotkey('win','d')
            speak("window is minimised")
        elif "volume up" in query:
            pyautogui.hotkey('volumeup')
            speak("ok")
        elif "restart system" in query:
            os.system("shutdown/r /t 0")
        elif "shutdown system" in query:
            os.system("shutdown /s /t 0")
            speak("system is shuting down")
        elif "sleep system" in query:
            os.system("sleep /s /t 0.5")
            speak("system is sleeping down")
        elif "volume down" in query:
            pyautogui.hotkey('volumedown')
            speak("ok sir")
        elif "mute the system" in query:
            speak("as you wish boss, but then you can't hear me")
            pyautogui.hotkey('volumemute')
        elif "tell me a joke" in query:
            speak("ok sir")
            jokes=pyjokes.get_joke()
            speak(jokes)
            print(jokes)
        elif "tell me time" in query:
            speak("ok")
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)
        elif "calculate" in query:
            speak("what should i calculate, sir")
            query = takecommand()
            #query = input(" Enter the query: ")
            res=app.query(query)
            speak(next(res.results).text)
            print(next(res.results).text)
        elif 'open camera' in query.lower():
            pyautogui.click(x=577, y=1054)
            write('camera')
            press('enter')
            speak('here is your camera')
        elif'new tab' in query.lower(): 
            press_and_release('ctrl+t')
        elif 'close tab' in query.lower():
            press_and_release('ctrl+w')
        elif 'new window' in query.lower():
            press_and_release('ctrl+n')
        elif"history" in query.lower(): 
            press_and_release('ctrl+h')
        elif 'download' in query.lower():
            press_and_release('ctrl+j') 
        elif'bookmark' in query.lower():
            press_and_release('ctrl+d') 
            press('enter')
        elif 'incognito' in query.lower(): 
            press_and_release('ctrl+shift+n')
        elif "open browser" in query:
            speak("ok opening browser, Boss what you want to search ")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("here is the result")
        elif "take a screenshot" in query:
            pyautogui.hotkey('win','prtsc')
            speak("takeing screenshot")
        
        elif "good night bro" in query:
            speak("time for sleep thank you..... boss, you can call me any time")
            sys.exit()
