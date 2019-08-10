## Project
Python 3 <br>
OpenCV 4.1.0

Example pet project for lane lines detection based on user defined region of interest (ROI). 

## How to run
Pass a valid video file path to the captureVideo method in the main.py and execute the script (several examples can be found in the data directory). This will load the first frame of the video where the user can manualy select the desired ROI by clicking on the displayed image. Once a valid ROI (minimum 3 points) has been selected, press the "ENTER" key to confirm and start the lane detection or press the "c" key to refresh the image and clear the previously selected points.    
## Results
ROI points

<p align="center">
  <img src="https://raw.githubusercontent.com/sumejko92/lane_lines_detector/master/results/ROI_points.png" width="350" /> 
</p>

Detected lane lines

<img src="https://raw.githubusercontent.com/sumejko92/lane_lines_detector/master/results/Lane1.png" width="250" /> <img src="https://raw.githubusercontent.com/sumejko92/lane_lines_detector/master/results/Lane2.png" width="250" /> <br>
<img src="https://raw.githubusercontent.com/sumejko92/lane_lines_detector/master/results/Lane3.png" width="250" /> <img src="https://raw.githubusercontent.com/sumejko92/lane_lines_detector/master/results/Lane4.png" width="250" />

