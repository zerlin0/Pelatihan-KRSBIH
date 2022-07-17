import socket
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
import time
import pyttsx3

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP = "192.168.137.202" #IP Celeh hotspot1
IP = "192.168.4.5"
PORT = 9939
client.connect((IP,PORT))

ngomong = ""
def kirim_pesan(message):
    pesan = message
    pesan.encode('utf-8')
    client.send(pesan)

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

class Init():
    def __init__(self):
        # # rospy.Subscriber("/KRSBI/Signal_Processing/Listening", Int8, recording_Callback)
        self.sub_takscontrol = rospy.Subscriber("/KRSBI/Comm/Talking", String, self.taskcontrol_Callback)
        self.pub_tone = rospy.Publisher("/KRSBI/Comm/Talking/Tone", String, queue_size=10)
        self.talkingState = rospy.Subscriber("/KRSBI/Comm/SaklarTalk", Bool, self.talkingState_Callback)
        time.sleep(1)

        self.talkingStatus = 0

    #callback task control lkr
    def taskcontrol_Callback(self, data):
        global ngomong
        ngomong = data.data
        self.pub_tone.publish(data)
        time.sleep(0.1)

    #callback talking state
    def talkingState_Callback(self, talkingState):
        if talkingState.data == True:
            self.talkingStatus = 1 #HIGH
        elif talkingState.data == False:
            self.talkingStatus = 0 #LOW

def Ticks():
    ticking = int(time.time() * 1000)
    return ticking

if __name__ == '__main__':

    print("Starting Talking")
    while not rospy.is_shutdown():
        try:

            rospy.init_node("Talker", anonymous=False)
            inisialisasi = Init()
            timerResetTalking = Ticks()
            time.sleep(1)
            # print("STARTING TALKING")
            # ros = rospy.Rate(10)
            while True:
                if inisialisasi.talkingStatus == 1:
                    #hanya testing
                    # ngomong = ""
                    if ngomong == "maju":
                        kirim_pesan("maju")
                        inisialisasi.pub_tone.publish('0')
                        talk("robot3 go and find the ball")
                    elif ngomong == "mundur":
                        kirim_pesan("mundur")
                        inisialisasi.pub_tone.publish('1')
                        talk("robot3 go backward and defense")
                elif inisialisasi.talkingStatus == 0 and Ticks() - timerResetTalking >= (60 * 1000):
                    continue
                break
        except rospy.ROSInterruptException:
            rospy.logerr("ROS Interrupt Exception! Just ignore the exception!")
        except rospy.ROSTimeMovedBackwardsException:
            rospy.logerr("ROS Time Backwards! Just ignore the exception!")