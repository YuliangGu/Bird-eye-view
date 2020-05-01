# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu
# This script generates warped image

import cv2
import numpy as np
from me470 import Geo_TF

front_img = cv2.imread('./setup2/src/top.jpg')  #Original size [1920,1080]
top_img = cv2.imread('./setup2/src/birdeye.jpg')
# print(front_img.shape)
geo = Geo_TF()

'''Note: manually adjust (x,y) to obtain the desired image'''
x,y = -1100,-2300

'''This transformation matrix is generated from pp_mat.py'''
M = np.float32([[  -17.7439,   54.5577,16988.7206],
 [   -4.1254,   38.967 ,16218.2366],
 [   -0.0018,    0.0238,    1.    ]])

M = geo.translate_mat(M,x,y)
M = geo.size(M,0.5)  # Change this scaling factor to resize the image

''' Copy paste this TF matrix to video.py '''
print(np.array2string(M, precision=4, separator=',',suppress_small=True))

warped = cv2.warpPerspective(front_img,M,(1280,640))
# warped = cv2.warpPerspective(front_img,M,(1280,640))  #size: (1280,640)
cv2.imwrite('./setup2/warped/warped_bot_test.png',warped)

while(1):
    cv2.imshow('warped',warped)
    if cv2.waitKey(1)== ord('q'):
        break

cv2.destroyAllWindows()
