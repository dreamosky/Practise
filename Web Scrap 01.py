import socket
import urllib.request
import urllib.error

try:
    res=urllib.request.urlopen('https://httpbin.org/get',timeout=0.3)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
     print('TIME OUT')
