# coding=utf8
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print s.recv(1024)
while True:
    message = raw_input('Enter you message:')
    s.send(message)
    print s.recv(1024)
    if message == 'exit':
        time.sleep(1)
        s.close()
        break
