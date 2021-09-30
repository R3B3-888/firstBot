import sys
try:
    from libs.Motors import *
except ImportError:
    
    sys.path.append(sys.path[0] + '/..')
    from libs.Motors import *
import pypot.dynamixel as dyn
import time

ports = dyn.get_available_ports()
if not ports:
	exit('No port')

dxl_io = Motors(ports[0])
d1 = [0,0,0,0.5,0.5,-0.5,-0.5,3]
d = [0,0,0.5,-0.5,3]
k = 0.4
def lets_go(list_direction):
	i = 0
	while(1):
		time.sleep(1)
		if i == len(d):
			exit()
		elif d[i] < 0 and d[i] > -1:
			dxl_io.turn_left(d[i])
		elif d[i] > 0 and d[i] < 1:
			dxl_io.turn_right(d[i])
		elif d[i] == 0 :
			dxl_io.go_forward()
		elif d[i] > 1 or d[i] < -1 :
			dxl_io.stop()
		
		i+=1



lets_go(d)




