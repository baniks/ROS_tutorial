# Python libs
import sys, time

# numpy and scipy
import numpy as np

# Ros libraries
import roslib
import rospy
import rosbag

# Ros Messages
from sensor_msgs.msg import CompressedImage


class image_feature:

    def __init__(self):
        # subscribed Topic
        self.bag1 = rosbag.Bag('/tmp/test1.bag', 'w')
        self.bag2 = rosbag.Bag('/tmp/test2.bag', 'w')
        self.subscriber1 = rospy.Subscriber("/cam_1/color/image_raw/compressed", CompressedImage, self.callback1,  queue_size = 1)
        self.subscriber2 = rospy.Subscriber("/cam_2/color/image_raw/compressed", CompressedImage, self.callback2,  queue_size = 1)
        print("subscribed to /cam_1/image/compressed and /cam_2/image/compressed")


    def __del__(self):
        print("Cleaning up")
        self.bag1.close()
        self.bag2.close()


    def callback1(self, ros_data):
        '''Callback function of subscribed topic. 
        Here images get converted and features detected'''
        self.bag1.write('/cam_1/color/image_raw/compressed',ros_data)
        print('sub1: bag file written')
        # Check http://docs.ros.org/melodic/api/sensor_msgs/html/msg/Image.html to see message format
                
    def callback2(self, ros_data):
        '''Callback function of subscribed topic. 
        Here images get converted and features detected'''
        self.bag2.write('/cam_2/color/image_raw/compressed', ros_data)
        print('sub2: bag file written')


def main(args):
    rospy.init_node('image_feature', anonymous=True)
    try:
        im_f = image_feature()
        rospy.spin()
    except KeyboardInterrupt:
        self.bag1.close()
        self.bag2.close()
        print("Shutting down ROS Image feature detector module")

if __name__ == '__main__':
    main(sys.argv)


