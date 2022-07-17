import socket
# import pyttsx3

# engine = pyttsx3.init()
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = "192.168.4.6"
PORT = 9979

client.connect((IP, PORT))

# def kirimPesan(msg):
#     global pesan
#     pesan = msg
#     pesan.encode('utf-8')
#     client.send(pesan)

# def speakUp(message):
#     ucap = message
#     engine.say(ucap)
#     engine.runAndWait()

while True:
    pesan = raw_input("masukkan pesan: ").encode('utf-8')
    client.send(pesan)
    # kirimPesan("berhenti")
    # speakUp(pesan)