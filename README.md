# SLAM-Graduation-Project  
### rplidar ROS WIKI : http://wiki.ros.org/rplidar  
### rplidar repository source: https://github.com/robopeak/rplidar_ros
### hector slam ROS WIKI : http://wiki.ros.org/hector_slam  
### hector slam repository: https://github.com/tu-darmstadt-ros-pkg/hector_slam  
  
  
  
Simultaneous localization and mapping using RPLIDAR connected to raspbeery pi with ROS  
  
  
## Steps to run it:  
1. Clone this repository in the src directory of the Catkin Workspace  
2. Build your workspace using catkin_make (Better using -j2 and enabling swap)  
3. Run roslaunch rplidar_ros rplidar.launch  
4. Run roslaunch hector_slam_launch tutorial.launch  
  
  
The Map should start build on Rviz on your screen  
  
  
  
## How to enable swap in ubuntu 16.04:  
https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-16-04
