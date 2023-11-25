import os
os.system('cls' if os.name == 'nt' else 'clear')

import time
from buildhat import Motor, MotorPair

#Define motor pair:
pair = MotorPair('A', 'B')

#Enabe functio to print motor readings while running:

def handle_motor(speed, pos, apos):
    """Motor data

    :param speed: Speed of motor
    :param pos: Position of motor
    :param apos: Absolute position of motor
    """
    print("Motor", speed, pos, apos)

#set motors  default values:::
# Better define this if you use run_for_seconds:::

pair._leftmotor.set_default_speed(-60)
pair._rightmotor.set_default_speed(60)


##Print left and right motor values
print("This print motor speed")
pair._leftmotor.when_rotated = handle_motor
pair._rightmotor.when_rotated =handle_motor


pair.start()
print("Forward moving start here----")
#Run forward for 3 rotations::
pair.run_for_rotations(4,-50,50)
pair.stop()
print("Stop moving forward")
#stay for .5 :
time.sleep(.5)

#go backward :::
pair.run_for_rotations(4, 50,-50)
pair.stop()
time.sleep(.5)


##### Turn left:::::
def turn_left():
	print(f"turn{count} start here::")
	pair.run_for_rotations(1.9,50,0)
	pair.stop()
	time.sleep(1.5)
	print("Motor turns and ready to go")

def move_forward():
	pair.run_for_rotations(3,-50,50)
	pair.stop()
	print("Motor Stop")
	time.sleep(1.5)
	
count=0
while(count<4):
#turn left and move
	turn_left()
	move_forward()
	count +=1
	

