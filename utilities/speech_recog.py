# This file will be for speech recognition; that is all i know
import speech_recognition as sr
r = sr.Recognizer()

#opens microphone as a source file
with sr.Microphone() as source:
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)