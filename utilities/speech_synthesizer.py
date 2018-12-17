import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 100)

engine.say('Hello')
engine.runAndWait()
