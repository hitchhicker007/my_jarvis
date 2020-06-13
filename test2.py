# import pyttsx3 as p

# engine = p.init()
# voices = engine.getProperty("voices")
# engine.setProperty("voice",voices[0].id)

# engine.say("hello, how are you doing?")
# engine.runAndWait()
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 150) 
engine.setProperty('volume', 1) 
engine.setProperty('voice',voices[1].id) 

# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()

engine.say("hey hitch hicker. i love you")
# engine.say("what is your name?")
engine.runAndWait()