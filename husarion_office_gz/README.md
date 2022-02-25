# Husarion office world 

## How to run 
```bash
mkdir gazebo_worlds
cd gazebo_worlds
git clone https://github.com/husarion/gazebo_worlds.git src
git clone -b foxy https://github.com/husarion/rosbot_description.git src/rosbot_description

colcon build
source install/setup.bash
source /usr/share/gazebo-11/setup.bash
export GAZEBO_MODEL_PATH=<dir/to/workspace>/install/husarion_office_gz/share/husarion_office_gz/worlds/models/

ros2 launch husarion_office_gz husarion_office_world.launch.py
```

Change spawning coordinats in `rosbot_descriptions/launch/rosbot_spawn.launch.py` ([line 82](https://github.com/husarion/rosbot_description/blob/79440c2664d470afb59655b1ccaabcdd2975a1c5/launch/rosbot_spawn.launch.py#L82))):
```python
arguments=['-spawn_service_timeout', '60', '-entity', 'rosbot', '-x', '1.5', '-y', '-1.2', '-z', '0.03', '-file', rosbot_description_dir + '/models/rosbot.sdf']),
```

## Results
![img1](./images/office1.png)
![img2](./images/office2.png)