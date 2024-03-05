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
    #gui = LaunchConfiguration('gui')

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
             )


    xacro_file=os.path.join(get_package_share_directory('py_pkg'),'urdf/my_2roues.urdf.xacro')
    robot_desc=xacro.process_file(xacro_file).toxml()
    # urdf_path = os.path.join(get_package_share_directory('py_pkg'), 'urdf/my_2roues.urdf')
    # urdf = open(urdf_path).read()
    # with open(urdf, 'r') as infp:
    #     robot_desc = infp.read()
    

    rviz=os.path.join(get_package_share_directory('py_pkg'),'urdf/2roues_sim.rviz')



    simu = DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true')
            
    
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name='rviz2',
        output='screen',
        arguments=['-d',rviz]
    )
# arguments=["-topic", "/robot_description", "-entity", "robot"]
    spawn_entity=Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=["-topic", "/robot_description", "-entity", "rob1"]
      
    )


    robot_state_node=Node(
          package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc,
            'use_sim_time': True}]
    
    )
    joint_state_node=Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        parameters=[{'robot_description': robot_desc}]
    )

    joint_state_gui_node=Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

  
        
    ld.add_action(spawn_entity)
    ld.add_action(robot_state_node)
    #ld.add_action(gazebo)
    ld.add_action(rviz_node)    

    return ld


