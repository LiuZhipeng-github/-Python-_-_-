# python爬虫 基础

## 1，基础知识

### 1，一般访问 urlopen
file=urllib.request.urlopen("http://www.baidu.com")


- import urllib.request
file=urllib.request.urlopen("http://www.baidu.com")
data=file.read()
dataline=file.readlines()
#print(data)
#print(dataline)

#Method1
fhandle=open("D:/Python/1.html","wb")//"wb"，二进制格式
fhandle.write(data)
fhandle.close()

#Method2
filename=urllib.request.urlretrieve("http://www.163.com",filename="D:/Python/2.html")
urllib.request.urlcleanup()

#检测状态
#file.info()
#print(file)
file.getcode()
print(file)
file.geturl()
print(file)

	- 

### 2，urllib.request

- #模拟成浏览器访问方式访问
#方法1：使用build_opener()修改报头

	- 

- #方法2：使用add_opener()添加报头

	- 

- import urllib.request

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


### 3，超时
urllib.request.urlopen(url,timeout=1)

- import urllib.request

#timeout
url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
for i in range(1,100):
    try:
        file=urllib.request.urlopen(url,timeout=1)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+str(e))

	- 

		- 

### 4，HTTP协议请求

- 1.GET请求实例
baidu查询"hello"
该网址为：https://www.baidu.com/s?ie=utf8&wd=hello&tn=87048150_dg，字段ie的值为utf8，代表的是编码信息，而字段wd为hello，刚好是我们要查询的信息，所以字段wd应该存储的就是用户带检索的关键词。

根据我们的猜测，简化一下该网址，可以简化为：https://www.baidu.com/s?wd=hello，此时只包含了对应的wd字段，即待检索关键词字段，将该网址复制到浏览器中，刷新一下，发现该网址也能够出现关键词为“hello”的搜索结果。

	- 百度上查询一个关键词时，会使用GET请求进行，其中关键性字段是 wd，网址的格式是："https://www.baidu.com/s?wd=关键词"

通过以上实例我们可以知道，如果要使用GET请求，思路如下： 
1）构建对应的URL地址，该URL地址包含GET请求的字段名和 字段内容等信息，并且URL地址满足GET请求的格式，
即“http://网 址？字段名1=字段内容1&字段名2=字段内容2”。 
2）以对应的URL为参数，构建Request对象。 3）通过urlopen（）打开构建的Request对象。
 4）按需求进行后续的处理操作，比如读取网页的内容、将内容 写入文件等

		- #GET请求
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


			- 非汉字搜索
			- 汉字搜索

- 2.POST请求实例
#POST请求
#1）设置好URL网址。
#2）构建表单数据，并使用urllib.parse.urlencode对数据进行编码 处理。
#3）创建Request对象，参数包括URL地址和要传递的数据。 
#4）使用add_header（）添加头信息，模拟浏览器进行爬取。 
#5）使用urllib.request.urlopen（）打开对应的Request对象，完成 信息的传递。 
#6）后续处理，比如读取网页内容、将内容写入文件等。

	- 

### 5，代理服务器设置

- 
使用urllib.request.ProxyHandler（）来设置对应的代理服 务器信息，
设置格式为：urllib.request.ProxyHandler（{'http'：代理服 务器地址}），
接下来，使用urllib.request.build_opener（）创建了一 个自定义的opener对象，第一个参数为代理信息，第二个参数为 urllib.request.HTTPHandler类。 为了方便，可以使用urllib.request.install_opener（）创建全局默 认的opener对象，那么，在使用urlopen（）时亦会使用我们安装的 opener对象，所以我们下面才可以直接使用urllib.request.urlopen（） 打开对应网址爬取网页并读取，编码后赋给变量data，最后返回data 的值给函数

	- 建立一个代理服务器登录函数

def use_proxy(proxy_addr,url):
        import urllib.request
        proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        data=urllib.request.urlopen(url).read().decode('utf-8')
        return data
proxy_addr="1.198.108.46:9999"
data=use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))

代理地址：https://www.kuaidaili.com/free/inha/

		- 

### 6，DebugLog实战

- 1）分别使用urllib.request.HTTPHandler（）和 urllib.request.HTTPSHandler（）将debuglevel设置为1。
2）使用urllib.request.build_opener（）创建自定义的opener对象， 并使用1）中设置的值作为参数。 
3）用urllib.request.install_opener（）创建全局默认的opener对 象，这样，在使用urlopen（）时，也会使用我们安装的opener对象。
4）进行后续相应的操作，比如urlopen（）等

	- import urllib.request
httphd=urllib.request.HTTPHandler(debuglevel=1)
httpshd=urllib.request.HTTPSHandler(debuglevel=1)
opener=urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data=urllib.request.urlopen("http://baidu.com").read()
print(data)

#写入本地
fhandle=open("D:/Python/8.html","wb")
fhandle.write(data)
fhandle.close()

		- 

			- 

### 7，异常处理URLError实战
HTTPError子类无法处理刚才所提到的产生URLError的前3种原 因的异常，即无法处理：连接不上服务器、远程URL不存在、无网络 引起的异常。

