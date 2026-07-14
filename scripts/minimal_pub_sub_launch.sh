#!/bin/bash
# Source the ROS2 environment path first
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
#Launch publisher & subscriber nodes with cleanup handling
cleanup(){
    echo "Restarting ROS 2 before shutting down all process..."
    ros2 daemon stop
    sleep 1
    ros2 daemon start
    echo "Terminating all ROS 2-related processes..."
    kill 0
    exit
}

trap 'cleanup' SIGINT

# Launch run the publisher node
ros2 run ros2_learning pub.py &
sleep 2 

#Launch the subscriber node
ros2 run ros2_learning py_minimal_subscriber.py &
wait
