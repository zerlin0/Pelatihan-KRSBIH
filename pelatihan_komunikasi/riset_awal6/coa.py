import speech_recognition as sr

r = sr.Recognizer

with sr.Microphone() as source:
    print("ayo bicara ")
    record = r.listen(source)

    try:
        text = r.recognize_google(record)
        print("hasilnya adalah ()".format(text))
    except:
        print("aneh kata katamu")