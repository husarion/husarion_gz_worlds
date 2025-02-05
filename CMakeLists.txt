cmake_minimum_required(VERSION 3.11)

project(husarion_gz_worlds)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch models worlds maps DESTINATION share/${PROJECT_NAME})

ament_environment_hooks(
  "${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/${PROJECT_NAME}.sh.in")
ament_package()
