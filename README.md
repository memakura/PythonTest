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

## asynchttp
- http://aiohttp.readthedocs.io/en/stable
    - asynchttp as a Protocol in asyncio (how to get handler)
- Samples of asyncio, etc: https://www.pythonsheets.com/notes/python-asyncio.html

Installation
```
pip install asynchttp
```

Console 1
```
python simpe_http_server.py
```

Console 2 (bash)
```
nc localhost 8888 (Enter)
GET /hello HTTP/1.1 (Enter)
(Enter)
```
