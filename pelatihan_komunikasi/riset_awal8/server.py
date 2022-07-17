import socket
import time
import rospy
from std_msgs.msg import String

# import pyttsx3

# engine = pyttsx3.init()
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = "192.168.245.166"
PORT = 9979

server.bind((IP,PORT))
server.listen(4)

client, add = server.accept()

def menerima_pesan():
    global nerima
    nerima = client.recv(1034)
    nerima.decode('utf-8')
    # print("mendeteksi", nerima)

def listenToRobot():
    rospy.init_node("Pendengar", anonymous=False)
    pub = rospy.Publisher("/Pelatihan/Comm/Mendengarkan", String, queue_size=1)
    time.sleep(1)
    rospy.loginfo("start listening...")
    while not rospy.is_shutdown():
        kaka = ""
        menerima_pesan()
        rospy.loginfo(nerima)
        kaka = nerima
        if kaka == "maju":
            print("terdeteksi =>", nerima)
            pub.publish("0")
        # elif nerima == 'berhenti':
        #     break

# def speakUp(message):
#     ucap = message
#     engine.say(ucap)
#     engine.runAndWait()

# while True:
#     menerima_pesan()
#     # speakUp("i detect" + nerima)
#     if nerima == 'berhenti':
#         break

if __name__ == '__main__':
    try:
        listenToRobot()
    except rospy.ROSInterruptException:
        pass