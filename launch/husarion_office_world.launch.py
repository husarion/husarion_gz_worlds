import os
import launch
import launch_ros
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    rosbot_description = get_package_share_directory('rosbot_description')
    map_package = get_package_share_directory('husarion_office_gz')

    world_file = os.path.join(map_package, 'worlds', 'husarion_office.world')

    world_cfg = LaunchConfiguration('world')

    declare_world_arg = DeclareLaunchArgument('world', default_value=world_file, description='SDF world file')

    
    include_files = GroupAction([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([rosbot_description, '/launch/rosbot_sim.launch.py']),
            launch_arguments = {'world': world_cfg}.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([rosbot_description, '/launch/rosbot_navigation_sim.launch.py']),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([rosbot_description, '/launch/slam_toolbox_sim.launch.py']),
        ),
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name="rviz2",
            arguments=['-d', rosbot_description+"/config/rosbot.rviz"],
        ),
    ])
    
    ld = LaunchDescription()
    ld.add_action(declare_world_arg)
    ld.add_action(include_files)
    
    return ld