- 1,urllib.error.URLError
产生URLError的原因有如下几种可能：
1）连接不上服务器
2）远程URL不存在
3）无网络
4）触发了HTTPError

print(e.reason)方法输出原因，
注意URLError没有print(e.code)方法。

	- i #-*- coding: UTF-8 -*-
import urllib.request
import urllib.error
import urllib.parse

#一个不存在的连接
url="http://www.iddddd.com"
req=urllib.request.Request(url)
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)




		- 

- 2,urllib.error.HTTPError

服务器存在但下面连接资源不存在
print(e.code)方法输出代码
print(e.reason)方法输出原因

	- import urllib.request
import urllib.error
import urllib.parse

try:    
urllib.request.urlopen("https://cloud.tencent.com/136GGG1630")

except urllib.error.HTTPError as e:
         print(e.code)
   


		- 

			- 注意HTTP与HTTPS区别
HTTPS加密

- 3，综合两种
try:
    urllib.request.urlopen("http://blog.cs33333dn.net") 
except urllib.error.URLError as e: 
    if hasattr(e,"code"): 
        print(e.code) 
    if hasattr(e,"reason"):
        print(e.reason)

	- 无论哪种都可用

## 2，正则表达式与Cookie的使用

### 1，基础知识
import re正则表达式引用

- （1）普通字符作为原子
import urllib.request
import urllib.error
import re

pattern="yue"#普通字符串作为原子
string="http://yum.iqianyue.com"
result1=re.search(pattern,string)
print(result1)
#pattern在string中的位置，若没有显示none


	- 

- （2）非打印字符作为原子
/n 用于匹配一个换行符
/t   用于匹配一个制表符

pattern=("\n")#非打印字符作为原子
string='''http://yum.iqianyue.com
http://baidu.com'''
result1=re.search(pattern,string)
print(result1)



	- 

- （3）通用字符作为原子
"."除换行符（\n）外任意字符

	- pattern ="\w\dpython\w"
string="ddfdasdfasdf1212131pythond_ddd1"
result=re.search(pattern,string)
print(result)

		- 

- （4）原子表
原子表由[ ]表示，比如[xyz]就是一个原子表，这个原子 表中定义了3个原子，这3个原子的地位平等，如，我们定义的正则表 达式为“[xyz]py”，对应的源字符串是“xpython”，如果此时使用 re.search（）函数进行匹配，就可以匹配出结果“xpy”，因为此时只要 py前一位是x y z字母中的其中一个字母，就可以匹配成功。 类似的，
[^]代表的是除了中括号里面的原子均可以匹配，比 如“[^xyz]py”能匹配“apy”，但是却不能匹配“xpy”等。

	- pattern1="\w\dpython[xyz]\w" 
pattern2="\w\dpython[^xyz]\w" 
pattern3="\w\dpython[xyz]\W" 
string="abcdfphp345pythony_py" 
result1=re.search(pattern1,string) 
result2=re.search(pattern2,string) 
result3=re.search(pattern3,string) 
print(result1) 
print(result2) 
print(result3)

		- 

- （5）元字符

	- （1）任意匹配元字符
	- （2）边界限制元字符

pattern1="^abd" #边界限制元字符
pattern2="^abc" 
pattern3="py$" 
pattern4="ay$" 
string="abcdfphp345pythony_py" 
result1=re.search(pattern1,string) 
result2=re.search(pattern2,string) 
result3=re.search(pattern3,string) 
result4=re.search(pattern4,string) 
print(result1) 
print(result2) 
print(result3) 
print(result4)

		- 

	- （3）限定符
pattern1="py.*n" 
pattern2="cd{2}" 
pattern3="cd{3}" 
pattern4="cd{2,}" 
string="abcdddfphp345pythony_py" 
result1=re.search(pattern1,string) 
result2=re.search(pattern2,string) 
result3=re.search(pattern3,string) 
result4=re.search(pattern4,string) 
print(result1) 
print(result2) 
print(result3) 
print(result4)

		- 

	- （4）模式选择符 “|”
正则表达式“python|php”中，字符串“python”和“php”均满足匹配条件
第一个满足的就输出结果。
import re
pattern="python|php" #模式选择符
string="abpythoncdfphp345y_py"
result1=re.search(pattern,string)
print(result1)

		- 

	- （5）模式单元符“（ ）”
字符整体不分割（ab）

import re
pattern1="(cd){1,}" 
pattern2="cd{1,}"
string="abcdcdcdcdfphp345pythony_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)
print(result1)
print(result2)

		- 

	- （6）可选字符集
[.com|.cn]  .com或.cn中有一个满足
[a-zA-Z] [0-5 7-9]

		- import re 
pattern="[a-zA-Z]+://[^\s]*[.com|.cn]" 
string="<a href='http://www.baidu.com'>百度首页</a>" 
result=re.search(pattern,string) 
print(result)

输出：
<re.Match object; span=(9, 29), match='http://www.baidu.com'>
Press any key to continue . . .

			- 

- (6)模式修正

	- import re  #不区分大小写
pattern1="python"
pattern2="python"
string="abcdfphp345Pythony_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string,re.I)
print(result1)
print(result2)

		- 

