# coding: utf-8

import socket
import threading

def handler(conn, addr):
    with conn:
        print('Connected by ', addr)
        while True:
            print("wait client's sending data")
            data = conn.recv(1024)
            print('Received data: ', data.decode())
            if not data: break
            conn.sendall(data)
    print('--- closing...')
    
    return

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with sock:
        sock.bind(('localhost', 8888))
        sock.listen(1)
        print('start accepting...')
        while True:
            conn, addr = sock.accept()
            print('--- accept() is called...start connection...') # accept でブロックされる
            threadhandle = threading.Thread(target=handler, args=(conn,addr), daemon=True)
            threadhandle.start()
    return

if __name__ == '__main__':
    main()
