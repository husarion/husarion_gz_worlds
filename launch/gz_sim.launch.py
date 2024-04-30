from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def launch_setup(context, *args, **kwargs):
    gz_log_level = LaunchConfiguration("gz_log_level").perform(context)
    headless_mode = LaunchConfiguration("headless_mode").perform(context)
    world = LaunchConfiguration("world").perform(context)

    gz_args = f"-r -v {gz_log_level} {world}"
    if eval(headless_mode):
        gz_args = "--headless-rendering -s " + gz_args

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("ros_gz_sim"),
                    "launch",
                    "gz_sim.launch.py",
                ]
            )
        ),
        launch_arguments={"gz_args": gz_args}.items(),
    )

    return [gz_sim]


def generate_launch_description():
    pkg_path = FindPackageShare("husarion_office_gz")

    declare_gz_log_level = DeclareLaunchArgument(
        "gz_log_level", default_value="1", description="Adjust the level of console output.", choices=["0", "1", "2", "3", "4"]
    )

    declare_headless_mode = DeclareLaunchArgument(
        "headless_mode", default_value="False", description="Run the simulation in headless mode. Useful when a GUI is not needed or to reduce the amount of calculations.", choices=["True", "False"]
    )

    declare_world_arg = DeclareLaunchArgument(
        "world", default_value=PathJoinSubstitution([pkg_path, "worlds", "husarion_world.sdf"]), description="Path to SDF world file."
    )

    return LaunchDescription(
        [
            declare_gz_log_level,
            declare_headless_mode,
            declare_world_arg,
            OpaqueFunction(function=launch_setup),
        ]
    )
