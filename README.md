# Turtlebot4 – Proyecto TFG

Este repositorio contiene un proyecto completo para **simular y desplegar** un Turtlebot 4 empleando **Webots** y **ROS 2 Humble**. Incluye pruebas de **SLAM**, grabación de datos, navegación autónoma y un **nodo de reparto** para distribuir productos.

---

## 📁 Estructura del Proyecto

```text
TFG/
├── mapa_rviz_simulacion/            # Mapa ideal (.pgm + .yaml) exportado desde RViz
│   ├── simulación_ideal.pgm
│   └── simulación_ideal.yaml
├── navegacion_con_y_sin_obstaculo-MCAP.zip
├── Simulacion_ideal_y_con_ruido-MCAP.zip
├── README.md
├── TB_Real/                         # Código y pruebas en robot real
│   ├── Nodo_Delivery_app/           # Nodo ROS 2 con la lógica de reparto
│   └── Test/                        # Bag files y scripts de test en entorno real
├── TFGwebots_ws/                    # Espacio de trabajo principal de simulación
│   ├── build/                       # Generado por colcon
│   ├── install/                     # Generado por colcon
│   ├── log/                         # Logs de compilación/ejecución
│   ├── src/                         # Paquetes ROS 2 (Webots, control, etc.)
│   ├── TB_Procesos.sh               # Script que lanza toda la simulación
│   ├── View_frames/                 # Capturas de los marcos de referencia
│   └── .vscode/                     # Configuración de VS Code (opcional)
```

---

## ▶️ Lanzar la simulación automáticamente

En `TFGwebots_ws/` encontrarás un script llamado `` que automatiza todo el flujo:

1. Abre el mundo de Webots con el Turtlebot 4.
2. Ejecuta SLAM en tiempo real.
3. Graba todos los tópicos ROS 2 en un archivo `.mcap`.
4. Lanza un nodo de movimiento del robot.
5. Guarda los bag files en `simulaciones/`.

### ✅ Cómo usarlo

1. Compila el espacio de trabajo:
   ```bash
   cd ~/Desktop/TFG/TFGwebots_ws/
   colcon build
   source install/setup.bash
   ```
2. Dale permisos y ejecútalo:
   ```bash
   chmod +x TB_Procesos.sh
   ./TB_Procesos.sh
   ```

Los datos se guardarán automáticamente con un nombre basado en **fecha y hora**.

---

## 🛠️ Pruebas en el Robot Real

A continuación se detalla cómo **crear el mapa** con SLAM y, después, **lanzar la localización y la navegación** con Nav2 sobre el mapa generado.

### 1. Crear el mapa (SLAM)

#### a) Terminal SSH en el robot

```bash
ros2 launch turtlebot4_bringup standard.launch.py \
  param_file:=$HOME/turtlebot4_ws/src/robot_delivery_app/config/turtlebot4_no_menu.yaml
```

#### b) Terminales en el PC

```bash
# SLAM 
ros2 launch turtlebot4_navigation slam.launch.py

# Teleoperación WASD
ros2 run teleop_twist_keyboard teleop_twist_keyboard

# Visualización en RViz
ros2 launch turtlebot4_viz view_robot.launch.py

# Guardar el mapa cuando esté listo
ros2 run nav2_map_server map_saver_cli -f ~/mi_mapa
```

Se generarán `` y `` en la ruta indicada.

---

### 2. Localización y navegación en el mapa

#### a) Terminales SSH en el robot

```bash
# Bring‑up del robot
ros2 launch turtlebot4_bringup standard.launch.py \
  param_file:=$HOME/turtlebot4_ws/src/robot_delivery_app/config/turtlebot4_no_menu.yaml

# AMCL (localización)
ros2 launch turtlebot4_navigation localization.launch.py \
  map:=/home/turtlebot4/mapas/mi_mapa.yaml

# Nav2 (planificación y control)
ros2 launch turtlebot4_navigation nav2.launch.py \
  slam:=off localization:=true \
  map:=/home/turtlebot4/mapas/mi_mapa.yaml \
  params_file:=/home/turtlebot4/turtlebot4_ws/src/robot_delivery_app/config/nav2_params_big.yaml

# Interfaz de reparto
ros2 run robot_delivery_app user_interface_node
```

#### b) Terminales en el PC

```bash
# Teleoperación opcional
ros2 run teleop_twist_keyboard teleop_twist_keyboard

# Visualización en RViz
ros2 launch turtlebot4_viz view_robot.launch.py
```

Una vez cargados todos los nodos, establece la **pose inicial** en RViz, elige los destinos mediante la interfaz (`user_interface_node`) y el robot distribuirá los productos en los puntos almacenados.

[![Demo en YouTube](https://img.youtube.com/vi/sXMZNmpou8c/hqdefault.jpg)](https://www.youtube.com/watch?v=sXMZNmpou8c "Haz clic para reproducir")

---

## ✅ Requisitos

- **ROS 2 Humble**
- **Webots**
- **Turtlebot 4**

---

## ✉️ Contacto

- [ahechedey@gmail.com](mailto\:ahechedey@gmail.com)
- [echaguher@alum.us.es](mailto\:echaguher@alum.us.es)

¡Gracias por visitar el proyecto! 🤖

