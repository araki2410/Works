#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import cv2
import sys,os
face_cascade = cv2.CascadeClassifier('/usr/local/opencv2411/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/opencv2411/share/OpenCV/haarcascades/haarcascade_mcs_nose.xml')


#img = cv2.imread('./Face/akaruiaraki.jpg')
output_img="./output.jpg"
img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#    roi_gray = gray[y:y+h, x:x+w]
#    roi_color = img[y:y+h, x:x+w]
#    eyes = eye_cascade.detectMultiScale(roi_gray)
#    for (ex,ey,ew,eh) in eyes:
#        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    print x,y,w,h
    xn = w-x
    yn = h-y
    if xn < 0:
        xn = x-w
    if yn < 0:
        yn = y-h
    wn = h+xn+xn
#    hn = w+yn+yn
    hn = wn
    cv2.rectangle(img,(xn,yn),(xn+wn,yn+hn),(255,255,0),2)
print xn, yn, wn, hn
cmd = "convert -crop " + str(wn) + "x" + str(hn) + "+" + str(xn) + "+" + str(yn) + " " + sys.argv[1] + " " + output_img
print cmd
os.system(cmd)
os.system('convert -geometry 250x250 %s %s'%(output_img, output_img))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
