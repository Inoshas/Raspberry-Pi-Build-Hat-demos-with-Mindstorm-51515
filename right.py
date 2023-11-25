from buildhat import MotorPair, ColorSensor, DistanceSensor
import time

pair = MotorPair('A','B')
color = ColorSensor('C')
dist = DistanceSensor('D')
def turn_right():
    pair.run_for_degrees(270,-20,-20)
    pair.stop()
    time.sleep(1)
    
turn_right()
print("turning right")