- （7）贪婪模式与懒惰模式
总的来说，贪婪模式的核心点就是尽可能多地匹配，而懒惰模式的核心点就是尽可能少地匹配。

	- 转化为懒惰模式，需要后面加上“？”，方可转化为懒惰模式。

例：
表达式 .* 就是单个字符匹配任意次,即贪婪匹配。 
表达式 .*? 是满足条件的情况只匹配一次,即最小匹配. 

		- import re 
pattern1="p.*y"#贪婪模式
pattern2="p.*?y"#懒惰模式
string="abcdfphp345pythony_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)
print(result1)
print(result2)

			- 

- （8）正则表达式常见函数

	- 1.re.match（）从头匹配函数
re.match(pattern,string,flag)
第一个参数代表对应的正确表达式，第二个参数代表对应的源字 符，第三个参数是可选参数，代表对应的标志位，可以放模式修正符 等信息

函数从头开始匹配，若第一个字符不符合输出none

		- 

			- 

	- 2.re.search（）整个字符串函数 
re.search(pattern,string,flag)
第一个参数代表对应的正确表达式，第二个参数代表对应的源字 符，第三个参数是可选参数，代表对应的标志位，可以放模式修正符 等信息

re.search（）函数进行匹配，使用该函 数进行匹配，会扫描整个字符串并进行对应的匹配。该函数与 re.match（）函数最大的不同是，re.match（）函数从源字符串的开头 进行匹配，而re.search（）函数会在全文中进行检索并匹配。

		- import re string="hellomypythonhispythonourpythonend" pattern=".python." result=re.match(pattern,string) result2=re.search(pattern,string) print(result) print(result2)

			- 

	- 3.全局匹配函数
处理字符串内多个符合要求的结果

		- 思路如下： 
1）使用re.compile（）对正则表达式进行预编译。
 2）编译后，使用findall（）根据正则表达式从源字符串中将匹 配的结果全部找出。

			- import re 
string="hellomypythonhispythonourpythonend" 
pattern=re.compile(".python.")#预编译 
result=pattern.findall(string)#找出符合模式的所有结果 
print(result)

				- 

			- import re #整合
string="hellomypythonhispythonourpythonend" 
pattern=".python." 
result=re.compile(pattern).findall(string) 
print(result)

				- 

	- 4.re.sub（）匹配并替换函数
re.sub(pattern,rep,string,max)

其中，第一个参数为对应的正则表达式，第二个参数为要替换成 的字符串，第三个参数为源字符串，第四个参数为可选项，代表最多 替换的次数，如果忽略不写，则会将符合模式的结果全部替换。 使用re.sub（）这个函数，会根据正则表达式pattern，从源字符 串string查找出符合模式的结果，并替换为字符串rep，最多可替换 max次

		- 用php 代替python字符
import re 
string="hellomypythonhispythonourpythonend" 
pattern="python." 
result1=re.sub(pattern,"php",string) #全部替换 
result2=re.sub(pattern,"php",string,2) #最多替换两次 
print(result1) 
print(result2)

输出：
hellomyphpisphpurphpnd
hellomyphpisphpurpythonend
Press any key to continue . . .


			- 

- （9）实例解析

	- 实例1：匹配.com或.cn后缀的URL网址

实例目的：将一串字符串里面以.com或.cn为域名后缀的URL网 址匹配出来，过滤掉其他的无关信息。

		- import re 
pattern="[a-zA-Z]+://[^\s]*[.com|.cn]" 
string="<a href='http://www.baidu.com'>百度首页</a>" 
result=re.search(pattern,string) 
print(result)

输出：
<re.Match object; span=(9, 29), match='http://www.baidu.com'>
Press any key to continue . . .
	

			- 

	- 实例2：匹配电话号码
实例目的：将一串字符串里面出现的电话号码信息提取出来，过 滤掉其他无关信息。

		- import re #匹配电话号码 
pattern="\d{4}-\d{7}|\d{3}-\d{8}" 
string="<a href='http://www.bai92698876g033-45645677ggg" 
result=re.search(pattern,string) 
print(result)

			- 

				- 

	- 实例3：匹配电子邮件地址
实例目的：将一串字符串里面出现的电子邮件信息提取出来，过 滤掉其他无关信息。

		-  
import re 
pattern="\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*" #匹配电子邮件的正则表达式 
string="<a href='http://a><br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址</a>" 
result=re.search(pattern,string) 
print(result)

			- 

### 2,Cookie

- 1，http.cookiejar

如果希望登录状态一直保持，则需要进行Cookie处理。 进行Cookie处理的一种常用思路如下：
1）导入Cookie处理模块http.cookiejar。
2）使用http.cookiejar.CookieJar（）创建CookieJar对象。 
3）使用HTTPCookieProcessor创建cookie处理器，并以其为参数 构建opener对象。 
4）创建全局默认的opener对象

	- #cookie使用
