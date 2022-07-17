import socket
import rospy
from std_msgs.msg import Int8
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP = "localhost"
PORT = 9979
server.bind((IP,PORT))

def menerima():
    global data
    global addr
    data, addr = server.recvfrom(1024)
    print("menerima dari", addr, "pesan: ", data)

def record():
    rospy.init_node("Listener", anonymous=False)
    pub = rospy.Publisher("/KRSBI/Comm/Listener", Int8, queue_size=1)
    time.sleep(0.1)
    print('Starting Listening')
    while not rospy.is_shutdown():
        print("listening.....")
        menerima()
        if data == 'maju':
            print("going forward")
            pub.publish(1)
        elif data == 'mundur':
            print("going backward")
            pub.publish(2)

if __name__ == '__main__':
    try:
        record()
    except rospy.ROSInterruptException:
        pass
