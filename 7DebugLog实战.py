import urllib.request
httphd=urllib.request.HTTPHandler(debuglevel=1)
httpshd=urllib.request.HTTPSHandler(debuglevel=1)
opener=urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data=urllib.request.urlopen("http://baidu.com").read()
#print(data)

#写入本地
fhandle=open("D:/Python/8.html","wb")
fhandle.write(data)
fhandle.close()