import urllib.request 
import urllib.parse 
import http.cookiejar 
url = "http:// bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit =yes&loginhash=L768q"
postdata =urllib.parse.urlencode({ "username":"weisuen", "password":"aA123456" }).encode('utf-8') 
req = urllib.request.Request(url,postdata) 
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0') 
#使用http.cookiejar.CookieJar()创建CookieJar对象
cjar=http.cookiejar.CookieJar() 
#使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象 
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar)) 
#将opener安装为全局 
urllib.request.install_opener(opener) 
file=opener.open(req) 
data=file.read() 
file=open("D:/Python10.html","wb") 
file.write(data) 
file.close() 
url2="http:// bbs.chinaunix.net/" 
data2=urllib.request.urlopen(url2).read() 
fhandle=open("D:/Python11.html","wb") 
fhandle.write(data2) 
fhandle.close()

		- 

			- 

## 3,手写Python爬虫

### 1，爬取图片

- pat1='<div id="plist".+？<div class="page clearfix">'。
所有内部包含的内容

	- 

- 图片1
- 图片2
- 综合图片得出
pat2='<img width="220" height="220" data-img="1" src="// (.+？\.jpg)">'

 "(.+？\.jpg)"其中\为引用符，说明后面点就是点，没有包含其他意思

- import urllib.request
import urllib.error
import re

def craw(url,page):
    file=urllib.request.urlopen(url).read()
    file=str(file)
    pat1='<div id="plist".+? <div class="page clearfix">'
    pat2='<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    result1=re.compile(pat1).findall(file)
    result1=result1[0]
    imagelist=re.compile(pat2).findall(result1)
    print(imagelist)
    x=1
    for imageurl in imagelist:
        imagename="D:/Python/img1/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:    
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(2,100):
    url="https://list.jd.com/list.html?cat=670,671,672&page="+str(i)+"&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
    craw(url,i)


	- 

### 2，连接爬虫
链接爬虫实现的思路如下： 
1）确定好要爬取的入口链接。 
2）根据需求构建好链接提取的正则表达式。 
3）模拟成浏览器并爬取对应网页。 
4）根据2）中的正则表达式提取出该网页中包含的链接。 
5）过滤掉重复的链接。 
6）后续操作。比如打印这些链接到屏幕上等。

- import urllib.request
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

	- 

### 3，多线程及列队爬取

- 1，队列用法
a.put() 写入队列
a.get()  出队列
a.task_done  判断是否写入成功

import queue
b=0
a=queue.Queue()
a.put("hello")
if a.task_done:
    b=b+1
    print(str(b))
a.put("world")
if a.task_done:
    b=b+1
    print(str(b))
a.put("haha")
if a.task_done:
    b=b+1
    print(str(b))
c=a.get()
print(c)
c=a.get()
print(c)
c=a.get()
print(c)

	- 

- 2，多线程用法

#多线程基础 
import threading 
class A(threading.Thread): 
    def __init__(self): 
        #初始化该线程
         threading.Thread.__init__(self) 
         def run(self): #该线程要执行的程序内容 
             for i in range(10): print("我是线程A") 
class B(threading.Thread): 
    def __init__(self): 
        threading.Thread.__init__(self) 
        def run(self): 
            for i in range(10): print("我是线程B") 
#实例化线程A为t1 
t1=A() #启动线程t1 
t1.start() 
#实例化线程B为t2 
t2=B() #启动线程t2，此时与t1同时执行 
t2.start()t2.start()

	- 

## 4，fiddler 监听软件使用

## 5，爬虫伪装

### 爬虫的浏览器伪装技术
常见的反爬虫机制主要有： 
1）通过分析用户请求的Headers信息进行反爬虫。 
2）通过检测用户行为进行反爬虫，比如通过判断同一个IP在短 时间内是否频繁访问对应网站等进行分析。 
3）通过动态页面增加爬虫爬取的难度，达到反爬虫的目的。

### Headers头信息

我们通过浏览器访问某个网址的时候，会向服务器发送一些 Headers头信息，然后服务器会根据对应的用户请求头信息生成一个 网页内容，并将生成的内容返回给浏览器。这就是Headers头信息使 用的基本原理和过程

- 

	- 常见字段1：Accept：text/html，application/xhtml+xml， application/xml；q=0.9，*/*；q=0.8


·Accept字段主要用来表示浏览器能够支持的内容类型有哪些。
 ·text/html表示HTML文档。 ·application/xhtml+xml表示XHTML文档。 
·application/xml表示XML文档。 
·q代表权重系数，值介于0和1之间。 
所以这一行字段信息表示浏览器可以支持text/html、 application/xhtml+xml、application/xml、*/*等内容类型，支持的优先 顺序从左到右依次排列
	- 常见字段2：Accept-Encoding：gzip，deflate 

·Accept-Encoding字段主要用来表示浏览器支持的压缩编码有哪 些。
·gzip是压缩编码的一种。
 ·deflate是一种无损数据压缩算法。
 这一行字段信息表示浏览器可以支持gzip、deflate等压缩编码。
	- 常见字段3：Accept-Language：zh-CN，zh；q=0.8，en-US； q=0.5，en；q=0.3 

·Accept-Language主要用来表示浏览器所支持的语言类型。
·zh-CN表示简体中文语言，zh表示中文，CN表示简体。
 ·en-US表示英语（美国）语言。
 ·en表示英语语言。
 所以之一行字段表示浏览器可以支持zh-CN、zh、en-US、en等 语言。
	- 常见字段4：User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36

