#!/bin/bash

# Crear carpeta de logs
mkdir -p logs
LOG_FILE="logs/test_$(date +%Y%m%d_%H%M).log"

# Colores
green="\e[32m"
red="\e[31m"
reset="\e[0m"

function log {
  echo -e "$1" | tee -a "$LOG_FILE"
}

log "[TEST] 🧪 Iniciando verificación del TurtleBot4..."

# 1. Verificar Create3 (base)
log "\n[TEST] Verificando conexión con Create 3 (base)..."
if ros2 topic list | grep -q "/wheel_status"; then
  if ros2 topic echo --once /wheel_status > /dev/null 2>&1; then
    log "${green}✅ Create 3 responde${reset}"
  else
    log "${red}❌ Create 3 sin datos${reset}"
  fi
else
  log "${red}❌ Tópico /wheel_status no encontrado${reset}"
fi

# 2. Verificar LIDAR
log "\n[TEST] Verificando LIDAR (RPLIDAR)..."
if ros2 topic list | grep -q "/scan"; then
  if ros2 topic echo --once /scan > /dev/null 2>&1; then
    log "${green}✅ LIDAR activo${reset}"
  else
    log "${red}❌ LIDAR sin datos${reset}"
  fi
else
  log "${red}❌ Tópico /scan no encontrado${reset}"
fi

# 3. Verificar cámara OAK-D
log "\n[TEST] Verificando cámara OAK-D..."
if ros2 topic list | grep -q "/oakd/rgb/preview/image_raw"; then
  if ros2 topic echo --once /oakd/rgb/preview/image_raw > /dev/null 2>&1; then
    log "${green}✅ Cámara OAK-D funcionando${reset}"
  else
    log "${red}❌ Cámara sin datos${reset}"
  fi
else
  log "${red}❌ Tópico de la cámara no encontrado${reset}"
fi

# 4. Verificar botones OLED
log "\n[TEST] Verificando botones OLED..."
if ros2 topic list | grep -q "/interface_buttons"; then
  if ros2 topic echo --once /interface_buttons > /dev/null 2>&1; then
    log "${green}✅ Botones detectados${reset}"
  else
    log "${red}❌ Botones sin respuesta${reset}"
  fi
else
  log "${red}❌ Tópico /interface_buttons no encontrado${reset}"
fi

# 5. Verificar display OLED
log "\n[TEST] Verificando display OLED..."
if ros2 topic list | grep -q "/hmi/display/message"; then
  if ros2 topic pub --once /hmi/display/message std_msgs/msg/String "data: '✅ TEST DISPLAY'" > /dev/null 2>&1; then
    log "${green}✅ Mensaje enviado al display${reset}"
  else
    log "${red}❌ No se pudo escribir en el display${reset}"
  fi
else
  log "${red}❌ Tópico /hmi/display/message no encontrado${reset}"
fi

# 6. Verificar árbol TF
log "\n[TEST] Verificando árbol TF..."
ros2 run tf2_tools view_frames > /dev/null 2>&1
if [ -f frames.pdf ]; then
  TF_NAME="logs/frames_$(date +%Y%m%d_%H%M).pdf"
  mv frames.pdf "$TF_NAME"
  log "${green}✅ Árbol TF generado: ${TF_NAME}${reset}"
else
  log "${red}❌ No se generó el árbol TF${reset}"
fi

# 7. Verificación manual de /cmd_vel
log "\n[TEST] Verificación manual de movimiento:"
log "  Ejecuta en otra terminal: ros2 run teleop_twist_keyboard teleop_twist_keyboard"

log "\n[TEST] ✅ Verificación terminada. Resultado en ${LOG_FILE}"

