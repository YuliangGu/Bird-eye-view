# This script plots gray_scale value vs frequency

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('birdeye.png')
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.hist(img2gray.ravel(),256,[0,256])
plt.show()