·User-Agent字段主要表示用户代理，服务器可以通过该字段识别 出客户端的浏览器类型、浏览器版本号、客户端的操作系统及版本 号，网页排版引擎等客户端信息。所以我们之前要模拟浏览器登录， 主要以伪造该字段进行
·Mozilla/5.0表示浏览器名及版本信息。
·(Windows NT 10.0; Win64; x64·表示客户端操作系统对应 信息。
.AppleWebKit/537.36 (KHTML, like Gecko) 网页架构信息
Chrome/80.0.3987.149 Safari/537.36 表示谷歌浏览器版本及 safari 内核
	- 常见字段5：Connection：keep-alive 

·Connection表示客户端与服务器的连接类型，对应的字段值主要 有两种：
·keep-alive表示持久性连接。 
·close表示单方面关闭连接，让连接断开。
所以此时，这一行字段表示客户端与服务器的连接是持久性连 接。
	- 常见字段6：Host：www.youku.com

 ·Host字段表示请求的服务器网址是什么，此时这一行字段表示 请求的服务器网址是www.youku.com。
	- 常见字段7：Referer：网址
 ·Referer字段主要表示来源网址地址，比如我们从 http://www.youku.com网址中访问了该网址下的子页面 http://tv.youku.com/?spm=0.0.topNav.5～1～3！2～A.QnQOEf，那么 此时来源网址为http://www.youku.com，即此时Referer字段的值 为http://www.youku.com。

- GET / HTTP/1.1
Host: www.youku.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
Sec-Fetch-Dest: document
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: __ysuid=1568085067055tYs; cna=EQL+FZg8C0gCATzRfUqkbNno; __aysid=1586241626446EYh; __ayspstp=1; UM_distinctid=171535e6d3a2e2-0f9ff77b33bb12-f313f6d-1fa400-171535e6d3ba13; CNZZDATA1277956573=1102223495-1586241220-%7C1586241220; _m_h5_tk=a6fbcd84d148587b397debf76713a799_1586246149855; _m_h5_tk_enc=fefdd6990a35ecf89c6f5c0262ffc373; modalFrequency={"UUID":"2"}; modalBlackListclose={"UUID":"2"}; modalBlackListlogined={"UUID":"2"}; firstTimes=0; isg=BPPzokq7qRYU5mZOBdZfLDhtgvcdKIfqFz7FLqWQQpJJpBNGLfqwOlP1WtRKBN_i


### 爬虫的浏览器伪装技术实战

- 可以看 到，此时的用户代理为“Python-urllib/3.7”，允许的压缩编码类型为 identity，服务器在收到这些Headers信息之后，就可以对客户端的基 本情况进行分析
- 

	- #模拟浏览器信息
import urllib.request
import http.cookiejar
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "Accept-Encoding":"utf-8,gb2312",
         "Accept-Language": "zh-CN,zh;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Connection": "keep-alive" ,
"referer":"baidu.com"}

url="https://news.163.com/"
cjar=http.cookiejar.CookieJar
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
proxy=urllib.request.ProxyHandler({'https':"127.0.0.1:8888"})
opener=urllib.request.build_opener(proxy,urllib.request.HTTPSHandler)
opener.addheaders=headall
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("D:/Python/20.html","wb")
fhandle.write(data)
fhandle.close()

- 添加代理及cookiejar


	- 
#模拟浏览器信息
import urllib.request
import http.cookiejar
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "Accept-Encoding":"utf-8,gb2312",
         "Accept-Language": "zh-CN,zh;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Connection": "keep-alive" ,
"referer":"baidu.com"}

url="https://news.163.com/"
cjar=http.cookiejar.CookieJar()
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
proxy=urllib.request.ProxyHandler({'https':"127.0.0.1:8888"})
opener=urllib.request.build_opener(proxy,urllib.request.HTTPSHandler,urllib.request.HTTPCookieProcessor(cjar))
opener.addheaders=headall
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("D:/Python/20.html","wb")
fhandle.write(data)
fhandle.close()


## 6,爬虫的定向爬取技术

### 爬虫的定向爬取技术主要需要解决3个问题：
 1）清晰地定义好爬虫的爬取目标，规划好主题。 
2）建立好爬取网址的过滤筛选规则以及内容的过滤筛选规则。
3）建立好URL排序算法，让爬虫能够明确优先爬取哪些网页、 以什么顺序爬取待爬取的网页。比如，待爬取的URL网址可能有很 多，在爬虫资源有限的情况下，需要确定好这些网址的爬行顺序，以 不一样的顺序去爬取，可能会导致不一样的爬取效率。

- 子主题 1

