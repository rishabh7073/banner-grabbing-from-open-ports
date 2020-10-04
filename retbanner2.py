#!/usr/bin/python

import socket

def retbanner2(ip,port):
              try:
                  socket.setdefaulttimeout(2)
                  s=socket.socket()
                  s.connect((ip,port))
                  banner=s.recv(1024)
                  return banner
              except:
                    return 
def main():
        
          ip=raw_input("[*]Enter Targrt IP: ")
          for port in range(1,65535):
                     banner=retbanner2(ip,port)
                     if banner:
                              print "[+]"+ip+": "+banner
main()
