This project implements various SLAM algorithms in ROS. The algorithms implemented include:
1. G-Mapping
2. Karto
3. Frontier Exploration
4. Cartographer
5. Hector SLAM

First, run the gazebo_env_<asl/room/def>.sh script. It brings up the Gazebo world you selected. The gazebo_env_asl.sh 
brings up a  custom environment of the Autonomous Systems Lab, SRMIST.
Note that this is a custom made environment to suit our requirements.
If need be, other inbuilt Gazebo worlds can also be called by using the ather bash scripts.

(Run the bash script by typing bash <bash_script_name.sh> in the terminal)

Next, run the <gmapping/karto/frontier_exploration>_slam.sh script. 
This opens up Rviz. Once the SLAM process starts, the map will be generated here.
Note that the SLAM algorithm can be changed by using the required bash files.

Next, run the auto_nav.sh for the TurtleBot 3 Burger to Autonomously Navigate throughout and run the SLAM algorithm.
Tele operation can also be used to manually control the TurtleBot through the keyboard.

To run the algorithms live on a physical TurtleBot, the ROS_MASTER_URI and ROS_HOSTNAME need to be set 
via the terminal by editing the ~/.bashrc script.

The data_coll file contains the measured data of CPU performances, its plots, Python scripts for calculation of
various metrics such as SSIM, RMSE, | R |, and | S | and a video of each methods run run.

---

## ROS 1 Compatibility Status

> [!WARNING]
> ### ROS 1 + Ubuntu 22.04 Compatibility Issues
> This project was originally developed for **ROS Melodic (Python 2.7)**.  
> Running it on **ROS Noetic + Ubuntu 22.04** currently introduces major compatibility and dependency issues.

> [!CAUTION]
> ### Known Problems
> - Missing `gazebo_ros` and `urdf` package compatibility for Ubuntu 22.04
> - Legacy Python 2 scripts inside `data_coll/` fail under Python 3
> - Cartographer compilation issues on newer GCC/CMake toolchains
> - Gazebo integration instability on modern ROS 1 environments

> [!TIP]
> ### Troubleshooting Guide
> For detailed fixes, workarounds, and environment setup instructions, see:
>
> `ROS1_TROUBLESHOOTING.md`

---

## Project Modernization Roadmap

> [!IMPORTANT]
> ### Python 3 Migration
> Refactored Python 3 compatible scripts are available inside:
>
> `data_coll/*_py3.py`

> [!IMPORTANT]
> ### ROS 2 Transition
> This project is actively being migrated to:
>
> - **ROS 2 Humble**
> - Native Ubuntu 22.04 support
> - Modern Gazebo integration
> - Updated dependency stack and tooling

> [!NOTE]
> The long-term goal is to fully deprecate legacy ROS Melodic/Python 2 dependencies.