import pypot.dynamixel as dyn
import math
import time 
from constants import *

IDLEFT = 2
IDRIGHT = 5
SPEED = 100

radius_wheel = 2.6 #in cm
radius_between_wheels = 16.6 #in cm 
#Motors, dyn.DxlIO subclass
class Motion(dyn.DxlIO):
    #Go forward at SPEED speed
	def go_forward(self):
		self.set_moving_speed({IDLEFT: SPEED*2, IDRIGHT: -SPEED*2})
		time.sleep(0.02)
	#Stop the wheels by disabling the torque excerce by the motors
	def stop(self):
		self.disable_torque([5,2])
	#Turn left or right depending on kl and kr (kl > kr turn right)
	def turn_old(self, kl: float, kr: float):
		self.set_moving_speed({IDLEFT: SPEED*kl, IDRIGHT: -SPEED*kr})
	#Turn to the left
	def turn_left(self,d):
		self.set_moving_speed({IDLEFT: SPEED+SPEED*(d+1), IDRIGHT: -2*SPEED})
	#Turn to the right
	def turn_right(self,d):
		self.set_moving_speed({IDLEFT: 2*SPEED, IDRIGHT: -SPEED-SPEED*(1-d)})

	def turn(self, d):
		if d > RANGE_OFFSET:
			self.turn_right(d)
		elif d < (-RANGE_OFFSET):
			self.turn_left(d)
		else:
			self.go_forward()
