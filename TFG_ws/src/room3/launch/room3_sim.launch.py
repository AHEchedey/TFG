from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Directorios de paquetes
    gazebo_ros_pkg = get_package_share_directory('gazebo_ros')
    turtlebot4_description_pkg = get_package_share_directory('turtlebot4_description')
    room3_pkg = get_package_share_directory('room3')

    # Ruta al archivo .world que incluye el modelo
    world_path = os.path.join(room3_pkg, 'worlds', 'room3.world')

    # Launch del robot oficial de TurtleBot4
    robot_description_launch = os.path.join(
        turtlebot4_description_pkg,
        'launch',
        'robot_description.launch.py'
    )

    # Lanzar Gazebo con nuestro mundo personalizado
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_pkg, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world_path}.items()
    )

    # Descripción del robot
    robot_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(robot_description_launch),
        launch_arguments={
            'model': 'standard',
            'use_sim_time': 'true',
            'robot_name': 'turtlebot4',
        }.items()
    )

    # Spawnear el robot como entidad
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
        DeclareLaunchArgument('world', default_value=world_path),
        gazebo,
        robot_description,
        TimerAction(period=4.0, actions=[spawn_robot])
    ])
