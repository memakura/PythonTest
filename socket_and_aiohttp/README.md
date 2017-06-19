# PythonTest/sock_and_aiohttp - How to Use
Small codes for Python

- python 3.5
- windows 10 command line

## Simple Socket Test
Console 1
```
python socket_server.py
```

Cosole 2
```
python socket_multiclient.py
```

Result of Console 1
```
start accepting...
--- accept() is called...start connection...
Connected by  ('127.0.0.1', 62298)
wait client's sending data
Received data:  Hello world!
wait client's sending data
Received data:
--- closing...
--- accept() is called...start connection...
Connected by  ('127.0.0.1', 62299)
wait client's sending data
Received data:  Hello world!
wait client's sending data
Received data:
--- closing...
```

### Stopping server
- Console1: Ctrl + C 
- Console2: `python socket_client.py`
Then the server will be terminated. If not, press enter at the console 1.

## Simple Threading Socket Test
Console 1
```
python socket_threadingserver.py
```

Cosole 2
```
python socket_multiclient.py
```

Result of Console 1
```
start accepting...
--- accept() is called...start connection...
Connected by  ('127.0.0.1', 62617)
--- accept() is called...start connection...
wait client's sending data
Connected by  ('127.0.0.1', 62618)
wait client's sending data
Received data:  Hello world!
Received data:  Hello world!
wait client's sending data
wait client's sending data
Received data:
Received data:
--- closing...
--- closing...
```

## Simple Asynchronous I/O Socket Test
Console 1
```
python socket_asyncserver.py
```

Cosole 2
```
python socket_multiclient.py
```

Result of Console 1
```
start accepting...
--- accept() is called...start connection...
Connected by  ('127.0.0.1', 62726)
wait client's sending data
--- accept() is called...start connection...
Connected by  ('127.0.0.1', 62727)
wait client's sending data
Received data:  Hello world!
wait client's sending data
Received data:
--- closing...
Received data:  Hello world!
wait client's sending data
Received data:
--- closing...
```

## aiohttp
- The example codes are from http://aiohttp.readthedocs.io/
- Samples of asyncio, etc: https://www.pythonsheets.com/notes/python-asyncio.html

Installation
```
pip install aiohttp
```

Console 1
```
python simpe_http_server.py
```

Console 2 (bash)
```
nc localhost 8888 (Enter)
GET /hoge HTTP/1.1 (Enter)
(Enter)
```

Result of Console 2
```
GET /hello HTTP/1.1

HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 12
Date: Mon, 19 Jun 2017 00:11:25 GMT
Server: Python/3.5 aiohttp/2.1.0

Hello, hoge
```

## Low-level aiohttp
- aiohttp as a Protocol in asyncio (how to get handler) : https://www.pythonsheets.com/notes/python-asyncio.html

