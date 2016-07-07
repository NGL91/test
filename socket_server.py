#! /usr/bin/env python

import socket
host = "127.0.0.1" #Server address
port = 12345 #Port of Server

print 'host=',socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind server
s.listen(2)

index = 0
while index <2:
   index +=1
   conn, addr = s.accept()
   print addr, "Now Connected"
   conn.send("Thanks")
   conn.close()

