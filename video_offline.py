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

M_left =np.float32([[    0.0514,   -6.3021, 2732.9204],
 [    1.9876,   -4.3249,-1258.1794],
 [    0.0001,   -0.0069,    1.    ]])

M_right =np.float32([[  -0.0215,   0.7568,-764.8566],
 [  -0.4719,  -1.8913,1150.316 ],
 [   0.0002,  -0.0032,   1.    ]])

M_bot =np.float32([[  -7.882 ,  14.1889,7944.3604],
 [   0.0073,  -7.8865,6959.118 ],
 [  -0.0018,   0.0238,   1.    ]])

''' Function for blending images (using params from blending.py)'''
def blending(warped_t,warped_r,warped_l,warped_b):
    canvas_1 = np.zeros(shape = [1700,1700,3], dtype = np.uint8)
    canvas_2 = np.zeros(shape = [1700,1700,3], dtype = np.uint8)
    img_t = geo.add(warped_t,canvas_1,x=200,y = 0)  # add top to the canvas
    img_tb = geo.add(warped_b,img_t,x=170,y=1000)   # add bottom
    copy = img_tb.copy()                            # make a copy
    img_tbr = geo.add(warped_r,canvas_2,x = 1050,y=200) # add right
    img_ = geo.add(warped_l,img_tbr,x=0,y=100)          # add left
    img2gray = cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY)              # convert to grayscale
    _ , mask = cv2.threshold(img2gray,1, 255, cv2.THRESH_BINARY)  # obtain mask
    mask_inv = cv2.bitwise_not(mask)                              # inverse mask
    over_not = cv2.bitwise_and(img_,img_,mask=mask_inv)
    img = geo.add(over_not,copy)
    return img

out = cv2.VideoWriter('./videos/birdeye.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 20, (1700,1700))

while cap_top.isOpened():
    _,f_top = cap_top.read()
    _,f_left = cap_left.read()
    _,f_right = cap_right.read()
    _,f_bot = cap_bot.read()
    img_t = cv2.resize(f_top,(1920,1080))
    img_l = cv2.resize(f_left,(1920,1080))
    img_r = cv2.resize(f_right,(1920,1080))
    img_b = cv2.resize(f_bot,(1920,1080))
    t_w = cv2.warpPerspective(img_t,M_top,(1280,640))
    r_w = cv2.warpPerspective(img_r,M_right,(640,1280))
    l_w  = cv2.warpPerspective(img_l,M_left,(640,1280))
    b_w = cv2.warpPerspective(img_b,M_bot,(1280,640))
    img = blending(t_w,r_w,l_w,b_w)
    out.write(img)
    cv2.imshow('birdeye',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap_top.release()
cap_right.release()
cap_left.release()
cap_bot.release()
cv2.destroyAllWindows()  # destroy all the opened windows
