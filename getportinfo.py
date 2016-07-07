#! /usr/bin/env python

import socket

def get_protnumber(prefix):
   return dict( (getattr(socket,a),a) for a in dir(socket) if a.startswith(prefix) )

proto_fam = get_protnumber('AF_')
types = get_protnumber('SOCK_')
protocols = get_protnumber('IPPROTO_')

for res in socket.getaddrinfo('www.google.com','http'):
    family, socktype, proto, cannonname, sockadrr = res
    print 'Family         :', proto_fam[family]
    print 'Type           :', types[socktype]
    print 'Protocol       :',protocols[proto]
    print 'Canonical name :',cannonname
    print 'Socket address :',sockadrr

