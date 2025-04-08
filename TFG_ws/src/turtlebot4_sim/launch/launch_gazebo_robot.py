from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Paths
    gazebo_launch = os.path.join(
        get_package_share_directory('gazebo_ros'),
        'launch',
        'gazebo.launch.py'
    )
    world_path = '/home/echedey/Desktop/TFG/room3/room3_turtlebot4.world'

    # Launch Gazebo with your custom world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch),
        launch_arguments={
            'world': world_path,
            'gui': 'true'  # Cambiar a 'false' si quieres sin interfaz gráfica
        }.items()
    )

    # Process the XACRO file from your custom description package
    robot_description_content = Command([
        'xacro ',
        os.path.join(
            get_package_share_directory('turtlebot4_custom_description'),
            'urdf',
            'standard',
            'turtlebot4.urdf.xacro'
        )
    ])
    robot_description = {'robot_description': robot_description_content}

    # Robot State Publisher
    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[robot_description],
        output='screen'
    )

    # Spawn the robot in Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'turtlebot4',
            '-x', '0', '-y', '0', '-z', '0.1'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_pub,
        spawn_entity
    ])

