import speech_recognition as sr
from pocketsphinx import *

r = sr.Recognizer

with sr.Microphone() as source:
    print("coba ngomong")
    audio = r.listen(source)

    try:
        text = r.recognize_sphinx(audio)
        print("kamu mengatakan : ()".format(text))
    except :
        print("gak ke detek")