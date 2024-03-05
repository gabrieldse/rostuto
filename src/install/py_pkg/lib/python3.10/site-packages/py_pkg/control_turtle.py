#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2,pi

def sature(a,b):
    if a>b :
         return b
    if a<-b:
        return -b
    return a

class Robot(Node):
    def __init__(self):
        super().__init__("Robot")
        self.publisher_ = self.create_publisher(Twist,"turtle1/cmd_vel",1)
        # Appel du publish par le timer
        # freq de commande indépendante de la freq du subscriber Pose
        self.timer=self.create_timer(0.1,self.publish_cmd)
        self.get_logger().info("demarrage node Robot")

        self.subscriber_ = self.create_subscription(Pose,"turtle1/pose",self.callback_pose,1)    
        self.pose=Pose(x=0.0,y=0.0,theta=0.0)
        self.cible=Pose()
        self.cible.x=1.0
        self.cible.y=8.0

    def publish_cmd(self):
        msg=Twist()

        #direction de la tortue / cible dans rep absolu  
        theta=atan2(self.cible.y-self.pose.y,self.cible.x-self.pose.x)
        #decalage avec l'orientation de la tortue, amené entre [-pi,pi]
        decalage=(theta-self.pose.theta+pi)%(2.0*pi)-pi
        #distance (norme1) a la cible :
        dist1=abs(self.pose.y-self.cible.y)+abs(self.pose.x-self.cible.x)

        #vitesse lineaire/angulaire en focntiion de decalages
        msg.linear.x=sature(dist1/3,2.0)
        msg.angular.z=sature(decalage,1.0)
        self.get_logger().info("decalage="+str(decalage))
        #Envoie de la commande si on est a plus de 0.1 de la cible
        if abs (dist1>0.1):        
            self.publisher_.publish(msg)

    def callback_pose(self,msg):
        self.get_logger().info("\nX="+str(msg.x)+"\nY="+str(msg.y)+"\n---\n")

        self.pose.x=msg.x
        self.pose.y=msg.y
        self.pose.theta=msg.theta
        
        # On peut appeler le publish a la freq du subscriber
        # et on n'a pas besoin du timer
        #self.publish_cmd()
        


def main(args=None):
    rclpy.init(args=args)
    node=Robot()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()