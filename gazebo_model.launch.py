import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg_name = 'mobile_robot'
    pkg_share = get_package_share_directory(pkg_name)
    ros_gz_sim_share = get_package_share_directory('ros_gz_sim')

    xacro_file = os.path.join(pkg_share, 'model', 'robot.xacro')
    bridge_params = os.path.join(pkg_share, 'config', 'bridge_parameters.yaml')

    # ---------- Launch arguments ----------
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='empty.sdf',
        description='World file to load in Gazebo Sim',
    )
    rviz_arg = DeclareLaunchArgument(
        'rviz',
        default_value='false',
        description='Start RViz2',
    )

    # ---------- Robot description from xacro ----------
    robot_description = ParameterValue(
        Command(['xacro ', xacro_file]),
        value_type=str,
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True,
        }],
    )

    # ---------- Gazebo Sim ----------
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_share, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': ['-r ', LaunchConfiguration('world')],
        }.items(),
    )

    # ---------- Spawn the robot ----------
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'robot',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.05',
        ],
    )

    # ---------- ROS <-> Gazebo bridge ----------
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        output='screen',
        parameters=[{
            'config_file': bridge_params,
            'use_sim_time': True,
        }],
    )

    # ---------- RViz (optional) ----------
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        parameters=[{'use_sim_time': True}],
        condition=IfCondition(LaunchConfiguration('rviz')),
    )

    return LaunchDescription([
        world_arg,
        rviz_arg,
        robot_state_publisher,
        gz_sim,
        spawn_robot,
        bridge,
        rviz,
    ])
