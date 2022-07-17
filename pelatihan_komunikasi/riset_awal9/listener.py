#!/usr/bin/python

import socket
import rospy
import time
from std_msgs.msg import Int8
# from std_msgs.msg import Bool
import pyttsx3

from datetime import datetime

saklarState = 0
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP = "192.168.137.208" #IP CELEH HOTSPOT
IP = "192.168.4.6"
PORT = 9979
server.bind((IP,PORT))
server.listen(5)
client, addr = server.accept()

menerima = None
def talk(text):
    # en = "englis_rp"
    engine = pyttsx3.init()
    # rate = engine.getProperty('/*rate')
    # engine.setProperty('rate', 125)
    # # volume = engine.getProperty('volume')
    # # engine.setProperty('volume', 1.0)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', en)
    engine.say(text)
    engine.runAndWait()

def mendengarkan():
    global menerima
    menerima = client.recv(1034)
    menerima.decode('utf-8')
    print("Recive at : ", datetime.now())
    print(menerima)

def saklarTalking_Callback(datum):
    global saklarState
    saklarState = datum.data

def Ticks():
    ticking = int(time.time() * 1000)
    return ticking

def record():
    global menerima
    rospy.init_node("Listener", anonymous=False)
    pub = rospy.Publisher("/KRSBI/Comm/Listener", Int8, queue_size=1)
    rospy.Subscriber("/KRSBI/Comm/Saklar_Listening", Int8, saklarTalking_Callback)
    time.sleep(1)
    print('Starting Listening')
    while not rospy.is_shutdown():
        print("listening.....")
        mendengarkan()
        if saklarState == 1:
            if menerima == 'maju':
                print("going forward")
                pub.publish(1)
                talk("understood")

            elif menerima == 'mundur':
                print("going backward")
                pub.publish(2)
                talk("i will go back")
                # menerima = "stop"
        else:
            pub.publish(3)

        # else :
        #     print("stop")
        #     pub.publish(3)

if __name__ == '__main__':
    try:
        record()
    except rospy.ROSInterruptException:
        pass

