#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

# when I do the ros2 run py_pkg sub sugested subs_callback -> subs_callbak a la ligne 12

class PosNode(Node):
    def __init__(self):
        super().__init__("subs")
        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.subs_callbak, 1)
        self.get_logger().info("coucou node subs")

    def subs_callbak(self,msg):
        self.get_logger().info("\nX="+str(msg.x)+"\nY="+str(msg.y)+"\n---\n")

def main(args=None):
    rclpy.init(args=args)
    node=PosNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()