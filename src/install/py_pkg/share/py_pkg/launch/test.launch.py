from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	ld=LaunchDescription()
	
	N1_node = Node(
    	package="turtlesim",
    	executable="turtlesim_node"
	)
	N2_node=Node(
    	package="py_pkg",
    	executable="control_turtle"
	)

	ld.add_action(N1_node)
	ld.add_action(N2_node)

	return ld
