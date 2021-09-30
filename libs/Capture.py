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

    _actual_mask = None
    _path_color = "Blue"

    def __init__(self, cam_id):
        print("Camera Object created")
        self._camera_id = cam_id

    def _colored_mask(self, image, lower_color, upper_color):
        return cv.inRange(image, lower_color, upper_color)

    def get_direction(self):
        width = self._actual_mask.shape[0]
        mask_mean = width // 2

        left_weight = self._actual_mask[:, :mask_mean].sum(dtype=np.int32)
        right_weight = self._actual_mask[:, mask_mean:].sum(dtype=np.int32)

        return (left_weight - right_weight) / (left_weight + right_weight + 1)

    def capture_video(self, enable_windows):
        print("capturing")
        capture = cv.VideoCapture(self._camera_id)
        while True:
            img_returned, frame = capture.read()

            if not img_returned:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            blue_mask = self._mask_processing(frame, self._lower_blue, self._upper_blue)            
            yellow_mask = self._mask_processing(frame, self._lower_yellow, self._upper_yellow)
            red_mask = self._red_mask_processing(frame)
            # if turn % 2 == True : 
            #     self._actual_mask = blue_mask
            # else:
            #     self.actual_mask = red_mask
            


            if enable_windows:
                cv.imshow("Blue_mask", blue_mask)
                cv.imshow("Red_mask", red_mask)
                cv.imshow("Yellow_mask", yellow_mask)


            # if key 'q' is press, close the windows and close
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv.destroyAllWindows()

    def has_cross_yellow_line(self):
        # calcul de la détection
        # return True
        # turn += 1
        pass

    def _mask_processing(self, frame, lower_color, upper_color):
            img_cpy = np.copy(frame)
            hsv = cv.cvtColor(img_cpy, cv.COLOR_BGR2HSV)
            mask = self._colored_mask(hsv, lower_color, upper_color)
            return mask

    def _red_mask_processing(self, frame):
            img_cpy = np.copy(frame)
            hsv = cv.cvtColor(img_cpy, cv.COLOR_BGR2HSV)
            mask0 = self._colored_mask(hsv, self._lower_red0, self._upper_red0)
            mask1 = self._colored_mask(hsv, self._lower_red1, self._upper_red1)
            mask = mask0 + mask1
            hsv[np.where(mask == 0)] = 0
            return mask