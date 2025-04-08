from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'gazebo',
                '--verbose',
                '/home/echedey/Desktop/TFG/room3/room3_turtlebot4.world'
            ],
            output='screen'
        )
    ])
