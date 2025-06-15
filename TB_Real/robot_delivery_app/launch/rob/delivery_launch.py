from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2',
            output='screen',
            parameters=['../config/nav2_params.yaml'],
            arguments=['map:=../maps/initial_map.yaml']
        ),
        Node(
            package='robot_delivery_app',
            executable='delivery_node.py',
            name='delivery_node',
            output='screen'
        ),
        Node(
            package='robot_delivery_app',
            executable='user_interface_node.py',
            name='user_interface_node',
            output='screen'
        )
    ])

