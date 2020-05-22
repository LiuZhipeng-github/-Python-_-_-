import urllib.request
import urllib.error
import re
def getlink(url):
    #模拟成浏览器
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')  
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    file=urllib.request.urlopen(url)
    data=str(file.read())
    #根据需求构建好连接表达式
    pat='(https?://[^\s)";]+\.(\w|/)*)'
    link=re.compile(pat).findall(data)
    #去除重复元素
    link=list(set(link))
    return link
#要爬取的网页
url="http://blog.csdn.net/"
#获取对应网页中的连接地址
linklist=getlink(url)
#通过for循环分别遍历输出获取到的连接地址到屏幕上
for link in linklist:   
    print(link[0])
