# -*- coding:utf-8 -*-
# Python3
import urllib.request#加载urllib库中的request模块

response = urllib.request.urlopen("https://baidu.com")#使用request模块的urlopen方法访问网站
print(type(response))#response是一个类，可以通过一些方法来输出想要的结果
print(response.read().decode("utf-8"))#通过read方法输出相应体，并通过utf-8解码
print(response.getheaders())#通过getheaders方法获取响应头信息
print(response.getheader('Server'))
print(response.fileno())
print(response.msg)#获取响应中的msg属性
print(response.version)
print(response.status)
print(response.reason)
print(response.debuglevel)
print(response.closed)
