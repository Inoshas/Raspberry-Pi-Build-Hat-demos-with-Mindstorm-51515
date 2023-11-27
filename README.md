
# Raspberry Pi and Mindstorms EV3 (51515) Python Testing

Welcome to the Raspberry Pi and Mindstorms EV3 (51515) Python testing repository! This project includes basic Python scripts to test LEGO Mindstorms EV3 motors and sensors using a Raspberry Pi and the `buildhat` library.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [Future Contributions](#future-contributions)
- [License](#license)

## Introduction

This project aims to demonstrate the integration of Raspberry Pi with the Mindstorms EV3 robot using Python. The provided scripts cover a range of functionalities and serve as a foundation for further development.

## Getting Started

### Prerequisites

- Raspberry Pi with Raspbian (or another Linux distribution) installed
- Python installed on your Raspberry Pi
- LEGO Mindstorms EV3 set (51515)
- Raspberry Pi build hat

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Inoshas/Raspberry-Pi-Build-Hat-demos-with-Mindstorm-51515

Navigate to the project directory: 
    ```bash

    cd your-repository 

Install project dependencies:
    ```bash

    sudo apt update
    sudo apt install python3-buildhat
Note: Replace python3 with python if your system uses Python 2.x.

#### Other Dependencies:
**time:** Standard Python library for time-related functions.

**datetime:** Standard Python library for working with dates and times. (Note: The import statement from datetime import datetime is used in the code.)

**os:** Standard Python library for interacting with the operating system.

Ensure that these standard libraries are available in your Python environment.

## File Structure
Setup Motors and Sensors:

Initialize the motors and sensors using the following setup:

    ```python
    # Create a motor pair with motors connected to ports 'A' and 'B'
    pair = MotorPair('A', 'B')

    # Create a color sensor connected to port 'C'
    color_sensor = ColorSensor('C')

    # Create a distance sensor connected to port 'D' with a threshold distance of 100 units
    distance_sensor = DistanceSensor('D', threshold_distance=100)

Power Supply:

Ensure that your Raspberry Pi, as well as the Raspberry Pi build hat, is powered using an 8V power supply. Connect the power supply to provide sufficient power to the entire setup.

Run Tests or Scripts:

Execute the provided scripts or write your own tests using the initialized motors and sensors. Adjust the scripts according to your specific use case.

Example script using the initialized motors and sensors: 

    python
    # Move the motor pair forward at 50% speed
    pair.forward(50) 
    # Get the current color value 
    color_value = color_sensor.get_color() 
    # Get the current distance value
    distance_value = distance_sensor.get_distance()



### Content

**single_motor_test.py:** Example script demonstrating the control of a single motor ('A') using the buildhat library on the Raspberry Pi.

**turning_motor.py:** This script, turning_motor.py, demonstrates the control of a motor pair ('A' and 'B') for various movements, including forward, backward, and turning left.

**propotional_behaviour.py:** This is a supporting file to analyze the the effect of proportional gain (kp) on motor speed in a control system. This can be used to understand the speed variartion changes use for path_follower.py

**path_follower.py:** The path_follower.py script implements a basic path-following algorithm using a PID controller. 

**path_follower_PD.py:** The path_follower_PD.py script implements a basic path-following algorithm using a PD controller.

**obstacle_stop_moveback.py:** The obstacle_stop_moveback.py script implements a basic obstacle avoidance algorithm.

## Contributing
This project welcomes contributions from the community. If you find a bug or have an idea for a new feature, please open an issue or submit a pull request. Your input is valuable, and we appreciate your help!


### Contributors

- [Antti Buller](https://github.com/anatt1b)
  
- [Inosha Sugathapala](https://github.com/Inoshas)

### Future Contributions
We are open to future contributions that enhance the functionality of this project. If you have ideas for new features or improvements, please let us know by opening an issue or starting a discussion.

## License

This project is licensed under the MIT License.
