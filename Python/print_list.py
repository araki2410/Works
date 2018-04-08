#!/usr/bin/python

import numpy as np
import os, sys


imgdir = "/export/space/araki-t/Enquete/"
imglist = os.listdir(imgdir)
try:
    imglist.remove("a")
except:
    hoge = "a"
    
print imglist

exit()
num = np.random.randint(0,len(imglist),1)

img = "/export/space/araki-t/Enquete/%s" % imglist[num] #[0]
