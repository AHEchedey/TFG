# Simulación Turtlebot4 - Proyecto TFG

Este repositorio contiene un proyecto de simulación con el robot Turtlebot4 utilizando Webots y ROS 2 Humble. El entorno ha sido diseñado para realizar pruebas con SLAM, grabación de datos y control automático del robot.

---

## 📁 Estructura del Proyecto

```
TFG/
├── Capturas simulaciones/           # rosbag de las simulaciones
├── TFGwebots_ws/                    # Espacio de trabajo principal
│   ├── TB_Procesos.sh               # Script para lanzar toda la simulación
│   ├── src/                         # Código fuente (paquetes ROS2)
│   ├── simulaciones/               # Carpeta donde se guardan los bag files
│   ├── View_frames/                # Visualización de frames (opcional)
│   └── build/, install/, log/      # Carpetas generadas por colcon
```

---

## ▶️ Lanzar la simulación automáticamente

Dentro de `TFGwebots_ws/` se encuentra un script llamado `TB_Procesos.sh` que automatiza el proceso completo:

1. Lanza el mundo de Webots con el robot Turtlebot4.
2. Ejecuta SLAM en tiempo real.
3. Graba todos los tópicos ROS2 en un archivo `.mcap`.
4. Ejecuta un nodo de movimiento del robot.
5. Guarda los datos en la carpeta `simulaciones/`.

### ✅ Cómo usarlo


1. compilar proyecto TFGWebots_ws
	colcon build
2. Sourcear
	source install/setup.bash

```bash
cd ~/Desktop/TFG/TFGwebots_ws/
chmod +x TB_Procesos.sh
./TB_Procesos.sh
```

Los datos se guardarán automáticamente en la carpeta `simulaciones/` con nombre basado en la fecha y hora de la ejecución.

---

## Requisitos

- ROS 2 Humble
- Webots instalado
- Dependencias como `slam_toolbox`, `ros2_bag`, etc.

---

¡Gracias por visitar este proyecto! 🤖 Si tienes dudas, puedes abrir un issue o contactar con el autor.
@ ahechedey@gmail.com
@ echaguher@alum.us.es
