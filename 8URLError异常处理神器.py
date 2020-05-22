 #-*- coding: UTF-8 -*-
import urllib.request
import urllib.error
import urllib.parse

##一个不存在的连接
#url="http://www.iddddd.com"
#req=urllib.request.Request(url)
#try:
#    urllib.request.urlopen(req)
#except urllib.error.URLError as e:
#    print(e.reason)
#    print(e.code)

##一个服务器存在但连接资源不存在
#url="http://www.badu.com/21212hahahaha0"
#try:
#    urllib.request.urlopen(url)  
#except urllib.error.HTTPError as e:
#    print(e.code)
#    print(e.reason)

try:
    urllib.request.urlopen("http://blog.cs33333dn.net") 
except urllib.error.URLError as e: 
    if hasattr(e,"code"): 
        print(e.code) 
    if hasattr(e,"reason"):
        print(e.reason)