# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu

# Test_version (not finshed yet)

import cv2
import threading
import time
import numpy as np
from me470 import Video,Geo_TF
x = 50

geo = Geo_TF()
i = Video()
i.initilize([2])

top = np.float32([[231. , 56.],
 [451. , 56.],
 [469., 397.],
 [226., 399.]]

)
fr = np.float32([[229., 141.],
 [444., 138.],
 [572., 419.],
 [113., 434.]]
)
frame_width = 1000
frame_height = 700

out= cv2.VideoWriter('front.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))
out_warped = cv2.VideoWriter('warped.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

M = geo.pp_mat(fr,top)
M = geo.translate_mat(M,150,120)

while(1):
    img = i.cap_frame()[0]
    warped = cv2.warpPerspective(img,M,(1000,700))
    out.write(img)
    out_warped.write(warped)
    cv2.imshow('result',warped)
    cv2.imshow('normal',img)
    if cv2.waitKey(1)== ord('q'):
        break

i.release_cap()
cv2.destroyAllWindows()
