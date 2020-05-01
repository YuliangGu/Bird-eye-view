# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu
# This script generates warped videop

import cv2
import numpy as np
from me470 import Geo_TF

'''Load video files'''
cap_top = cv2.VideoCapture('./videos/top.avi')

M_top = np.float32([[  -3.8658,  -9.3394,4175.655 ],
 [   0.3243, -14.1634,4167.4443],
 [   0.0007,  -0.0173,   1.    ]])

for i in range(100):
    _,ftop = cap_top.read()
    f_top = cv2.resize(ftop,(1920,1080))
    warped = cv2.warpPerspective(f_top,M_top,(1280,640))
    cv2.imwrite('./test_imgs/test.png',warped)
    cv2.imshow('window-name',warped)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

print(f_top.shape)
cap_top.release()
cv2.destroyAllWindows()  # destroy all the opened windows
