#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import sys


list = {}
hashed = {}
hashed["data"] = []
hashed["id"] = "hoge"
hashed["usename"] = "荒木勇人"
hashed["image"] = "http://naruhiyoko.ddns.net/data/debug.jpg"
hashed["data"] = []


hashed["data"].append({"question":"電話番号", "answer":"042(443)5102"})
hashed["data"].append({"question":"mail", "answer":"araki-t@mm.inf.uec.ac.jp"})
hashed["data"].append({"question":"生年月日", "answer":"1918-12-08"})


# def echo():
#     print("Enter new Question:")
#     que = raw_input()
#     print("Enter The Answer:")
#     ans = raw_input()
# #    print("Q:%s\nA:%s"%(que,ans))
#     list["question"] = que
#     list["answer"] = ans
# #    hashed[data]=dict([("question",que),("answer",ans)])
#     hashed["data"].append(list)
# for i in range(3):
#     echo()




#list =

print hashed

openfile = open('./entry.json','w')
json.dump(hashed, openfile, ensure_ascii=False)
