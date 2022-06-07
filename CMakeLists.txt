cmake_minimum_required(VERSION 3.5)

project(husarion_office_gz)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}
)


install(DIRECTORY
  world/
  DESTINATION share/${PROJECT_NAME}/worlds/
)

ament_package()
