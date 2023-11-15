from buildhat import MotorPair
import time
pair = MotorPair('A','B')

def turn_right():
    pair.run_for_degrees(90,-20,0)
    pair.stop()
    time.sleep(1)