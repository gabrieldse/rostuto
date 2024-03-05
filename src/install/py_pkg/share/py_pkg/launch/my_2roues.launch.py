from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument,IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import Command,LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
import xacro



def generate_launch_description():
    ld=LaunchDescription()

    #   Avec un XACRO
    xacro_file=os.path.join(get_package_share_directory('py_pkg'),'urdf/my_2roues.urdf.xacro')
    robot_desc=xacro.process_file(xacro_file).toxml()
    
    #   Avec un URDF
    # urdf_path = os.path.join(get_package_share_directory('py_pkg'), 'urdf/my_2roues.urdf')
    # urdf = open(urdf_path).read()
    # with open(urdf, 'r') as infp:
    #     robot_desc = infp.read()  

    rviz=os.path.join(get_package_share_directory('py_pkg'),'urdf/2roues.rviz')

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name='rviz2',
        output='screen',
        arguments=['-d',rviz]
    )


    robot_state_node=Node(
          package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
    
    )
    # Joint state sans interface graphique
    joint_state_node=Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        parameters=[{'robot_description': robot_desc}]
    )

    # Joint state avec GUI : lancer un des 2 seulement
    joint_state_gui_node=Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    ld.add_action(robot_state_node)
   # ld.add_action(joint_state_node) 
    ld.add_action(joint_state_gui_node)
    ld.add_action(rviz_node)




    return ld


