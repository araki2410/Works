#!/usr/bin/python

import socket
import os, sys

hostname = "nboot2.cs.uec.ac.jp"
host = "130.153.192.3"
port = 20004

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port))
serversock.listen(10)

while True:
    print 'Waiting for connections...'
    clientsock, client_address = serversock.accept()

    while True:
        rcvmsg = clientsock.recv(1024)
        print 'Received -> %s' % (rcvmsg)
        if rcvmsg == '':
            break
        print 'Type message...'
        s_msg = raw_input()
        if s_msg == '':
            break
        print 'Wait...'

        clientsock.sendall(s_msg)
clientsock.close()
