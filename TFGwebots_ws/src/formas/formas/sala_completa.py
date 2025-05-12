import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class RectangleDrawer(Node):
    def __init__(self):
        super().__init__('rectangle_drawer')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        # Lados del rectángulo en el orden de movimiento
        self.side_lengths = [2.0, 5.0, 2.0, 5.0]  # metros

        # Velocidades
        self.linear_speed = 0.2   # m/s
        self.angular_speed = 0.5  # rad/s

        # 90 grados en radianes
        self.turn_angle = 1.5708  

    def move_straight(self, distance: float):
        twist = Twist()
        twist.linear.x = self.linear_speed
        duration = distance / self.linear_speed
        end_time = self.get_clock().now().nanoseconds / 1e9 + duration
        while self.get_clock().now().nanoseconds / 1e9 < end_time:
            self.publisher_.publish(twist)
            rclpy.spin_once(self, timeout_sec=0.1)
        # Detener
        twist.linear.x = 0.0
        self.publisher_.publish(twist)

    def turn_right(self, angle: float):
        twist = Twist()
        twist.angular.z = -self.angular_speed  # negativo = giro a la derecha
        duration = angle / self.angular_speed
        end_time = self.get_clock().now().nanoseconds / 1e9 + duration
        while self.get_clock().now().nanoseconds / 1e9 < end_time:
            self.publisher_.publish(twist)
            rclpy.spin_once(self, timeout_sec=0.1)
        # Detener
        twist.angular.z = 0.0
        self.publisher_.publish(twist)

    def draw_rectangle(self):
        for distance in self.side_lengths:
            self.move_straight(distance)
            time.sleep(0.5)               # pequeña pausa
            self.turn_right(self.turn_angle)
            time.sleep(0.5)

def main(args=None):
    rclpy.init(args=args)
    node = RectangleDrawer()
    time.sleep(2)  # esperar a que el publisher se conecte
    node.draw_rectangle()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
