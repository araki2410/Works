#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import os, sys


pid = os.fork()
if pid == 0:
    os.system("ssh -x gp08 'cd ~/Style32; ./generate2num3.py --color_preserve 1 --net 0808_mobile_ex1 --model style32_080801_out_2.model --style_num 32 --style_index 1,2,3 --style_weight 0.3,0.3,0.4 --out ~/out.jpg tamon.jpg'")
    print ("os system end\n\n")
    sys.exit()
os.wait()

print("perent process\n")
print("child process Id: %d\n" % pid)
