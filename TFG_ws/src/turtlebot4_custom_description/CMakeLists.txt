cmake_minimum_required(VERSION 3.8)
project(turtlebot4_custom_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)

# Install urdf folder (containing xacro files)
install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

# Optional: if you later include meshes
# install(DIRECTORY meshes
#   DESTINATION share/${PROJECT_NAME}
# )

# Testing
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

