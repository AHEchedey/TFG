kfrom launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Ruta al mundo SDF personalizado
    declare_world_arg = DeclareLaunchArgument(
        'world',
        default_value=os.path.join(
            get_package_share_directory('room3'),
            'maps', 'room_with_walls_2', 'room3', 'model.sdf'
        ),
        description='Ruta al archivo .sdf del mundo room3'
    )

    world = LaunchConfiguration('world')

    # Ruta al launch de Gazebo
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={'world': world}.items()
    )

    # Ruta al launch de descripción del robot
    robot_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot4_description'),
                'launch',
                'robot_description.launch.py'
            )
        )
    )

    return LaunchDescription([
        declare_world_arg,
        gazebo_launch,
        robot_description_launch
    ])

