# ROS 1 Noetic Troubleshooting & Known Issues (Ubuntu 22.04)

This document details the issues encountered when trying to run this legacy project on a system running Ubuntu 22.04 with ROS Noetic.

## 1. Operating System Mismatch
*   **Issue**: ROS Noetic is designed for Ubuntu 20.04 (Focal). Running it on Ubuntu 22.04 (Jammy) results in a "partial" installation.
*   **Symptom**: Core packages like `gazebo_ros`, `urdf`, and `xacro` are unavailable via standard `apt` for ROS Noetic on Ubuntu 22.04.
*   **Result**: Gazebo simulations will not launch, and robot models cannot be parsed.

## 2. Python Version Conflicts
*   **Issue**: The original project was built for ROS Melodic (Python 2.7). ROS Noetic requires Python 3.
*   **Symptom**: Many scripts in `data_coll/` use Python 2 syntax and outdated library APIs (e.g., `skimage.measure.compare_ssim`).
*   **Fix**: Use the refactored scripts suffixed with `_py3.py` (e.g., `similarity_metric_py3.py`).

## 3. C++ Compatibility & Library Mismatches
*   **Issue**: Modern compilers on Ubuntu 22.04 use C++ standards that are often incompatible with legacy versions of `cartographer` and `ceres-solver` as configured for ROS Noetic.
*   **Symptom**: Compilation errors during `catkin_make_isolated` related to `Eigen` and `std::map`.
*   **Result**: Advanced SLAM algorithms like Cartographer may fail to build without significant manual patching.

## 4. Hardcoded Paths
*   **Issue**: Legacy build artifacts (`build/`, `devel/`) may contain hardcoded paths to previous developer environments (e.g., `/home/rushad/...`).
*   **Fix**: Always delete `build/`, `devel/`, and `install/` folders before attempting a build on a new machine.

## Recommended Alternative
If you must use ROS 1 for this project on Ubuntu 22.04+, it is highly recommended to use **Docker** with an `osrf/ros:noetic-desktop-full` image based on Ubuntu 20.04. Otherwise, migrating to **ROS 2 Humble** is the preferred path for Ubuntu 22.04.
