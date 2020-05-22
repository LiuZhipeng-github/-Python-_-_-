import urllib.request

#timeout
url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
for i in range(1,100):
    try:
        file=urllib.request.urlopen(url,timeout=1)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+str(e))
