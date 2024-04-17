import speech_recognition as sr 
import sys
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
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
def Pass(pass_inp):
    
    passs=str(pass_inp)
    pass_inp="optimus"
    

    if passs==str(pass_inp):
        speak("password matched , welcome boss")
    else:
        speak("wait what.....this.. is this is my name?...who the hell are you ,.......Go the fuck off ") 
        sys.exit()  
if __name__=="__main__":
    speak("this system is not for all, so.... say my name")
    passs=takecommand()
    Pass(passs)