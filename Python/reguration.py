#!/usr/bin/python

import re

data="--style_index 21,19 --style_weight 1.0,1.0 --out ~/out.jpg input hogehoge.jpg"


try:
    receive_style_index = re.match(r'.*--style_index (\S+) .*',data).group(1)
except AttributeError:
    receive_style_index = 300
    
try:
    receive_style_weight = re.match(r'.*--style_weight (\S+) .*',data).group(1)
except AttributeError:
    receive_style_weight = 1000
        
try:
    receive_imgname = re.match(r'.*input (\S+\.jpg)',data).group(1)
except AttributeError:
    receive_imgname = "missed.jpg"


print receive_imgname
print receive_style_index
print receive_style_weight
