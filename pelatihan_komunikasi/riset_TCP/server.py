import socket
import rospy
from std_msgs.msg import String

# import pyttsx3

# engine = pyttsx3.init()
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = "localhost"
PORT = 9979

server.bind((IP,PORT))
server.listen(4)

client, add = server.accept()

def menerima_pesan():
    global nerima
    nerima = client.recv(1034)
    nerima.decode('utf-8')
    print("mendeteksi", nerima)

# def speakUp(message):
#     ucap = message
#     engine.say(ucap)
#     engine.runAndWait()

while True:
    menerima_pesan()
    # speakUp("i detect" + nerima)
    if nerima == 'berhenti':
        break