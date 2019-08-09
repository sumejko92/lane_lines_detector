from lane_lines_detector import LaneLinesDetector

if __name__ == '__main__':
    detector = LaneLinesDetector()
    detector.captureVideo('data/solidWhiteRight.mp4')
