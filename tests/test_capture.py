import sys
try:
    from libs.Capture import *
except ImportError:
    
    sys.path.append(sys.path[0] + '/..')
    from libs.Capture import *

def test_capture(show_windows, path):
    print("The test on capture processing ...")
    
    Camera = Capture(1, path)
    Camera.capture_video(show_windows)

    #Camera.get_angle()

    #LeftMotor = Motor(IDLEFT)
    #RightMotor = Motor(IDRIGHT)


test_path = np.array(["blue", "red", "yellow"])

test_capture(sys.argv[1], test_path)
