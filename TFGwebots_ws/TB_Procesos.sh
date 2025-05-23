#!/bin/bash

SIM_DIR="/home/echedey/Desktop/TFG/TFGwebots_ws/simulaciones"
mkdir -p "$SIM_DIR"
N=$(ls -d "$SIM_DIR"/Prueba_* 2>/dev/null | wc -l)
NUEVO_NUM=$((N+1))
BAG_PATH="$SIM_DIR/Prueba_$NUEVO_NUM"

ros2 launch tb4_sim tb4_launcher.py &
PID_WEBOTS=$!
sleep 10

ros2 launch foxglove_bridge foxglove_bridge_launch.xml &
PID_BRIDGE=$!
sleep 3

ros2 launch slam_toolbox online_sync_launch.py use_sim_time:=true &
PID_SLAM=$!
sleep 5

xdg-open "https://studio.foxglove.dev" &

ros2 bag record -s mcap -o "$BAG_PATH" -a &
PID_BAG=$!
sleep 3

ros2 run formas sala

kill $PID_BAG
kill $PID_SLAM
kill $PID_WEBOTS
kill $PID_BRIDGE

echo "Simulación y grabación finalizadas. Archivo guardado en: $BAG_PATH"
