# -*- coding:utf-8 -*-
# Python3

import urllib.request
import urllib.error
import socket

try:
    response = urllib.request.urlopen("https://www.httpbin.org/post",timeout=0.1)
# except urllib.error.URLError as a:
#    print(a.reason)
except urllib.error.URLError as a:
#    print(type(a.reason))
#    print(socket.timeout)
   if isinstance(a.reason, socket.timeout):#isinstance() 函数来判断一个对象是否是一个已知的类型
    print("Time Out.")
