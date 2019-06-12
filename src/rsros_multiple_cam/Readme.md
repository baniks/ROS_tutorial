realsense_subsriber subscribes to two realsense camera topics /cam_1/color/image_raw/compressed and /cam_2/color/image_raw/compressed and saves the frames in .bag files.
<br>The clean up logic is not working so far.
<br>Output bag files can be converted to images or video files for further processing using [bag_tools](http://wiki.ros.org/bag_tools).
<br>Reindex the .bag file using rosbag reindex \<bag_file_name\>
<br>From bag_tools scripts directory run make_video.py to convert .bag to video
<br>python make_video.py topic_name bag_filename --output output_path
