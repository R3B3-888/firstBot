import numpy as np
import cv2 as cv


class Capture:
    _camera_id = 0

    _lower_blue = np.array([100, 100, 100])
    _upper_blue = np.array([140, 255, 255])
    _lower_red0 = np.array([0, 100, 100])
    _upper_red0 = np.array([10, 255, 255])
    _lower_red1 = np.array([170, 50, 50])
    _upper_red1 = np.array([180, 255, 255])
    _lower_yellow = np.array([20, 50, 50])
    _upper_yellow = np.array([40, 255, 255])

    def __init__(self, cam_id):
        print("Camera Object created")
        self._camera_id = cam_id

    def _colored_mask(self, image, lower_color, upper_color):
        return cv.inRange(image, lower_color, upper_color)

    def _direction(self, mask):
        width = mask.shape[0]
        mask_mean = width // 2

        left_weight = mask[:, :mask_mean].sum(dtype=np.int32)
        right_weight = mask[:, mask_mean:].sum(dtype=np.int32)

        return (left_weight - right_weight) / (left_weight + right_weight + 1)

    def capture_video(self, enable_windows):
        print("capturing")
        capture = cv.VideoCapture(self._camera_id)
        while True:
            img_returned, frame = capture.read()

            if not img_returned:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            blue_img_cpy = np.copy(frame)
            red_img_cpy = np.copy(frame)
            yellow_img_cpy = np.copy(frame)

            hsv_blue = cv.cvtColor(blue_img_cpy, cv.COLOR_BGR2HSV)
            hsv_red = cv.cvtColor(red_img_cpy, cv.COLOR_BGR2HSV)
            hsv_yellow = cv.cvtColor(yellow_img_cpy, cv.COLOR_BGR2HSV)

            blue_mask = self._colored_mask(hsv_blue, self._lower_blue, self._upper_blue)
            red_mask0 = self._colored_mask(hsv_red, self._lower_red0, self._upper_red0)
            red_mask1 = self._colored_mask(hsv_red, self._lower_red1, self._upper_red1)
            red_mask = red_mask0 + red_mask1
            hsv_red[np.where(red_mask == 0)] = 0
            yellow_mask = self._colored_mask(hsv_yellow, self._lower_yellow, self._upper_yellow)

            if enable_windows:
                cv.imshow("Blue_mask", blue_mask)
                cv.imshow("Red_mask", red_mask)
                cv.imshow("Yellow_mask", yellow_mask)


            # if key 'q' is press, close the windows and close
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv.destroyAllWindows()

    #    def get_direction(self)

#    def get_angle(self)
