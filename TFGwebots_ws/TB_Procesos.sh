#!/usr/bin/env bash
set -euo pipefail

# Directorio base para simulaciones
SIM_DIR="$HOME/Desktop/simulaciones"
mkdir -p "$SIM_DIR"

# Generar timestamp con fecha y hora
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BAG_PATH="$SIM_DIR/${TIMESTAMP}"

echo "[INFO] Carpeta de salida: $BAG_PATH"

# 1) Lanzar simulación Webots+ROS2
ros2 launch tb4_sim tb4_launcher.py &
PID_WEBOTS=$!
sleep 10

# 2) Lanzar SLAM
ros2 launch slam_toolbox online_sync_launch.py use_sim_time:=true &
PID_SLAM=$!
sleep 5

# 3) Iniciar grabación de bag (ros2 bag crea $BAG_PATH)
echo "[INFO] Iniciando ros2 bag record..."
ros2 bag record -s mcap -o "$BAG_PATH" -a &
PID_BAG=$!
sleep 3

# 4) Ejecutar el nodo de movimiento
echo "[INFO] Lanzando nodo de movimiento 'linea'..."
#ros2 run formas linea_recta --dist=3
ros2 run formas sala


# 5) Detener procesos que sigan vivos
for pid in "$PID_BAG" "$PID_SLAM" "$PID_WEBOTS"; do
  if ps -p "$pid" > /dev/null 2>&1; then
    echo "[INFO] Matando PID $pid"
    kill "$pid"
  fi
done

echo "[INFO] Simulación y grabación finalizadas."
echo "[INFO] Datos grabados en: $BAG_PATH"

