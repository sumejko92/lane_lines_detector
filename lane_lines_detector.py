import numpy as np
import cv2
import math
from roi_selector import ROISelector


class LaneLinesDetector(object):
    # Image params
    height = 0
    width = 0

    # Canny params
    threshold1 = 100
    threshold2 = 200

    # HoughLinesP params
    rho = 2  # distance resolution in pixels
    theta = np.pi / 180  # angular resolution in radians
    min_votes = 40  # min number of votes
    min_line_len = 30  # min number of pixels for a line 20
    max_line_gap = 100  # max gap in pixels between connectable line segments 10

    def processFrame(self, frame):
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        blured_frame = cv2.GaussianBlur(grayscale_frame, (7, 7), 0)

        canny_frame = cv2.Canny(blured_frame, self.threshold1, self.threshold2)

        mask = np.zeros_like(canny_frame)
        cv2.fillPoly(mask, self.vertices, 255)

        # masked_frame_gray = cv2.bitwise_and(grayscale_frame, mask)
        roi_frame = cv2.bitwise_and(canny_frame, mask)

        result_frame = self.detectLines(frame, roi_frame)

        return result_frame

    def detectLines(self, frame, mask_frame):

        lines = cv2.HoughLinesP(mask_frame, self.rho, self.theta, self.min_votes, np.array([]),
                                minLineLength=self.min_line_len, maxLineGap=self.max_line_gap)

        # return the input frame if no lines were detected
        if lines is None:
            return frame

        line_image = np.zeros((mask_frame.shape[0], mask_frame.shape[1], 3), dtype=np.uint8)

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), [0, 0, 255], 15)

        α = 1
        β = 1
        γ = 0
        Image_with_lines = cv2.addWeighted(frame, α, line_image, β, γ)

        return Image_with_lines

    def captureVideo(self, file_path):
        cap = cv2.VideoCapture(file_path)

        if (cap.isOpened() == False):
            print("Error opening video stream or file")
            exit()

        self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print("Resolution: ", self.width, "x", self.height)

        fps = cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second: ", int(fps))

        print("Click on the image to select ROI vertices (min 3).")
        print("Press >> Enter << to create ROI")
        print("Press >> c << to refresh and clear clicked points")
        # Get ROI vertices
        ret, initial_frame = cap.read()
        roi = ROISelector(initial_frame)
        roi.setROI()

        try:
            roi_pts = roi.getROI()
        except BaseException as err:
            print(err)
            exit(0)

        self.vertices = np.array([roi_pts], dtype=np.int32)

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                lane_lines_frame = self.processFrame(frame)
                cv2.imshow('Lane Lines', lane_lines_frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
