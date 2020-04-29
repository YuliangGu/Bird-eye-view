# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu
# This script generates warped image

import cv2
import numpy as np
from me470 import Geo_TF

front_img = cv2.imread('./setup2/src/right.jpg')  #Original size [1920,1080]
top_img = cv2.imread('./setup2/src/birdeye.jpg')

geo = Geo_TF()

'''Note: manually adjust (x,y) to obtain the desired image'''
x,y = -750,-500

'''This transformation matrix is generated from pp_mat.py'''
M = np.float32([[   0.1217,  -7.3459,3293.4387],
 [   1.1619,  -5.9302, 930.1546],
 [   0.0001,  -0.0031,   1.    ]])

M = geo.translate_mat(M,x,y)
M = geo.size(M,0.5)

''' Copy paste this TF matrix to video.py '''
print(np.array2string(M, precision=4, separator=',',suppress_small=True))

warped = cv2.warpPerspective(front_img,M,(640,1280))
# warped = cv2.warpPerspective(front_img,M,(1280,640))  #size: (1280,640)
cv2.imwrite('./setup2/warped/warped_left.png',warped)

while(1):
    cv2.imshow('warped',warped)
    if cv2.waitKey(1)== ord('q'):
        break

cv2.destroyAllWindows()
