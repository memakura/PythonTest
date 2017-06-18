# coding: utf-8

import socket
import asyncio
#from contextlib import closing

async def handler(conn, addr, loop):
#    with conn:
    print('Connected by ', addr)
    while True:
        print("wait client's sending data")
        data = await loop.sock_recv(conn, 1024)
        print('Received data: ', data.decode())
        if not data: break
        await loop.sock_sendall(conn, data)
    print('--- closing...')
    conn.close()
    
    return

async def server(loop, sock):
    while True:
        conn, addr = await loop.sock_accept(sock)
        print('--- accept() is called...start connection...') # accept でブロックされる
        loop.create_task(handler(conn, addr, loop))
    return

def main():
    loop = asyncio.get_event_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 #   with sock, closing(loop):
    sock.setblocking(False)
    sock.bind(('localhost', 8888))
    sock.listen(1)
    print('start accepting...')
    loop.create_task(server(loop, sock))
    #loop.run_forever()
    try:
        loop.run_until_complete(server(loop, sock))
    except KeyboardInterupt:
        pass
    finally:
        loop.close()
        sock.close()
    return

if __name__ == '__main__':
    main()
