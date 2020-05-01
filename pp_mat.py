# ME 470 Senior Design Project
# Authored by Yuliang Gu
# yuliang3@illinois.edu

# Run the script, click on the 4 reference points, and press 'q' to quit
# Output: perspective transformation matrix

import cv2
import numpy as np
from me470 import Geo_TF

geo = Geo_TF()
scale = 1

top_list = np.empty([4,2],dtype=np.float32)
front_list = np.empty([4,2],dtype=np.float32)

count_top = 0
count_fr = 0

top_img = cv2.imread('./setup2/src/birdeye.jpg')
top_img = geo.resize(top_img,scale)
front_img = cv2.imread('./setup2/src/bot.jpg')

cv2.namedWindow('top')
cv2.namedWindow('front')

def coords_top(event,x,y,flags,param):
    global count_top
    if event == cv2.EVENT_LBUTTONDOWN:
        if count_top == 4:
            print('Done!')
        else:
            cv2.circle(top_img,(x,y),15,(0,255,0),-1)
            top_list[count_top] = [x,y]
            count_top += 1

def coords_front(event,x,y,flags,param):
    global count_fr
    if event == cv2.EVENT_LBUTTONDOWN:
        if count_fr == 4:
            print('Done!')
        else:
            cv2.circle(front_img,(x,y),15,(0,255,0),-1)
            front_list[count_fr] = [x,y]
            count_fr += 1

cv2.setMouseCallback('top',coords_top)
cv2.setMouseCallback('front',coords_front)

while(1):
    cv2.imshow('front',front_img)
    cv2.imshow('top',top_img)
    if cv2.waitKey(1)== ord('q'):
        break

M = geo.pp_mat(front_list,top_list)
# M = geo.pp_mat(top_list,front_list)
# print('top list:{}'.format(top_list))
# print('front list:{}'.format(front_list))

print(np.array2string(M, precision=4, separator=',',suppress_small=True))

cv2.destroyAllWindows()
