from buildhat import MotorPair, ColorSensor, DistanceSensor
import time

motorpair = MotorPair('A','B')
color = ColorSensor('C')
dist = DistanceSensor('D', threshold_distance=100)
target_light = 50  # Target reflected light value
kP = 1.55  # Proportional gain
kD = 0.3  # Derivative gain

previous_error = 0
# set default speed
motorpair.set_default_speed(15)
while True:
    # Read the reflected light value from the color sensor
	current_light = color.get_reflected_light()

    # Calculate the error
	error = current_light - target_light
	print("ERROR", error)
    # Calculate the proportional component
	proportional_component = kP * error

    # Calculate the derivative component
	derivative_component = kD * (error - previous_error)
	print("P", proportional_component, "D", derivative_component)
    # Calculate the control signal
	control_signal = proportional_component + derivative_component
	print("CONTROL_SIGNAL", control_signal)
    # Apply the control signal to the motors
	left_motor_speed = control_signal
	right_motor_speed = control_signal
	
	motorpair.start(left_motor_speed)
	print("LEFT SPEED", left_motor_speed, "RIGHT_SPEED", motorpair._rightmotor.get_speed())
#	print(motorpair._rightmotor.get_speed())
    # Update the previous error for the next iteration
	previous_error = error

    # Add a delay to avoid overloading the motors
#	time.sleep(0.01)
