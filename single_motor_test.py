"""Example driving motors"""

import time

from buildhat import Motor

motor = Motor('A')

### Testing motors seperately:
def handle_motor(speed, pos, apos):
    """Motor data

    :param speed: Speed of motor
    :param pos: Position of motor
    :param apos: Absolute position of motor
    """
    print("Motor", speed, pos, apos)

# This will print motora  attributes
motor.when_rotated = handle_motor

#Set default speed: This is set to left and need minus value to move forward:
motor.set_default_speed(-50)

print("Testing degrees")
#Rotate the wheel 360 degree
motor.run_for_degrees(360)
time.sleep(3)
print("Stop motor")
motor.stop()

#Rotate the wheeel 2 rounds:::
print("Run for rotations")
motor.run_for_rotations(2)
time.sleep(3)

#Rotate the wheeel 2 rounds:::
print("Run for seconds")
motor.run_for_seconds(2, 34)
time.sleep(3)

