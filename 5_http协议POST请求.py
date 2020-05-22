#POST请求
#1）设置好URL网址。
#2）构建表单数据，并使用urllib.parse.urlencode对数据进行编码 处理。
#3）创建Request对象，参数包括URL地址和要传递的数据。 
#4）使用add_header（）添加头信息，模拟浏览器进行爬取。 
#5）使用urllib.request.urlopen（）打开对应的Request对象，完成 信息的传递。 
#6）后续处理，比如读取网页内容、将内容写入文件等。
import urllib.request
import urllib.parse

url="http://www.iqianyue.com/mypost/"
headers=('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')

postdata=urllib.parse.urlencode({
"name":"ceo@iqianyue.com", "pass":"aA123456" }).encode('utf-8')#将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
req=urllib.request.Request(url,postdata)
req.add_header("User-Agent",headers)
data=urllib.request.urlopen(req).read()
print(len(data))
fhandle=open("D:/Python/7.html","wb")
fhandle.write(data)
fhandle.close()

