# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu

# Offline version for demo

import cv2
import threading
import numpy as np
from me470 import Geo_TF

geo = Geo_TF()

'''Load video files'''
cap_top = cv2.VideoCapture('./videos/top.avi')
cap_left = cv2.VideoCapture('./videos/left.avi')
cap_right = cv2.VideoCapture('./videos/right.avi')
cap_bot = cv2.VideoCapture('./videos/bot.avi')

''' Transformation matrices from generate_warped.py'''
M_top = np.float32([[  -3.8658,  -9.3394,4175.655 ],
 [   0.3243, -14.1634,4167.4443],
 [   0.0007,  -0.0173,   1.    ]])
M_left =np.float32([[  -3.707 ,   6.2256,3965.1167],
 [  -0.0678,  -2.8551,3128.9346],
 [  -0.0011,   0.0102,   1.    ]])
M_right =np.float32([[  -0.0215,   0.7568,-764.8566],
 [  -0.4719,  -1.8913,1150.316 ],
 [   0.0002,  -0.0032,   1.    ]])
M_bot =np.float32([[   0.0233,  -2.5104,1271.7194],
 [   0.556 ,  -2.1901, 215.0773],
 [   0.0001,  -0.0031,   1.    ]])

''' Function for blending images (using params from blending.py)'''
def blending(list_images):
    warped_t,warped_r,warped_l,warped_b = list_images
    canvas_1 = np.zeros(shape = [1800,1700,3], dtype = np.uint8)
    canvas_2 = np.zeros(shape = [1800,1700,3], dtype = np.uint8)
    img_t = geo.add(warped_t,canvas_1,x=300,y = 0)  # add top to the canvas
    img_tb = geo.add(warped_b,img_t,x=170,y=1100)   # add bottom
    copy = img_tb.copy()                            # make a copy
    img_tbr = geo.add(warped_r,canvas_2,x = 1050,y=250) # add right
    img_ = geo.add(warped_l,img_tbr,x=0,y=100)          # add left
    img2gray = cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY)              # convert to grayscale
    _ , mask = cv2.threshold(img2gray,1, 255, cv2.THRESH_BINARY)  # obtain mask
    mask_inv = cv2.bitwise_not(mask)                              # inverse mask
    over_not = cv2.bitwise_and(img_,img_,mask=mask_inv)
    img = geo.add(over_not,copy)
    return img

'''Function to warp images with given TF matrices'''
def warp(img1,img2,img3,img4,x=1280,y=640): # (x,y) shape of the wapred image
    top = cv2.warpPerspective(img1,M_top,(x,y))
    right = cv2.warpPerspective(img2,M_right,(x,y))
    left = cv2.warpPerspective(img3,M_left,(x,y))
    bot = cv2.warpPerspective(img4,M_bot,(x,y))
    return [top,right,left,bot]

while cap_top.isOpened():
    _,f_top = cap_top.read()
    _,f_left = cap_left.read()
    _,f_right = cap_right.read()
    _,f_bot = cap_bot.read()
    ls = warp(f_top,f_right,f_left,f_bot)
    img = blending(ls)
    cv2.imshow('window-name',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap_top.release()
cap_right.release()
cap_left.release()
cap_bot.release()
cv2.destroyAllWindows()  # destroy all the opened windows
