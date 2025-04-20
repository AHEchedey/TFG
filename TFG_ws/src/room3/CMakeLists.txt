cmake_minimum_required(VERSION 3.8)
project(room3)

# Opciones de compilador
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Dependencias requeridas
find_package(ament_cmake REQUIRED)

# Instalar carpeta maps (modelos, mapas, etc.)
install(DIRECTORY maps
  DESTINATION share/${PROJECT_NAME}/
)

# Instalar carpeta launch (archivos de lanzamiento)
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

# Soporte para pruebas (opcional)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_cpplint_FOUND TRUE)
  set(ament_cmake_copyright_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Declaración final del paquete
ament_package()
