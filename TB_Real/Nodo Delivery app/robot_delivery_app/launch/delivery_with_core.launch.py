import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():

    # Ruta ABSOLUTA al YAML
    param_file = os.path.join(
        get_package_share_directory('robot_delivery_app'),
        'config', 'turtlebot4_no_menu.yaml'
    )

    # 1) bring-up oficial + nuestro YAML
    bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot4_bringup'),
                'launch', 'standard.launch.py')),
        launch_arguments={
            'param_file': param_file
        }.items()
    )

    # 2) Nodo de interfaz
    hmi_node = Node(
        package='robot_delivery_app',
        executable='user_interface_node',
        name='delivery_hmi',
        output='screen'
    )

    return LaunchDescription([bringup, hmi_node])
