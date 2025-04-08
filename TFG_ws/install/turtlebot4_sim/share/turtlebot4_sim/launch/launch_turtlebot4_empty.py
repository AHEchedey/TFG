from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro

def generate_launch_description():
    # Archivo XACRO del TurtleBot4
    xacro_file = '/opt/ros/humble/share/turtlebot4_description/urdf/standard/turtlebot4.urdf.xacro'

    if not os.path.exists(xacro_file):
        raise FileNotFoundError(f"No se encuentra el archivo XACRO: {xacro_file}")

    # Procesar URDF desde el XACRO y guardarlo en /tmp
    urdf_file = '/tmp/turtlebot4_tmp.urdf'
    robot_description_config = xacro.process_file(xacro_file)
    with open(urdf_file, 'w') as urdf_out:
        urdf_out.write(robot_description_config.toxml())

    # Gazebo vacío
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        )
    )

    # Publicar TFs del robot
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_config.toxml()}]
    )

    # Spawnear el TurtleBot4 en vacío
    spawn_robot = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=[
                    '-file', urdf_file,
                    '-entity', 'turtlebot4',
                    '-x', '0', '-y', '0', '-z', '0.1'
                ],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot
    ])
