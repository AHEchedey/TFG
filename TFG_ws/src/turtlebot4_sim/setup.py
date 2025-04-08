from setuptools import find_packages, setup

package_name = 'turtlebot4_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/launch_sim_turtlebot4.py',
            'launch/launch_turtlebot4_empty.py',
            'launch/launch_gazebo_robot.py',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='echedey',
    maintainer_email='ahechedey@gmail.com',
    description='Simulación TurtleBot4 con mundo personalizado',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
        'launch': [
            'launch_sim_turtlebot4 = turtlebot4_sim.launch.launch_sim_turtlebot4:generate_launch_description',
            'launch_turtlebot4_empty = turtlebot4_sim.launch.launch_turtlebot4_empty:generate_launch_description',
            'launch_gazebo_robot = turtlebot4_sim.launch.launch_gazebo_robot:generate_launch_description',
        ],
    },
)