### 在一个爬虫项目中，定向爬取某些信息的步骤主要有： 
1）理清爬取的目的。这一步非常关键，有一个明确的爬取目 的，可以让我们在设置爬取规则的时候思路更加清晰，爬取失败率更 低。
2）设置网址的过滤规则。这一步显然不是必须的，但是在网址 数较多的爬取任务中，合理地进行该项设置，可以大大提高爬虫的爬 取效率。由于有的时候爬虫爬取的网址数量很多，要爬取的内容在某 些有规律的网址中，此时，我们可以设置对应的模式，比如设置好对 应的正则表达式，将不满足格式的网址过滤掉，此时爬虫就不需要爬 取那些没有包含目标信息的网址了，爬虫只需要爬取满足格式的网 址，即包含目标信息的网址即可，这样做可以大大的提高爬行效率， 当然这一步并不是强制要求去做的。对于某些网址数量并不多的爬取 任务，我们是否进行该项设置对爬取效率的影响并不会太大。 
3）设置好内容采集规则。通过这一步的设置，我们可以提取出
我们关注的信息，从而过滤掉那些不关注的信息，信息筛选的方法与 策略有很多，通过正则表达式去筛选信息是其中一种方法。 
4）规划好采集任务，合理的设置爬虫线程与爬虫数量。对于任 务量不大的爬虫，使用一个单线程爬虫即可完成。但如果爬虫的任务 量很大，此时为了提高效率，我们可以使用多线程爬虫或者使用多个 爬虫去爬取对应的任务，但是，如果使用多线程爬虫或使用多个爬虫 去爬取，则需要对每个爬虫要爬取的任务进行合理规划，避免出现一 直重复爬取或某些目标网页漏爬的情况。 
5）将采集结果进行相应的修正，处理成我们想要的格式。完成 采集后，有可能采集结果并不是我们想要的格式，此时我们对采集的 结果进行相应的修正，比如进行编码、解码、格式整理等修正操作， 将采集的结果处理成我们需要的格式。 
6）对结果进行进一步处理，完成任务。比如，如有需要，我们 可以将结果写入数据库等，等相应的后续处理操作，从而完成我们的 爬虫任务。

- 

## 7，scrapy基础

### 1，创建项目及文件

- 1，scrapy startproject 项目名 建立爬虫项目（一个项目，多个文件）

2，scrapy genspider -t 类型名 建立爬虫类型（一个文件而已）

D:\>CD D:\300_Python\Program

D:\300_Python\Program>scrapy genspider -l
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed

D:\300_Python\Program>scrapy startproject scrapytest
New Scrapy project 'scrapytest', using template directory 'D:\300_Python\Setup_file\Anaconda3\lib\site-packages\scrapy\templates\project', created in:
    D:\300_Python\Program\scrapytest

You can start your first spider with:
    cd scrapytest
    scrapy genspider example example.com

- 3，Items 编写
结构化数据名= scrapy.Field()

	- import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urlname=scrapy.Field()
    urlkey=scrapy.Field()
    urlcr=scrapy.Field()
    urladdr=scrapy.Field()
    

		- 

	- 实验

		- import scrapy

class person(scrapy.Item):
    name=scrapy.Field()
    job=scrapy.Field()
    email=scrapy.Field()
    

tod=person(name="tod",job="teacher",email="tod.com")

print(tod)
{'email': 'tod.com', 'job': 'teacher', 'name': 'tod'}

tod["job"]
Out[5]: 'teacher'

tod.keys()
Out[6]: dict_keys(['name', 'job', 'email'])

tod.items()
Out[7]: ItemsView({'email': 'tod.com', 'job': 'teacher', 'name': 'tod'})


- 4，Spider的编写
使用 scrapy genspider -t basic 文件名 要访问的网址


	- 

		- # -*- coding: utf-8 -*-
import scrapy


class TodSpider(scrapy.Spider):
    name = 'tod'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass

	- 

		- # -*- coding: utf-8 -*-
import scrapy
from scrapytest.items import ScrapytestItem

class TodSpider(scrapy.Spider):
    name = 'tod'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
                  'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml']

    def parse(self, response):
        item=ScrapytestItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print(item["urlname"])


### 2，xpath基础

XPath是一种XML路径语言，通过该语言可以在XML文档中迅速 地查找到相应的信息，XPath表达式通常叫作XPath selector。 
在XPath表达式中，使用“/”可以选择某个标签，并且可以使 用“/”进行多层标签的查找

- 1，查询内容
<html>
 <head><title>首页</title></head>
 <body> 
<h2> 大数据与爬虫有什么关系？
 </h2> 
<p>在大数据处理中，数据源是很重要的，某些时候，数据源无法直接得到，此时使用爬虫可以轻松对大量的数据进行采集，…
</p> 
<p>除此之外，它们之间的关系还有…</p> 
</body>
 </html>

	- 1,如果要提取出<h2></h2>标签对应的内容
/html/body/h2
	- 2,如果想获取该标签中的文本信息，可以通过text（）实现



		- /html/body/h2/text()

大数据与爬虫有什么关系？

	- 3,多个标签提取

使用“//”可以提取某个标签的所有信息。比如上方代码中出现了 多个<p>标签，如果想将这所有<p>标签的所有信息都提取出来

		- //p

<p>在大数据处理中，数据源是很重要的，某些时候，数据源无法直接得到，此时使用爬虫可以轻松对大量的数据进行采集，…
</p> 
<p>除此之外，它们之间的关系还有…</p> 

- <div class="Page Top">
 <div class="fl Logo"> 
