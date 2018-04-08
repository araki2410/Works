#!/usr/bin/python
# -*- coding:utf-8 -*-

# path中のimg画像から特徴量を抽出してハッシュでtokucho.txtに格納します

import commands, os,imghdr,shutil, json
path = "/export/space/araki-t/100img/"
#path = "./Img/100img/"
filename = "tokucho.json"
tokucho = {}

def get_image_list(path):
    file_list = []
    for (root, dirs, files) in os.walk(path): # 再帰的に探索
        for file in files: # ファイル名だけ取得
            target = os.path.join(root,file).replace("\\", "/")  # フルパス取得
            if os.path.isfile(target): # ファイルかどうか判別
                if imghdr.what(target) != None : # 画像ファイルかどうかの判別
                    file_list.append(target) # 画像ファイルであればリストに追加
    return file_list

list = get_image_list(path)


for file in list:
    hoge = commands.getoutput("./resize_img %s %s 231 -3" % (file,file))

# gabor = commands.getoutput("~yanai/Pub/im/gabor/gabor /export/space/araki-t/100img/crow.jpg 2 2")
print hoge
