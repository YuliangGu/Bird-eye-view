# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu
# This script generates warped image

import cv2
import numpy as np
from me470 import Geo_TF

front_img = cv2.imread('./src_pics/bot.jpg')
top_img = cv2.imread('./src_pics/fisheye.jpg')

geo = Geo_TF()

x,y = 0,-1150   # Note: manually adjust (x,y) to obtain the desired image

# This transformation matrix is generated from pp_mat.py
M = np.float32([[ 0.6732,-1.9764,27.8993],
 [-0.1401,-2.3433,73.0916],
 [-0.0001,-0.003 , 1.    ]])

M = geo.translate_mat(M,x,y)
M = geo.size(M,1)
print(np.array2string(M, precision=4, separator=',',suppress_small=True))

warped = cv2.warpPerspective(front_img,M,(1280,640))   # size: (1280,640)
cv2.imwrite('warped_bot.png',warped)

while(1):
    cv2.imshow('warped',warped)
    if cv2.waitKey(1)== ord('q'):
        break

cv2.destroyAllWindows()
