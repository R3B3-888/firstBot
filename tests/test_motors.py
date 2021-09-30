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
dxl_io.go_forward()
time.sleep(2)
dxl_io.turn_left()
time.sleep(2)
dxl_io.stop()
