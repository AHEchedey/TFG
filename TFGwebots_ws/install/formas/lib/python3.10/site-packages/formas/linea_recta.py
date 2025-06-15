#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import sys
import random
import os

class LineDrawer(Node):
    def __init__(self, distance: float, ruido_activo: bool):
        super().__init__('line_drawer')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.odom_sub_ = self.create_subscription(
            Odometry, '/odom', self.odom_callback, 10)

        # Parámetros de movimiento
        self.distance = distance
        self.linear_speed = 0.2   # m/s
        self.dt = 0.1             # intervalo de control (segundos)
        self.ruido = ruido_activo
        self.noise_sigma = 0.05   # desviación estándar del ruido 0.03

        self.current_pose = None

    def odom_callback(self, msg: Odometry):
        # Actualiza la última posición
        self.current_pose = msg.pose.pose

    def move_straight(self, distance: float):
        twist = Twist()
        travelled = 0.0
        start_time = self.get_clock().now().nanoseconds / 1e9

        while travelled < distance:
            # Aplica ruido si procede
            noise = random.gauss(0, self.noise_sigma) if self.ruido else 0.0
            twist.linear.x = self.linear_speed + noise
            self.publisher_.publish(twist)

            # Espera y procesa callbacks
            rclpy.spin_once(self, timeout_sec=self.dt)

            # Recalcula distancia recorrida según tiempo
            now = self.get_clock().now().nanoseconds / 1e9
            travelled = (now - start_time) * self.linear_speed

        # Detener el robot
        twist.linear.x = 0.0
        self.publisher_.publish(twist)

    def draw_line(self):
        self.move_straight(self.distance)


def main(args=None):
    rclpy.init(args=args)

    # Valores por defecto
    distancia = 2.0
    modo = 'ruido'

    # Parseo de flags
    for arg in sys.argv[1:]:
        if arg.startswith('--dist='):
            try:
                distancia = float(arg.split('=', 1)[1])
            except ValueError:
                pass
        if arg == '--modo=ideal':
            modo = 'ideal'

    nodo = LineDrawer(
        distance=distancia,
        ruido_activo=(modo != 'ideal')
    )

    # Espera breve para conexiones
    time.sleep(2)
    nodo.get_logger().info(f"Iniciando movimiento en modo {'ideal' if modo=='ideal' else 'ruido'}")
    nodo.draw_line()
    nodo.get_logger().info("Movimiento completado.")

    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

