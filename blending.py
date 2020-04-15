# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu
# This script generates the composite bird eye view

import cv2
import numpy as np
from me470 import Geo_TF

geo = Geo_TF()

# Load Images
warped_r = cv2.imread('warped_right.png')
warped_t = cv2.imread('warped_top.png')
warped_l = cv2.imread('warped_left.png')
warped_b =cv2.imread('warped_bot.png')

# Background
canvas_1 = np.zeros(shape = [1800,1700,3], dtype = np.uint8)
canvas_2 = np.zeros(shape = [1800,1700,3], dtype = np.uint8)

# Manually adjust (x,y) to line up images
img_t = geo.add(warped_t,canvas_1,x=300,y = 0)  # add top to the canvas
img_tb = geo.add(warped_b,img_t,x=170,y=1100)   # add bottom
copy = img_tb.copy()                            # make a copy

img_tbr = geo.add(warped_r,canvas_2,x = 1050,y=250) # add right
img_ = geo.add(warped_l,img_tbr,x=0,y=100)          # add left

# img_example = geo.add(img_,img_tb)

# Find the mask of overlapping region
img2gray = cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY)              # convert to grayscale
_ , mask = cv2.threshold(img2gray,1, 255, cv2.THRESH_BINARY)  # obtain mask
mask_inv = cv2.bitwise_not(mask)                              # inverse mask

over_not = cv2.bitwise_and(img_,img_,mask=mask_inv)           #
img = geo.add(over_not,copy)

# cv2.imwrite('birdeye.png',copy)

while(1):
    cv2.imshow('bird eye view',img_)
    if cv2.waitKey(1)== ord('q'):
        break

cv2.destroyAllWindows()
