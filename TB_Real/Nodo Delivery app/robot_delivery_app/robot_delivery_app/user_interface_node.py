#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from turtlebot4_msgs.msg import UserButton, UserDisplay
from nav2_msgs.action import NavigateToPose
import math
import tf_transformations

MAX_LEN = 16

def _fit(s):
    return s[:MAX_LEN].ljust(MAX_LEN)

def yaw_to_quaternion(yaw):
    q = tf_transformations.quaternion_from_euler(0, 0, yaw)
    return q

class DeliveryHMI(Node):
    def __init__(self):
        super().__init__('user_interface_node')

        # Estado
        self.menu = ['Ubicaciones', 'Agregar']
        self.cursor = 0
        self.state = 'main'  # o 'listado'
        self.locations = []
        self.pose = None

        # Subscripciones y publicaciones
        self.create_subscription(UserButton, '/hmi/buttons', self.on_buttons, qos_profile_sensor_data)
        self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.on_pose, 10)
        self.pub_disp = self.create_publisher(UserDisplay, '/hmi/display', 10)
        self.nav_client = ActionClient(self, NavigateToPose, '/navigate_to_pose')

        self.push_menu()

    def on_pose(self, msg):
        self.pose = msg.pose.pose

    def push_menu(self):
        self.state = 'main'
        msg = UserDisplay()
        msg.entries = [''] * 5
        msg.entries[0] = _fit('Delivery App')
        msg.entries[2] = _fit(self.menu[0])
        msg.entries[3] = _fit(self.menu[1])
        msg.selected_entry = 2 + self.cursor
        self.pub_disp.publish(msg)

    def push_empty_locations(self):
        msg = UserDisplay()
        msg.entries = [''] * 5
        msg.entries[0] = _fit('Lista vacía')
        msg.entries[2] = _fit('(Atras para volver)')
        msg.selected_entry = -1
        self.pub_disp.publish(msg)

    def push_locations_menu(self):
        self.state = 'listado'
        msg = UserDisplay()
        msg.entries = [''] * 5
        msg.entries[0] = _fit('Ubicaciones')
        for i, loc in enumerate(self.locations[:4]):
            msg.entries[i+1] = _fit(loc['name'])
        msg.selected_entry = 1 + self.cursor
        self.pub_disp.publish(msg)

    def on_buttons(self, m):
        up, down, ok, back = m.button

        if self.state == 'main':
            if up:
                self.cursor = (self.cursor - 1) % len(self.menu)
                self.push_menu()
            elif down:
                self.cursor = (self.cursor + 1) % len(self.menu)
                self.push_menu()
            elif ok:
                if self.cursor == 0:
                    if not self.locations:
                        self.push_empty_locations()
                    else:
                        self.cursor = 0
                        self.push_locations_menu()
                else:
                    self.save_current_location()
            elif back:
                self.push_menu()

        elif self.state == 'listado':
            if up:
                self.cursor = (self.cursor - 1) % len(self.locations)
                self.push_locations_menu()
            elif down:
                self.cursor = (self.cursor + 1) % len(self.locations)
                self.push_locations_menu()
            elif ok:
                self.navigate_to(self.locations[self.cursor])
            elif back:
                self.cursor = 0
                self.push_menu()

    def save_current_location(self):
        if not self.pose:
            self.get_logger().warn('No pose available')
            return

        x = self.pose.position.x
        y = self.pose.position.y

        # Extrae yaw del quaternion
        q = self.pose.orientation
        _, _, yaw = tf_transformations.euler_from_quaternion([q.x, q.y, q.z, q.w])

        self.locations.append({
            'name': f'Punto_{len(self.locations)+1}',
            'x': x,
            'y': y,
            'yaw': yaw
        })
        self.get_logger().info(f'Ubicación guardada: Punto_{len(self.locations)}')
        self.push_menu()

    def navigate_to(self, location):
        if not self.nav_client.wait_for_server(timeout_sec=2.0):
            self.get_logger().error('Nav2 no disponible')
            return

        goal = NavigateToPose.Goal()
        goal.pose.header.frame_id = 'map'
        goal.pose.header.stamp = self.get_clock().now().to_msg()
        goal.pose.pose.position.x = location['x']
        goal.pose.pose.position.y = location['y']

        q = yaw_to_quaternion(location['yaw'])
        goal.pose.pose.orientation.x = q[0]
        goal.pose.pose.orientation.y = q[1]
        goal.pose.pose.orientation.z = q[2]
        goal.pose.pose.orientation.w = q[3]

        self.get_logger().info(f'Navegando a {location["name"]}')
        self.nav_client.send_goal_async(goal)


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(DeliveryHMI())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
