#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class publisher(Node):

    def __init__(self):
        super().__init__('publisher_node') #name of a node

        #create a publisher on the topic with queuq size of 10 msg
        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        #initiakised a counter variable for message content
        self.i = 0

    def timer_callback(self):
        """callback function executed periodically by the timer
        """

        #create a new string message obj
        msg = String()
        msg.data = 'Hello World: %d' % self.i

        #publish msg we created above to a topic
        self.publisher_1.publish(msg)

        #log a msg indicating the msg  has been publisher
        self.get_logger().info('publishing: "%s"' % msg.data)

        self.i = self.i + 1

def main(args=None):
    """Main Fuction to start the ros2 2 node
    
    Args:
    args (List , optional): command-line arguments. Default to none.
    """

    rclpy.init(args=args)

    #create an instance of the pub node
    node = publisher()
    rclpy.spin(node)

    #destroy the node explicity
    node.destroy_node()

    #shutdown ros2 communication
    rclpy.shutdown()

if __name__ == '__main__':
    #execute the main function if the script is run directly
    main()