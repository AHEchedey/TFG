"""webots_ros2 package setup file."""

from setuptools import setup

package_name = 'tb4_sim'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/tb4_launcher.py']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/tb4_raw.urdf',
    'resource/tb4_webots.xacro',
    'resource/tb4_control.yaml',
    'resource/helper.xacro'
]))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/house.wbt',
]))
data_files.append(('share/' + package_name, ['package.xml']))


setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    author='Echedey',
    author_email='ahechedey@gmail.com',
    maintainer='Echedey Aguilar Hernández',
    maintainer_email='ahechedey@gmail.com',
    keywords=['ROS', 'Webots', 'Robot', 'Simulation', 'Examples'],
    description='TurtleBot4 ROS2 interface for Webots.',
    license='This package is available under the MIT license.',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']
    }
)
