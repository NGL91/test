#! /usr/bin/env python

import socket

host='127.0.0.1'
port=12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#print s.recv(1024)

buf = bytearray('-' *30)
print 'Number of Bytes',s.recv_into(buf)
print buf


s.send('Hello Server')
s.close()
