#!/usr/bin/python3
import socket

s = socket.socket()
host = socket.gethostname()
port = 80

s.connect((host, port))
print(s.recv(1024))
s.close()
