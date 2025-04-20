from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    gazebo_pkg = get_package_share_directory('gazebo_ros')
    turtlebot4_description_pkg = get_package_share_directory('turtlebot4_description')
    robot_description_launch = os.path.join(turtlebot4_description_pkg, 'launch', 'robot_description.launch.py')

    # Lanzar Gazebo vacío
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg, 'launch', 'gazebo.launch.py')
        )
    )

    # Lanzar URDF del robot
    robot_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(robot_description_launch),
        launch_arguments={'model': 'standard', 'use_sim_time': 'true'}.items()
    )

    # Spawnear el robot desde el topic robot_description
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'turtlebot4',
            '-x', '0', '-y', '0', '-z', '0.3'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_description,
        TimerAction(period=3.0, actions=[spawn_robot])
    ])
