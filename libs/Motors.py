import pypot.dynamixel as dyn

IDLEFT = 2
IDRIGHT = 5
SPEED = 360 
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
	def turn_left(self):
		self.set_moving_speed({IDLEFT: SPEED*0.8, IDRIGHT: -SPEED*1.2})
	#Turn to the right
	def turn_right(self):
		self.set_moving_speed({IDLEFT: SPEED*1.2, IDRIGHT: -SPEED*0.8})
