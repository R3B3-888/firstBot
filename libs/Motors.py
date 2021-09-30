import pypot.dynamixel as dyn
import math
import time 

IDLEFT = 2
IDRIGHT = 5
SPEED = 360 

radius_wheel = 2.6 #in cm
radius_between_wheels = 16.6 #in cm 
#Motors, dyn.DxlIO subclass
class Motors(dyn.DxlIO):
	
    #Go forward at SPEED speed
	def go_forward(self):
		self.set_moving_speed({IDLEFT: SPEED, IDRIGHT: -SPEED})
	#Stop the wheels by disabling the torque excerce by the motors
	def stop(self):
		self.disable_torque([5,2])
	#Turn left or right depending on kl and kr (kl > kr turn right)
	def turn(self, kl: float, kr: float):
		self.set_moving_speed({IDLEFT: SPEED*kl, IDRIGHT: -SPEED*kr})
	#Turn to the left
	def turn_left(self,d):
		self.set_moving_speed({IDLEFT: SPEED*(d+1), IDRIGHT: -SPEED})
	#Turn to the right
	def turn_right(self,d):
		self.set_moving_speed({IDLEFT: SPEED, IDRIGHT: -SPEED*(1-d)})
	def rotate_angle_clockwise(self,angle):
		angle = angle*180/math.pi
		#move the left wheel but not the right
		perimeter_circunference_robot = 2*math.pi*radius_between_wheels
		perimeter_circunference_wheel = 2*math.pi*radius_wheel
		distance_rotation = (angle*perimeter_circunference_robot)/360
		distance_rotation/=2
		#we need the speed of the wheel
		v_rad = SPEED*math.pi/180

		speed = v_rad * radius_wheel
		times = distance_rotation/speed
		print(times, speed, distance_rotation)
		#set the timer
		self.set_moving_speed({IDLEFT: SPEED, IDRIGHT: SPEED})
		time.sleep(times)
		self.stop()
