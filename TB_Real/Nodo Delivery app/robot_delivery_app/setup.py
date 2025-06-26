from setuptools import setup

package_name = 'robot_delivery_app'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # Instala config y launch en share/...
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/turtlebot4_no_menu.yaml']),
        ('share/' + package_name + '/launch', ['launch/delivery_with_core.launch.py']),
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tu_nombre',
    maintainer_email='tu_email@example.com',
    description='Robot delivery app',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'user_interface_node = robot_delivery_app.user_interface_node:main',
        ],
    },
)
