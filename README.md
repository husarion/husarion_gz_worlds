# Husarion office world 

Custom made gazebo worlds.

## How to run

Prepare workspace and run Gazebo:

```bash
mkdir -p ~/ros2_ws
cd ~/ros2_ws
git clone https://github.com/husarion/husarion_office_gz.git src/husarion_office_gz

colcon build
source install/setup.bash
ros2 launch husarion_office_gz gz_sim.launch.py
```

## Results
![img1](./images/office1.png)
![img2](./images/office2.png)
![img3](./images/husarion_world.png)
