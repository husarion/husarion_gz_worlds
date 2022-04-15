# Husarion office world 

## How to run 
Prepare workspace and run Gazebo:
```bash
mkdir gazebo_worlds
cd gazebo_worlds
git clone https://github.com/husarion/gazebo_worlds.git src
git clone -b foxy https://github.com/husarion/rosbot_description.git src/rosbot_description

colcon build
source install/setup.bash
source /usr/share/gazebo-11/setup.bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:<dir/to/workspace>/install/husarion_office_gz/share/husarion_office_gz/worlds/models/

ros2 launch husarion_office_gz husarion_office_world.launch.py
```



## Results
![img1](./images/office1.png)
![img2](./images/office2.png)
