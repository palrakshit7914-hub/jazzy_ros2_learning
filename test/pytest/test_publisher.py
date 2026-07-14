#!/usr/bin/env python3

"""
Test suite for the ros2 minimal publisher node.

This script contains unit tests for verifying the functionality of a minimal ros2 publisher.
It test the node creation, message counter increment, and message content formatting.

---------
Subscription Topics:
    None

Publishing Topic
    /py_example_topic (std_msgs/String): Example message with incrementing counter

:author:Pal
:date: july 15,2026

"""
import pytest
import rclpy
from std_msgs import String
from ros2_learning.pub.py import publisher

def test_publisher_creation():
    """
    Test if the publisher is set correctly.

    This test verifies:
    1. The node name is set correctly.
    2. The publsher object exists.
    3. The topic name is correct.

    :raises: AssertionError if any of the checks fail
    """

    #Initialize ROS2 communication
    rclpy.init()

    try:
        #Create an instance of the publisher node
        node = publisher()

        #Check if the node name is set correctly
        assert node.get_name() == 'publisher_node', "Node name is not set correctly."

        #Check if the publisher object exists
        assert hasattr(node, 'publisher_1'), "Publisher object does not exist."

        #Check if the topic name is correct
        assert node.publisher_1.topic_name == '/py_example_topic'."
    finally:
        #Shutdown ROS2 communication
        rclpy.shutdown()

def test_message_content():
    """
    Test if the message content is formatted correctly.

    This test verifies:
    1. The message content includes the correct counter value.
    2. The message is of type std_msgs/String.

    :raises: AssertionError if any of the checks fail
    """

    #Initialize ROS2 communication
    rclpy.init()

    try:
        #Create an instance of the publisher node
        node = publisher()

        #Simulate a timer callback to generate a message
        node.timer_callback()
        msg = String()

        #Check if the message content includes the correct counter value
        msg.data = f'Hello World: {node.i}'
        assert msg.data == 'Hello World: 5'

        
    finally:
        #Shutdown ROS2 communication
        rclpy.shutdown()