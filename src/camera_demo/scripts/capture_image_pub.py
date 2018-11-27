#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import Int32


def set_camera(device_id=1):
    cap = cv2.VideoCapture(device_id)
    print("Camera connected")
    return cap


def capture_image(cap):
    ret, frame = cap.read()
    print(frame.shape)
    return frame


def release_camera(cap):
    cap.release()


def main():
    rospy.init_node('image_publisher')

    # define publisher
    pub_width = rospy.Publisher('img_width', Int32)
    pub_height = rospy.Publisher('img_height', Int32)

    # loop and camera settings
    rate = rospy.Rate(2)
    cap = set_camera()
    
    while not rospy.is_shutdown():
        img = capture_image(cap)
        pub_width.publish(img.shape[0])
        pub_height.publish(img.shape[1])
        rate.sleep()
    
    release_camera(cap)

    
if __name__ == '__main__':
    main()



