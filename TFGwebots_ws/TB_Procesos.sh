#!/bin/bash

# Ruta donde guardar las simulaciones
SIM_DIR="/home/echedey/Desktop/TFG/TFGwebots_ws/simulaciones"

# Crear el directorio si no existe
mkdir -p "$SIM_DIR"

# Calcular el siguiente número de prueba
N=$(ls -d "$SIM_DIR"/Prueba_* 2>/dev/null | wc -l)
NUEVO_NUM=$((N+1))
BAG_PATH="$SIM_DIR/Prueba_$NUEVO_NUM"

# 1. Lanzar Webots con la simulación (en segundo plano)
ros2 launch tb4_sim tb4_launcher.py &
PID_WEBOTS=$!
sleep 10  # Ajusta según lo que tarde en arrancar tu simulación

# 2. Comenzar a guardar los datos en ros2 bag (en segundo plano)
ros2 bag record -s mcap -o "$BAG_PATH" -a &
PID_BAG=$!
sleep 3

# 3. Lanzar la simulación del cuadrado (espera a que termine)
ros2 run formas cuadrado

# 4. Parar la grabación del ros2 bag
kill $PID_BAG

# 5. Parar Webots
kill $PID_WEBOTS

# 6. Buscar el último archivo MCAP generado
MCAP_FILE=$(find "$SIM_DIR"/Prueba_* -type f -name "*.mcap" | sort | tail -n 1)

# 7. Abrir Foxglove Studio Online con el archivo MCAP (si existe)
if [ -n "$MCAP_FILE" ]; then
    xdg-open "https://studio.foxglove.dev/open?file=$MCAP_FILE"
else
    echo "No se encontró ningún archivo MCAP para abrir en Foxglove."
fi

echo "Simulación, grabación y apertura de Foxglove finalizadas."
exit 0
