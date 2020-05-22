import urllib.request

#模拟成浏览器访问方式访问
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
#方法1：使用build_opener()修改报头
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
#写入本地
fhandle=open("D:/Python/3.html","wb")
fhandle.write(data)
fhandle.close()
#print(data)

#方法2：使用add_opener()添加报头
headers=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
req=urllib.request.Request(url)
req.add_header("User-Agent",headers)
data=urllib.request.urlopen(req).read()
#写入本地
fhandle=open("D:/Python/4.html","wb")
fhandle.write(data)
fhandle.close()
print(data)
