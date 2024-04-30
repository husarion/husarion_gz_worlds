cmake_minimum_required(VERSION 3.5)

project(husarion_office_gz)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

install(DIRECTORY launch worlds DESTINATION share/${PROJECT_NAME})

ament_package()