"""Line Following

Robot should be able to follow a colored line
When it reaches the end of the track at the green and yellow tape, it will follow the next one:
Begin with the blue tape and change to the red one
"""


import pypot.dynamixel as dyn
from constants import *
import sys

try:
    from libs import Capture, Motion
except ImportError:
    sys.path.append(sys.path[0] + '/..')
    from libs import Capture, Motion
import time

def line_following():
    print("line following processing ...")

    Camera = Capture.Capture(0, ORDER_COLORS_PATH)
    ports = dyn.get_available_ports()
    Bot = Motion.Motion(ports[0])

    while(True):
        direction = Camera.get_direction(SHOW_WINDOWS) # value between -1 (left) and 1 (right) (0 you dont move)
        Bot.turn(direction)
        print(direction)
        # time.sleep(TIME_OFFSET)
        if Camera.is_interrupted_key_pressed(KEY):
            Camera.stop_capturing()
            break
    print("Out")
    
    