<img src="http://static.edu.51cto.com/index/images/logo.png?v=1.0.0.0" class="fl"> 
<img src="http://static.edu.51cto.com/index/images/sublogo.png" class="fl">
 <div class="clear"></div> 
</div> ……</div>

	- 4，如果想获取所有属性X的值为Y的<Z>标签的内容，可以通
过“//Z[@X=”Y”]”的方式获取。

		- 比如想获取上方代码中所有class属性值为“f1”的<img>标签中的 内容，可以通过以下XPath表达式获取

//img[@class=”f1”]

- 

	- # -*- coding: utf-8 -*-
import scrapy
from scrapytest.items import ScrapytestItem

class TodSpider(scrapy.Spider):
    name = 'tod'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_103185.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1',
                  'http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml',]

    def parse(self, response):
        item=ScrapytestItem()
        item["urlname"]=response.xpath("/html/head/title/text()")
        print(item["urlname"])
    #重新初始化方法__init__(),并设置参数myurl
    #args 是 arguments 的缩写，表示位置参数；kwargs 是 keyword arguments 的缩写，表示关键字参数。
    def __init__(self,myurl=None,*args,**kwargs):
        super(TodSpider,self).__init__(*args,**kwargs)
        print("要爬取的网址为： %s"%myurl)
        self.start_urls=["%s"%myurl]

### 3，抓取实验
两种爬虫试验

xmlfeed
csvfeed

- 1，读取订阅信息 xml

	- # -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # 迭代器
    itertag = 'rss' # 用来设置开始迭代的节点

    def parse_node(self, response, selector):
        #方法在节点与所提供的标 签名相符合的时候会被调用，在该方法中，可以进行一些信息的提取 和处理的操作
        item =MyxmlItem()
        item['title']=selector.xpath("/rss/channel/item/title/text()").extract()
        item['link'] = selector.xpath("/rss/channel/item/link/text()").extract()
        item['author'] = selector.xpath("/rss/channel/item/author/text()").extract()

        for j in range(len(item['author'])):
            print("第"+str(j+1)+"篇文章")
            print("标题是： ")
            print(item['title'][j])
            print("对应链接是：")
            print(item['link'][j])
            print("对应作者是： ")
            print(item['author'][j])
        return item

		- 
(base) D:\300_Python\Program\myxml>scrapy crawl myxmlspider --nolog
第1篇文章
标题是：
襄阳美
对应链接是：
http://blog.sina.com.cn/s/blog_6050805d01016wxn.html
对应作者是：
韦玮pig
第2篇文章
标题是：
春至华夏
对应链接是：
http://blog.sina.com.cn/s/blog_6050805d01014ak1.html
对应作者是：
韦玮pig
第3篇文章
标题是：
思
对应链接是：
http://blog.sina.com.cn/s/blog_6050805d010128nj.html
对应作者是：
韦玮pig
第4篇文章
标题是：
春影
对应链接是：

- 2，读取邮件信息 xml

	- from myxml.items import MyxmlItem

class PersonalemailSpider(XMLFeedSpider):
    name = 'personalemail'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
    iterator = 'iternodes' # 迭代器
    itertag = 'person' # 用来设置开始迭代的节点
    
    def parse_node(self, response, selector):
        #方法在节点与所提供的标 签名相符合的时候会被调用，在该方法中，可以进行一些信息的提取 和处理的操作
        item =MyxmlItem()
        item['link'] = selector.xpath("/person/email/text()").extract()
        print(item['link'])


- 3,csv抓取

	- 

		- # -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/mydata.csv']
    #定义heders
    headers = [ 'name', 'sex', 'addr','email']
    #定义间隔符
    delimiter = ','
    def parse_row(self, response, row):       
        i = MycsvItem
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        i['addr']=row['addr'].encode()
        i['email']=row['email'].encode()
        print(i['name'])
        print(i['sex'])
        print(i['addr'])
        print(i['email'])
        print("-----------------")
        return i

### 4，多爬虫运行
修改CRAW 代码实现多爬虫
https://github.com/scrapy/scrapy/blob/master/scrapy/commands/crawl

- 1，同一目录下建立3个爬虫文件

D:\Python35\myweb\part12>cd mymultispd 
D:\Python35\myweb\part12\mymultispd>scrapy genspider -t basic myspd1 sina.com.cn Created spider 'myspd1' using template 'basic' in module: mymultispd.spiders.myspd1 
D:\Python35\myweb\part12\mymultispd>scrapy genspider -t basic myspd2 sina.com.cn Created spider 'myspd2' using template 'basic' in module: mymultispd.spiders.myspd2 
D:\Python35\myweb\part12\mymultispd>scrapy genspider -t basic myspd3 sina.com.cn Created spider 'myspd3' using template 'basic' in module: mymultispd.spiders.myspd3

	- 

- 2，建立存放修改crawl 命令的目录及文件
在这里，我们将新文件夹的名字命名为mycmd，在对应目录下创 建该文件夹，如下所示：
 D:\Python35\myweb\part12\mymultispd>cd .\mymultispd\ 
D:\Python35\myweb\part12\mymultispd\mymultispd>mkdir mycmd

