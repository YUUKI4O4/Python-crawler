# -*- coding:utf-8 -*-
# Python3
import urllib.request#加载urllib库中的request模块
import urllib.parse#加载urllib库中的parse模块

data = bytes(urllib.parse.urlencode({"name":"admin"}), encoding="utf-8")#bytes转换数据结构为二进制，利用parse模块中的urlencode方法以utf-8的编码格式，将字典参数转换为字符串
response = urllib.request.urlopen("https://www.httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
