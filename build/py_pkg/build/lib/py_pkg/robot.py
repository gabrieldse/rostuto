#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Robot(Node):
    def __init__(self):
        super().__init__("Robot")
        self.publisher_ = self.create_publisher(Twist, "turtle/cmd_vel", 1)
        self.timer = self.create_timer(0.5,self.publish_cmd)
        self.get_logger().info("demarrage node Robot")

        def publish_cmd(self):
            msg=Twist()
            msg.linear.x=1.0
            msg.angular.z=0.2
            self.publisher_.publish(msg)
        
def main(arg=None):
    rclpy.init(args=args)
    node=Robot()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()