# coding: utf-8

import socket
import time
import threading

def connect_to_server(id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with sock:
        print('Connecting: id=', id)
        sock.connect(('localhost', 8888))
        time.sleep(2)
        sock.sendall(b'Hello world!')
        data = sock.recv(1024)
    print('Received', data.decode())
    return

def main():
    nclients = 2
    for i in range(0,nclients):
        threadhandle = threading.Thread(target=connect_to_server, args=(i,))
        threadhandle.start()

    return

if __name__ == '__main__':
    main()
