import os
os.system('cls' if os.name == 'nt' else 'clear')

import time
from buildhat import Motor, MotorPair, ColorSensor, DistanceSensor
#import datetime
from datetime import datetime

#Define motor pair:
pair = MotorPair('A', 'B')
color =ColorSensor('C')
dist=DistanceSensor('D', threshold_distance=100)


def distance_cal():
	global distance
	distance=dist.get_distance()
	if distance > 150 or distance ==-1:
		pair.start(-15,15)
	else: 
		pair.stop()
		time.sleep(.05)
		#reverse 
		pair.run_for_rotations(2,20,-20)
	

while True:
	distance_cal()
	print("distance:", distance)
	
