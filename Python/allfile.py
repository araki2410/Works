#!/usr/bin/python
# -*- coding:utf-8 -*-

# path中のimg画像から特徴量を抽出してハッシュでtokucho.txtに格納します

import commands, os, imghdr, shutil, json, re
#path = "/export/space/araki-t/100img/"
path = "~/Img/araki-t/100img/"

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

print list
#print os.walk("~/Img/")
print os.walk(path)