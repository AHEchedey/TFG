from setuptools import find_packages, setup

package_name = 'room3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 👇 Esto es lo que debes añadir
        ('share/' + package_name + '/launch', ['launch/room3_sim.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='echedey',
    maintainer_email='ahechedey@gmail.com',
    description='Room3 Gazebo simulation with TurtleBot4',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

