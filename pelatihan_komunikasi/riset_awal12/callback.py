import rospy
from std_msgs.msg import Int8
import time

recording = 0

pub_ngomong = rospy.Publisher("Talking", Int8, queue_size = 1)

def init():
    rospy.init_node("TaskControl", anonymous=False)


ngomong_nol = 1

def talking(data):
    pub_ngomong.publish(data)
    time.sleep(1)

if __name__ == '__main__':

    try:

        init()
        while not rospy.is_shutdown():
            talking(ngomong_nol)
            print("tone 0")
    except rospy.ROSInterruptException():
        pass