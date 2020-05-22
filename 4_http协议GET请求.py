#GET请求
#非汉字搜索
import urllib.request
keywd="hello"

url="http://www.baidu.com/s?wd="+keywd
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()

fhandle=open("D:/Python/5.html","wb")
fhandle.write(data)
fhandle.close()

#汉字搜索
#urllib.request.quote(汉字) 将汉字编码
import urllib.request
key="聂如意"
key_code=urllib.request.quote(key)
url="http://www.baidu.com/s?wd="+key_code
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()

fhandle=open("D:/Python/6.html","wb")
fhandle.write(data)
fhandle.close()

