#!/usr/bin/python
# -*- coding:utf-8 -*-

import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

imgdir = "../../Img/"
imagename = imgdir + "3.png"
futureimage = imgdir + "qrfuture.png"
outimage = imgdir + "out.png" #cut image.
writeimage = imgdir + "result.png" #written square box image.

img = cv2.imread('%s'%(imagename)) #read image.
future = cv2.imread('%s'%(futureimage), 0) #gray scaled by "( ,0)", QR corner square image.

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR image to RGB image.
#print(img) #print each pixel's RGB.

#Set up figures of between Min[] and Max[].
red = np.array([58,30,196],np.uint8) #RED (min and max)
orange = np.array([0, 88, 255],np.uint8) #ORANGE (min and max)
blue_max = np.array([140,255,255],np.uint8)


img = cv2.inRange(img, red, red)#(read_img, min, max)
#img = cv2.inRange(img, red, orange) #red ~ orange
cv2.imwrite("%s"%(outimage),img) #Output image.

img = cv2.imread("%s"%(outimage),0) #KUSO cord, reread outputed image.
result = cv2.matchTemplate(img, future, cv2.TM_CCOEFF_NORMED) #matching by TM_CCOEFF_NORMED method.

#Locate matchied grid .
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #(x,y),(x,y)
top_left = max_loc
w, h = future.shape[::-1]
bottom_right = (top_left[0] + w, top_left[1] + h)

#write square box
# result = cv2.imread("%s"%(imagename)) #Background layer
# cv2.rectangle(result,top_left, bottom_right, (255, 255, 0), 2) #write box by 
# cv2.imwrite("%s"%(writeimage), result) #write "result" in "writeimage" 



### check all matching location...
threshold = 0.9 #how neir(0~1)
loc = np.where(result >= threshold) #get locations
result = cv2.imread(imagename)
w, h = future.shape[::1]#qrfuture.png s width and height (same score).

#loc = np.array(loc).T ##add transpose code. ???


for top_left in zip(*loc[::1]):
    stack = np.array(top_left) #(A) transpose (tuple to array to tuple)
    swap = stack[0]            #(A)
    stack[0] = stack[1]        #(A)
    stack[1] = swap            #(A)
    top_left = tuple(stack)    #(A) (y,x)=>(x,y)
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print top_left, bottom_right

    cv2.rectangle(result, tuple(top_left), bottom_right, (255, 255, 0), 2)#(~, 2) 2px
cv2.imwrite(writeimage, result)
