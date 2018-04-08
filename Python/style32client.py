#!/usr/bin/python

import socket
import numpy as np
import os, sys
hostname= "nboot2.cs.uec.ac.jp" # no need
host = "130.153.192.3"
port = 2410

imgdir = "/export/space/araki-t/Enquete/Original/"
imglist = np.array(os.listdir(imgdir))
num = np.random.randint(0,len(imglist),1)

img = "%s%s" % (imgdir,imglist[num][0])

n = 4 # number of styles
styles = np.random.randint(0,31,n)
percentage = ["0","0.25","0.5","0.75","1"]
weight = []
while n > 0:
    i =  np.random.randint(0,len(percentage),1)[0]
    weight.append(percentage[i])
    n -= 1
weight = ",".join(weight) #[0.25,1,0.5,0]
styles = ",".join(map(str, styles)) #[a,b,c,d] # style's numbers
print styles, weight

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

client.send("--style_index %s --style_weight %s %s" %(styles, weight, img))

response = client.recv(1024)

print img, response
