#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import cv2
import sys,os
face_cascade = cv2.CascadeClassifier('/usr/local/opencv2411/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/opencv2411/share/OpenCV/haarcascades/haarcascade_mcs_nose.xml')


#img = cv2.imread('./Face/akaruiaraki.jpg')
output_img="./Face/output.jpg"
try:
    img = cv2.imread(sys.argv[1])
    height, width = img.shape[:2]
except:
    print(" Error: too few argument.\n Please execute:\n\t./facedetection.py [imagefile]")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#    roi_gray = gray[y:y+h, x:x+w]
#    roi_color = img[y:y+h, x:x+w]
#    eyes = eye_cascade.detectMultiScale(roi_gray)
#    for (ex,ey,ew,eh) in eyes:
#        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    xn = x-w
    yn = y-h
    wn = x+w+w
    hn = y+h+h
    if xn < 0:
        xn = 0
    if yn < 0:
        yn = 0
    if wn > width:
        wn = width
    if hn > height:
        hn = height
    cv2.rectangle(img,(xn,yn),(wn,hn),(255,255,0),2)
print x,y,w,h
print xn, yn, wn, hn
print width, height
cmd = "convert -crop " + str(wn) + "x" + str(wn) + "+" + str(xn) + "+" + str(yn) + " " + sys.argv[1] + " " + output_img
print cmd
os.system(cmd)
os.system('convert -geometry 250x250 %s %s'%(output_img, output_img))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
