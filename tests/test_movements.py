from Motors import Motors
import pypot.dynamixel as dyn
import time

ports = dyn.get_available_ports()
if not ports:
	exit('No port')

dxl_io = Motors(ports[0])
dxl_io.rotate_angle_clockwise(90)
