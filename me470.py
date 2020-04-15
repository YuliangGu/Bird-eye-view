# ME 470 Senior Design:  Mower Vision
# Yuliang Gu     yuliang3@illinois.edu
# This script is the main module

import numpy as np
import cv2

class Video:
    def __init__(self):
        self.access = []

    def initilize(self,camera_index): # input: a list of camera indices 
        for i in camera_index:
            self.access.append(cv2.VideoCapture(i))

    def cap_frame(self): # output: a list of frames
        ls = [0]
        for i,cam in enumerate(self.access):
            _ , f = cam.read()
            ls[i] = f
        return ls

    def release_cap(self): #release cameras
        for i in self.access:
            i.release()

class Geo_TF:
    def resize(self,img,scale): #
        a = cv2.resize(img,(0,0),fx = scale, fy = scale)
        return a

    def pp_mat(self,src,dst):  # calculate perpective tf matrix
        M = cv2.getPerspectiveTransform(src,dst)
        return M

    def size(self,M,scale):
        H = np.float32([[scale,0,0],[0,scale,0],[0,0,1]])
        return np.matmul(H,M)

    def translate_mat(self,M,x,y):  # input: matrix  output: matrix after translation
        H = np.float32([[1,0,x],[0,1,y],[0,0,1]])
        return np.matmul(H,M)

    def rotate(self,img, angle, center = None, scale = 1.0): # rotate the image
        (h, w) = image.shape[:2]
        if center is None:
            center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(image, M, (w, h))
        return rotated

    def pp_tf(self,img,M,scale = None): #return warped image
        rows,cols,_= img.shape
        if scale == None:
            warped = cv2.warpPerspective(img,M,(cols,rows))
        else:
            warped = cv2.warpPerspective(img,M,(int(cols*scale),int(rows*scale)))
        return warped

    def add(self,img,canvas,x=0,y=0,): # (x,y) is left-corner coordinate
        h,w,_ = img.shape
        roi = canvas[y:y+h,x:x+w]
        roi = cv2.add(img,roi)
        canvas[y:y+h,x:x+w] = roi
        return canvas
