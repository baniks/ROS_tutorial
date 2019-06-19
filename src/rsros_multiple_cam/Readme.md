## realsense_subsriber
It subscribes to two realsense camera topics `/cam_1/color/image_raw/compressed` and `/cam_2/color/image_raw/compressed` and saves the frames in .bag files.
The clean up logic is not working so far.

## post-processing
Output bag files can be converted to images or video files for further processing using [bag_tools](http://wiki.ros.org/bag_tools).
Reindex the .bag file using `rosbag reindex \<bag_file_name\>`
From bag_tools scripts directory, run make_video.py to convert .bag to video
```python make_video.py topic_name bag_filename --output output_path```

## Realsense and ROS interfacing
Follow the instructions for installing [realsense-ros](https://github.com/IntelRealSense/realsense-ros).
Connect the cameras.
Get the serial numbers of the cameras by
```
rs-enumerate-devices | grep Serial`
```
Launch the cameras by
```
roslaunch realsense2_camera rs_camera.launch camera:=cam_1 serial_no:=<serial number of the first camera>
roslaunch realsense2_camera rs_camera.launch camera:=cam_2 serial_no:=<serial number of the second camera>
...
```
To launch only the camera
```
roslaunch realsense2_camera rs_camera.launch camera:=cam_1 serial_no:=<serial number> enable_fisheye:=false enable_depth:=false enable_infra2:=false enable_infra1:=false
```
Run realsense_subscriber.py
