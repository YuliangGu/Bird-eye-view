# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu
# This script tests cameras

import cv2
import numpy as np
from me470 import Video

i = Video()             # initilize the Video class
camera_index = [0]      # use lsusb command(Linux) to obtain the camera index

i.initilize(camera_index) #initilize the camera

while(1):
    ls = i.cap_frame()              #capture a frame
    cv2.imshow('result',ls[0])      #show the frame
    if cv2.waitKey(1)== ord('q'):   # press q to exit
        break

i.release_cap()
cv2.destroyAllWindows()
