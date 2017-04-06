# coding=utf8
import socket
import threading
import time


def sockResp(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(3)
        if data == 'exit':
            break
        print data
        sock.send('You message is: %s!' % data)
    sock.close()
    print 'Connection from %s:%s is closed.' % addr


host = '127.0.0.1'
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print 'Waiting for connection...'
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=sockResp, args=(sock, addr))
    t.start()

