#!/usr/bin/python3
import socket

s = socket.socket()
host = socket.gethostname()
port = 80
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("got connection from ")
    print("HELLO SOCKET 80")
    s.send(str.encode('Hiya!'))
    s.close()
