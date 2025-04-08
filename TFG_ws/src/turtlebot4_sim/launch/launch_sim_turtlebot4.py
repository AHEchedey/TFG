from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution
import os
import xacro

def generate_launch_description():
    # Ruta al mundo
    world_path = '/home/echedey/Desktop/TFG/room3/room3_turtlebot4.world'
    xacro_file = '/opt/ros/humble/share/turtlebot4_description/urdf/standard/turtlebot4.urdf.xacro'

    # Verificación de archivos
    if not os.path.exists(world_path):
        raise FileNotFoundError(f"❌ Mundo no encontrado: {world_path}")
    if not os.path.exists(xacro_file):
        raise FileNotFoundError(f"❌ Xacro no encontrado: {xacro_file}")

    # Procesar XACRO
    robot_description_config = xacro.process_file(xacro_file)
    robot_description = robot_description_config.toxml()

    # Nodo robot_state_publisher
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # Nodo spawn_entity con delay
    spawn_entity = TimerAction(
        period=3.0,  # espera 3 segundos
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                arguments=[
                    '-topic', 'robot_description',
                    '-entity', 'turtlebot4',
                    '-x', '0', '-y', '0', '-z', '0.1'
                ],
                output='screen'
            )
        ]
    )

    # Lanzar Gazebo con el mundo personalizado
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            ])
        ),
        launch_arguments={'world': world_path}.items()
    )

    return LaunchDescription([
        gazebo,
        rsp_node,
        spawn_entity
    ])
