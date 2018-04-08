#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import urllib2

url = "http://zipcloud.ibsnet.co.jp/api/search"

response = urllib2.urlopen(url)
json_data = json.loads(response.read())

print json.dumps(json_data, indent=2)
