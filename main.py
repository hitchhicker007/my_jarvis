import speech_recognition as sr
import pyttsx3 as p 
from web_automations import *

r = sr.Recognizer()
engine = p.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 150) 
engine.setProperty('volume', 1) 
engine.setProperty('voice',voices[1].id) 

engine.say("hello, how are you doing?")
engine.runAndWait()

ply_music = ["play","music"]

while True:
    with sr.Microphone() as source:
        text = r.listen(source)
        try:
            recognized_text = r.recognize_google(text)
            print(recognized_text)
            
            if "play" and "song" in recognized_text:
                engine.say("Please wait, i am playing music for you")
                engine.runAndWait()
                music()
            elif "decrease" and "volume" in recognized_text:
                decrease_volume()
            elif "increase" and "volume" in recognized_text:
                increase_volume()
            elif "stop" or "stop the song" in recognized_text:
                stop_music()
            elif "current time" in recognized_text:
                t=current_time()
                engine.say("the current time is "+t)
                engine.runAndWait()                
            elif "bye" in recognized_text:
                engine.say("Okay, bye bye... have a good day!!")
                engine.runAndWait()
                exit()         
            elif "today" and "date" in recognized_text:
                date=current_date()
                engine.say("Today's date is, " + date)
                engine.runAndWait()   
            recognized_text = ""
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print(e)