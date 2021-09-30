import sys
try:
    from libs.Capture import *
except ImportError:
    
    sys.path.append(sys.path[0] + '/..')
    from libs.Capture import *

import settings

def test_capture(show_windows):
    print("The test on capture processing ...")
    
    Camera = Capture(0)
    Camera.capture_video(show_windows)

    #Camera.get_angle()

    #LeftMotor = Motor(IDLEFT)
    #RightMotor = Motor(IDRIGHT)
    
test_capture(sys.argv[1])
