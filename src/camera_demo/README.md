# Demo for connecting ROS to a webcam. 
The image_publisher captures images and publishes the width and height. 
The image subscriber subscribes to these informations.

libraries: Opencv, rospy

![alt text](out/rosgraph.png "ROS computation graph (rqt_graph)")
Issue: The graph only shows one published variable, img_width
