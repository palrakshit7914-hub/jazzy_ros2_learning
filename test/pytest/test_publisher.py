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