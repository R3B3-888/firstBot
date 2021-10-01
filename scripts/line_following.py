"""Line Following

Robot should be able to follow a colored line
When it reaches the end of the track at the green and yellow tape, it will follow the next one:
Begin with the blue tape and change to the red one
"""


import pypot.dynamixel as dyn
from constants import *
import sys

try:
    from libs import Capture, Motors
except ImportError:
    sys.path.append(sys.path[0] + '/..')
    from libs import Capture, Motors


def line_following():
    print("line following processing ...")
    
    Camera = Capture.Capture(0, ORDER_COLORS_PATH)
    #ports = dyn.get_available_ports()
    #Bot = Motors.Motors(ports[0])
    
    while(True):
        direction = Camera.get_direction() # value between -1 (left) and 1 (right) (0 you dont move)
        #Bot.turn(direction)
        if Camera.is_interrupted_key_pressed(KEY):
            Camera.stop_all()
            break
    print("Out")
    

