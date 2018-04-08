#!/usr/bin/python

import socket
import os, sys

im = os.system("hostname -a")

hostname= "nboot2.cs.uec.ac.jp"
host = "130.153.192.3"
port = 20004

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

client.send("Im araki-t@%s",im)

response = client.recv(4096)

print response
