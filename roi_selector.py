import cv2
import numpy as np


class ROISelector(object):
    def __init__(self, image_in):
        self.image = image_in
        self.image_copy = self.image.copy()
        self.points = []
        self.window_name = 'ROI selection'

    def getCoords(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(self.image, (x, y), 5, (255, 0, 0), -1)
            point = (x, y)
            self.points.append(point)

            print(point)

    def setROI(self):
        print('Select points on the image to define ROI')
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.getCoords)

        while(cv2.getWindowProperty(self.window_name, 0) >= 0):
            cv2.imshow(self.window_name, self.image)
            k = cv2.waitKey(20) & 0xFF
            if k == 13:
                break
            elif k == ord('c'):
                print('Points cleared. Select new points')
                self.points.clear()
                self.image = self.image_copy.copy()

        cv2.destroyAllWindows()

    def getROI(self):
        if len(self.points) < 3:
            raise Exception('ERROR: Invalid number of points for ROI')
        else:
            return self.points
