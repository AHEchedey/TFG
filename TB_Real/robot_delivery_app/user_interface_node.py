#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class UserInterfaceNode(Node):
    def __init__(self):
        super().__init__('user_interface_node')
        self.publisher_ = self.create_publisher(String, 'delivery_request', 10)
        self.timer = self.create_timer(5.0, self.prompt_user)

    def prompt_user(self):
        destino = input("📦 Introduce destino (ej: mesa1, mesa2, entrada): ")
        msg = String()
        msg.data = destino
        self.publisher_.publish(msg)
        self.get_logger().info(f"Solicitud enviada a: {destino}")

def main(args=None):
    rclpy.init(args=args)
    node = UserInterfaceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

