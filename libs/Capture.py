import numpy as np
import cv2 as cv


class Capture:

    _lower_blue = np.array([100, 100, 100])
    _upper_blue = np.array([140, 255, 255])
    _lower_red0 = np.array([0, 100, 100])
    _upper_red0 = np.array([10, 255, 255])
    _lower_red1 = np.array([170, 50, 50])
    _upper_red1 = np.array([180, 255, 255])
    _lower_yellow = np.array([20, 50, 50])
    _upper_yellow = np.array([40, 255, 255])
    _lower_starting_color = _lower_yellow
    _upper_starting_color = _upper_yellow
    
    _camera_id = None
    _camera_frame = None # 1 frame of the camera
    _actual_mask = None
    _starting_mask = None
    _path_color = None
    _switch_color = None


    def __init__(self, cam_id, path_color):
        print("Camera Object created")
        self._camera_id = cam_id
        self._camera_frame = self._start_capturing()
        self._path_color = path_color
        self._switch_color = path_color[len(path_color)-1]


    def _colored_mask(self, image, lower_color, upper_color):
        return cv.inRange(image, lower_color, upper_color)


    def get_direction(self, enable_windows):
        self._capture_frame(enable_windows)
        width = self._actual_mask.shape[0]
        mask_mean = width // 2

        left_weight = self._actual_mask[:, :mask_mean].sum(dtype=np.int32)
        right_weight = self._actual_mask[:, mask_mean:].sum(dtype=np.int32)

        return (right_weight - left_weight) / (left_weight + right_weight + 1)


    def _capture_frame(self, enable_windows):
        
        img_returned, frame = self._camera_frame.read()

        if not img_returned:
            print("Can't receive frame (stream end?). Exiting ...")
            self._stop_capturing()

        if self._path_color[0] == "blue":
            blue_mask = self._mask_processing(frame, self._lower_blue, self._upper_blue, False)

        elif self._path_color[0] == "red":
            red_mask = self._red_mask_processing(frame, False)
        else:
            yellow_mask = self._mask_processing(frame, self._lower_yellow, self._upper_yellow, False)

        self._starting_mask = self._mask_processing(frame, self._lower_starting_color, self._upper_starting_color, True)

        self._switch_color_path()

        # Shows the actual image processed
        self._enable_windows(enable_windows)


    def _start_capturing(self):
        print("capturing")
        return cv.VideoCapture(self._camera_id)

    def stop_capturing(self):
        self._camera_frame.release()

    def stop_all(self):
        self._camera_frame.release()
        cv.destroyAllWindows()


    def _enable_windows(self, enable_windows):
        if enable_windows:
            cv.imshow("Window", self._actual_mask)
            cv.imshow("Starting_point", self._starting_mask)


    def _has_crossed_starting_line(self):
        # calcul de la détection
        # return True
        # turn += 1
        width = self._starting_mask.shape[0]
        height = self._starting_mask.shape[1]

        weight = self._starting_mask[:,:].sum(dtype=np.int32)

        return weight > 1280000


    def _actualize_mask(self, mask, is_starting_color):
        if not is_starting_color:
            self._actual_mask = mask
        else:
            self._starting_mask = mask


    def _mask_processing(self, frame, lower_color, upper_color, is_starting_color):
        img_cpy = np.copy(frame)
        hsv = cv.cvtColor(img_cpy, cv.COLOR_BGR2HSV)
        mask = self._colored_mask(hsv, lower_color, upper_color)
        self._actualize_mask(mask, is_starting_color)
        return mask


    def _red_mask_processing(self, frame, is_starting_color):
        img_cpy = np.copy(frame)
        hsv = cv.cvtColor(img_cpy, cv.COLOR_BGR2HSV)
        mask0 = self._colored_mask(hsv, self._lower_red0, self._upper_red0)
        mask1 = self._colored_mask(hsv, self._lower_red1, self._upper_red1)
        mask = mask0 + mask1
        hsv[np.where(mask == 0)] = 0
        self._actualize_mask(mask, is_starting_color)
        return mask

    def _switch_color_path(self):
        if self._has_crossed_starting_line():
            if len(self._path_color) > 2:
                np.delete(self._path_color, 0)
        return

    def is_interrupted_key_pressed(self, key):
        if cv.waitKey(1) & 0xFF == ord(key):
            return True
        return False