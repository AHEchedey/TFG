#!/usr/bin/env bash
set -eo pipefail

# 1. Fuente del entorno ROS2
source /opt/ros/humble/setup.bash

#source ~/robot_delivery_app/install/setup.bash

# 2. Lanzar mapa y navegación
echo "[INFO] Lanzando sistema de navegación con mapa..."
ros2 launch turtlebot4_navigation nav2.launch.py map:=~/mapa_11junio_pruebas/initial_map.yaml &
PID_NAV=$!
sleep 5

# 3. Lanzar aplicación de entrega (nodos personalizados)
#echo "[INFO] Lanzando aplicación de entrega..."
#ros2 launch robot_delivery_app delivery_launch.py &
#PID_APP=$!
#sleep 3

# 4. Lanzar Foxglove Bridge para visualización remota
echo "[INFO] Lanzando Foxglove Bridge..."
ros2 launch foxglove_bridge foxglove_bridge_launch.xml &
PID_FOX=$!
sleep 3

echo "[INFO] Sistema en ejecución. Puedes conectarte a Foxglove en http://<IP_ROBOT>:8765"

# Espera a Ctrl+C y termina procesos
trap "echo '[INFO] Terminando procesos...'; kill $PID_NAV $PID_APP $PID_FOX" SIGINT
wait
