# delivery_node.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String

class DeliveryNode(Node):
    def __init__(self):
        super().__init__('delivery_node')
        self.publisher_ = self.create_publisher(PoseStamped, 'goal_pose', 10)
        self.subscription_ = self.create_subscription(String, 'delivery_request', self.listener_callback, 10)

    def listener_callback(self, msg):
        goal_name = msg.data.lower()
        self.get_logger().info(f'Recibido destino: {goal_name}')

        predefined_goals = {
            'mesa1': (1.0, 1.5, 0.0),
            'mesa2': (2.0, -0.5, 0.0),
            'entrada': (0.0, 0.0, 0.0),
        }

        if goal_name in predefined_goals:
            x, y, theta = predefined_goals[goal_name]
            goal = PoseStamped()
            goal.header.frame_id = 'map'
            goal.header.stamp = self.get_clock().now().to_msg()
            goal.pose.position.x = x
            goal.pose.position.y = y
            goal.pose.orientation.w = 1.0
            self.publisher_.publish(goal)
            self.get_logger().info(f'Enviado objetivo a: {x}, {y}')
        else:
            self.get_logger().warn(f'Objetivo desconocido: {goal_name}')


def main(args=None):
    rclpy.init(args=args)
    node = DeliveryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