然后，进入新建的文件夹并创建一个Python文件（文件名可以自 定义，满足Python文件命名规则即可），如下所示： D:\Python35\myweb\part12\mymultispd\mymultispd>cd .\mycmd\ 
D:\Python35\myweb\part12\mymultispd\mymultispd\mycmd>echo #>mycrawl.py #
- 3，在当前子目录下建立__init__.py初始化文件
D:\Python35\myweb\part12\mymultispd\mymultispd\mycmd>echo #>__init__.py #

在settings.py文件下增加COMMANDS_MODULE = 'mymultispd.mycmd'
- 4，检查是否正常建立 多爬虫运行文件
D:\300_Python\Program\mymultispd\mymultispd\mycmd>scrapy -h

	- 运行结果

### 5，避免被禁止

在Scrapy项目中，主要可以通过以下方法来避免被禁止： 
1）禁止Cookie； 
2）设置下载延时； 
3）使用IP池； 
4）使用用户代理池； 
5）其他方法，比如进行分布式爬取等。

- 1，禁止cookie（默认已注释掉）
setings.py 下注释点两行
# Disable cookies (enabled by default) 
#COOKIES_ENABLED = False
- 2，设置下载延时
打开settings.py文件，会发现有如下几行代码： 
# Configure a delay for requests for the same website (default: 0) 
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay 
# See also autothrottle settings and docs #DOWNLOAD_DELAY = 3

#DOWNLOAD_DELAY=3为设置时间间隔的具体代码，解除这一行 的注释即可实现下载延时的配置，其中3代表3秒，如果想将爬虫下载 网页的时间间隔设置为0.5秒，将对应的值改为0.5即可。
DOWNLOAD_DELAY=0.5
- 3,使用IP池

为Scrapy爬虫项目建立一个下载中间件，在下载 中间件中设置好IP选择规则，在settings.py设置文件中配置好下载中 间件，并配置好IP池

	- 1，修改中间件


		- #导入随机数模块，目的是随机挑选一个IP池中的IP
import random
#从settings文件（mymultispd.settings为settings文件的地址）中导入设置好的IPPOOL
from mymultispd.settings import IPPOOL
#导入官方一样思考HttpProxyMiddleware对应模块  scrapy.contrib无法使用，直接接downloadermiddlewares

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    #初始化方法
    def __init__(self,ip=''):
        self.ip=ip
    #process_request()方法，主要进行请求处理
    def process_request(self, request, spider):
        #先随机选择一个IP
        thisip=random.choice(IPPOOL)
        #输出当前选择的IP，便于调试观察
        print("当前IP地址是： "+thisip["ipaddr"])
        #将对应的IP实际添加为具体的代理，用该IP进行爬取
        request.meta["proxy"]="http://"+thisip["ipaddr"]

	- 2,修改setting.py 内容
DOWNLOADER_MIDDLEWARES = {
   # 'mymultispd.middlewares.MymultispdDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    'mymultispd.middlewares.IPPOOLS':125
}


### 6，保存

- 1，修改Setting值
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'mypjt.pipelines.MypjtPipeline': 300,
}


	- 

- 2，存储 pipelins
import codecs

class MypjtPipeline(object):
    def __init__(self):
        self.file=codecs.open("D:/300_Python/320_Program/mydata1.txt","wb",encoding="utf-8")
    def process_item(self, item, spider):
        l=str(item)+"\n"
        print(l)
        self.file.write(l)
        return item
    def close_spider(self,spider):
        self.file.close()



	- 

- 3,爬取程序
注意 yield item ,不加无法保存

	- # -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    # allowed_domains = ['sina.com.cn']
    start_urls = ['https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=OPM#tabs-246']

    def parse(self, response):
        item=MypjtItem()
        item["title"]=response.xpath("/html/head/title/text()")
        print(item["title"])
        yield item


### 例

- 1，spnider
# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://e.dangdang.com/list-CXSJ-comment-0-1.html']

    def parse(self, response):
        item=AutopjtItem()
        item["name"]=response.xpath("//a[@target='_blank']/@title").extract()
        item["author"] = response.xpath("//a[@target='_blank']/@dd_name").extract()
        item["link"] = response.xpath("//a[@target='_blank']/@href").extract()
        yield item
        print(len(item["name"]))

	- 

- 2,item

import scrapy

class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    link=scrapy.Field()
    comnum=scrapy.Field()
    author=scrapy.Field()


	- 

- 3,pipelines

import json
import codecs

class AutopjtPipeline(object):
    def __init__(self):
        self.file=codecs.open("D:/300_Python/320_Program/miiata0423.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        for j in range(0,len(item["name"])):
            name=item["name"][j]
            author=item["author"][j]
            link=item["link"][j]
            goods={"name":name,"author":author,"link":link}
    #         将组合后的商量写入json
            i=json.dumps(dict(goods),ensure_ascii=False)
            line=i+'\n'
            print(line)
            self.file.write(line)
        return item

    def close_spider(self,spider):
        self.file.close()

	- 

- 运行结果

## 8，scrapy 
CrawlSpider（自动爬取网页）实例

extract()==getall()

### 

