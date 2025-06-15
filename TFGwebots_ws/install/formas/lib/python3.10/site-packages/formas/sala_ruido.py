import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import random

class SmoothRectangleDrawer(Node):
    def __init__(self):
        super().__init__('smooth_rectangle_drawer')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        # Lados del rectángulo (m)
        self.side_lengths = [2.0, 5.0, 2.0, 5.0]

        # Velocidades base
        self.linear_speed = 0.2
        self.angular_speed = 0.5
        self.turn_angle = 1.5708  # 90 grados

        # Parámetros de ruido
        self.noise_sigma = 0.001
        self.wheel_base = 0.16  # distancia entre ruedas (m)

        # Tiempo de muestreo
        self.dt = 0.1

    def apply_wheel_noise(self):
        noise_left = random.gauss(0, self.noise_sigma)
        noise_right = random.gauss(0, self.noise_sigma)
        v = self.linear_speed + (noise_left + noise_right) / 2.0
        w = (noise_right - noise_left) / self.wheel_base
        return v, w

    def draw_continuous_rectangle(self):
        twist = Twist()
        current_time = self.get_clock().now().nanoseconds / 1e9

        for _ in range(3):  # Repetir vueltas
            for side_length in self.side_lengths:
                # Calcular duración para avanzar recto
                duration_straight = side_length / self.linear_speed
                end_straight = current_time + duration_straight

                while self.get_clock().now().nanoseconds / 1e9 < end_straight:
                    v, w = self.apply_wheel_noise()
                    twist.linear.x = v
                    twist.angular.z = w
                    self.publisher_.publish(twist)
                    rclpy.spin_once(self, timeout_sec=self.dt)

                # Curva suave a la derecha sin detenerse
                duration_turn = self.turn_angle / abs(self.angular_speed)
                end_turn = end_straight + duration_turn

                while self.get_clock().now().nanoseconds / 1e9 < end_turn:
                    v, w = self.apply_wheel_noise()
                    twist.linear.x = v
                    twist.angular.z = -abs(self.angular_speed) + w
                    self.publisher_.publish(twist)
                    rclpy.spin_once(self, timeout_sec=self.dt)

                current_time = end_turn  # avanzar el tiempo base

        # Detención final
        self.publisher_.publish(Twist())

def main(args=None):
    rclpy.init(args=args)
    node = SmoothRectangleDrawer()
    time.sleep(2)
    node.draw_continuous_rectangle()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

