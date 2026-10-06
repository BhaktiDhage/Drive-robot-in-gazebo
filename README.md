# Drive-robot-in-gazebo
Differential drive robot simulated in ROS 2 and Gazebo, with a URDF/Xacro model, launch files, RViz visualisation and teleop control.
# Differential Drive Bot: ROS 2 + Gazebo Simulation

A simulated differential drive robot built from scratch in ROS 2 and Gazebo. It was made while learning the ROS 2 and Gazebo workflow: describing the robot in URDF/Xacro, spawning it in a Gazebo world, and driving it with velocity commands.


https://github.com/user-attachments/assets/c18ab5a9-df49-4c3a-b856-f95727f69f97




## What this project covers

- Robot modelling with **URDF/Xacro** (chassis, wheels, joints, inertia)
- Spawning and simulating the robot in **Gazebo**
- Differential drive control through the Gazebo drive plugin
- Starting everything together with a **ROS 2 launch file**
- Visualising the robot in **RViz**
- Moving the robot with `/cmd_vel` (keyboard teleop)

## Tech stack

| Tool | Purpose |
|------|---------|
| ROS 2 (Humble/Jazzy: edit to match yours) | Robot middleware: nodes, topics, launch |
| Gazebo | Physics simulation |
| URDF / Xacro | Robot description |
| RViz2 | Visualisation |
| Python | Launch files and nodes |
| Ubuntu on WSL | Development environment |

## Repository structure

```
<your_package>/
├── launch/        # Launch files (spawn robot, start Gazebo, RViz)
├── urdf/          # Robot description (.urdf / .xacro)
├── worlds/        # Gazebo world files
├── config/        # RViz and controller configs
├── CMakeLists.txt
└── package.xml
```

Edit this tree to match your actual folders.

## Getting started

### Prerequisites

- Ubuntu (native or WSL) with ROS 2 installed
- Gazebo and the ROS 2 Gazebo packages
- `colcon` build tools

### Build

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

### Run the simulation

```bash
ros2 launch mobile_robot gazebo.launch.py
```

### Drive the robot

In a new terminal:

```bash
source ~/ros2_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## Useful commands

```bash
ros2 topic list              # see active topics
ros2 topic echo /odom        # watch odometry
ros2 node list               # see running nodes
ros2 run tf2_tools view_frames   # inspect the TF tree
```

## What I learned

- How nodes, topics, and messages fit together in ROS 2
- How a robot is described in URDF/Xacro and how links and joints define its structure
- How the Gazebo simulation pipeline works, from description to spawn to control
- Debugging launch files, plugin configs, and TF issues (a lot of this)

