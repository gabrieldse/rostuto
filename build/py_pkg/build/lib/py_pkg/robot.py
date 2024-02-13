#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class Robot(Node):
    def __init__(self):
        super().__init__("Robot")
        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 1)
        self.timer = self.create_timer(0.5,self.publish_cmd)
        self.get_logger().info("demarrage node Robot")

    def publish_cmd(self):
        msg=Twist()
        msg.linear.x=0.9
        msg.angular.z=0.4

        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    node=Robot()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

#command to see map of nodes:  rqt_graph