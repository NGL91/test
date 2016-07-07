#! /usr/bin/env python

import socket

host = '127.0.0.1'
portlist = range(0,65536)

for port in portlist:
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   res = sock.connect_ex((host, port))
   if res == 0:
      try:
         protocol = socket.getservbyport(port)   
         print port,':',res,':',protocol
      except:
         print port,":",res
   sock.close()

