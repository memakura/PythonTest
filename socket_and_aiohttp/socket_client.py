# coding: utf-8

import socket
import time

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with sock:
        sock.connect(('localhost', 8888))
        time.sleep(2)
        sock.sendall(b'Hello world!')
        data = sock.recv(1024)
    print('Received', data.decode())
    return

if __name__ == '__main__':
    main()
