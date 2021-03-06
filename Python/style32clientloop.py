#!/usr/bin/python

import socket
import numpy as np
import os, sys
import random
#from time import sleep
hostname= "nboot2.cs.uec.ac.jp" # no need
host = "130.153.192.3"
port = 2410

if '-D' in sys.argv:
    print(sys.argv)
else:
    print("### Caution! This is doublu rope! Transferred_5~8 ###\n### If you OK, try ./style32clientloop -D\n")
    exit()



def clientloop():
    #num = np.random.randint(0,len(imglist),1)
    #img = "%s%s" % (imgdir,imglist[num][0])

    percentage = ["0","0.25","0.5","0.75","1"]
    for imagename in imglist:
        n = 4 # number of styles
        img = "%s%s" % (imgdir, imagename)
        #    styles = np.random.randint(0,31,n)
        styles = random.sample(xrange(32),n) #[0~31,0~31,0~31,0~31] no overlapping
        styles.sort()
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

        client.send("--style_index %s --style_weight %s --out %s --outdir %s %s" %(styles, weight, imagename, outputimagedir, img))

        response = client.recv(1024)

        print img, response
        os.system('echo "%s:%s:%s:0:Ramen" >> %s' % (imagename, styles, weight, resultdata))







n=4
e=20 # 19
imgdir = "/export/space/araki-t/Enquete/Original/"
imglist = np.array(os.listdir(imgdir))
#resultdata = "%sweightdata" % outputimagedir
for i in range(n, e):
    # ./Transferred_n ~ e /
    outputimagedir = "/export/space/araki-t/Enquete/Transferred_%d/" % i
    resultdata = "/export/space/araki-t/Enquete/weightdata_%d" % i
    clientloop()
#    os.system('mv %s %s'%(resultdata, outputimagedir))
    ## /export/.../Enquete/weightdata --> /export/.../Transferred_N/weightdata
