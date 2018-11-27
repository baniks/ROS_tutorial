#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    print msg.data


def main():
    rospy.init_node('image_subscriber')
    sub_width = rospy.Subscriber('img_width', Int32, callback)
    sub_height = rospy.Subscriber('img_height', Int32, callback)
    rospy.spin()
    

if __name__ == '__main__':
    main()
