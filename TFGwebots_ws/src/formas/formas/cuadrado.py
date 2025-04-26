import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareDrawer(Node):
    def __init__(self):
        super().__init__('square_drawer')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.side_length = 1.5  # metros
        self.linear_speed = 0.2  # m/s
        self.angular_speed = 0.5  # rad/s
        self.turn_angle = 1.5708  # 90 grados en radianes

    def move_straight(self, distance):
        twist = Twist()
        twist.linear.x = self.linear_speed
        duration = distance / self.linear_speed
        end_time = self.get_clock().now().seconds_nanoseconds()[0] + duration
        while self.get_clock().now().seconds_nanoseconds()[0] < end_time:
            self.publisher_.publish(twist)
            rclpy.spin_once(self, timeout_sec=0.1)
        twist.linear.x = 0.0
        self.publisher_.publish(twist)

    def turn(self, angle):
        twist = Twist()
        twist.angular.z = self.angular_speed
        duration = angle / self.angular_speed
        end_time = self.get_clock().now().seconds_nanoseconds()[0] + duration
        while self.get_clock().now().seconds_nanoseconds()[0] < end_time:
            self.publisher_.publish(twist)
            rclpy.spin_once(self, timeout_sec=0.1)
        twist.angular.z = 0.0
        self.publisher_.publish(twist)

    def draw_square(self):
        for _ in range(4):
            self.move_straight(self.side_length)
            time.sleep(0.5)
            self.turn(self.turn_angle)
            time.sleep(0.5)

def main(args=None):
    rclpy.init(args=args)
    node = SquareDrawer()
    time.sleep(2)  # Espera a que se conecte el publisher
    node.draw_square()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
