import numpy as np
import cv2 as cv


class Capture:

    _camera_id = 0
    
    _lower_blue = np.array([110, 50, 50])
    _upper_blue = np.array([130, 255, 255])
    _lower_red = np.array([0, 50, 50])
    _upper_red = np.array([15, 255, 255])
    _lower_yellow = np.array([20, 50, 50])
    _upper_yellow = np.array([40, 255, 255])
    
    
    def __init__(self, id):
        print("Camera Object created")
        self._camera_id = id
        

    def capture_video(self, enable_windows):
        print("capturing")
        capture = cv.VideoCapture(self._camera_id)
        while True:
            imgReturned, frame = capture.read()

            if not imgReturned:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            lane_image = np.copy(frame)
            lane_image2 = np.copy(frame)
            
            hsv_blue = cv.cvtColor(lane_image, cv.COLOR_BGR2HSV)
            hsv_red = cv.cvtColor(lane_image2, cv.COLOR_BGR2HSV)
            blue_mask = cv.inRange(hsv_blue, self._lower_blue, self._upper_blue)
            red_mask = cv.inRange(hsv_red, self._lower_red, self._upper_red)
            
            if enable_windows:
                cv.imshow("Blue_mask", blue_mask)
                cv.imshow("Red_mask", red_mask)

            # if key 'q' is press, close the windows and close
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv.destroyAllWindows()        

#    def get_direction(self)

#    def get_angle(self)


    

