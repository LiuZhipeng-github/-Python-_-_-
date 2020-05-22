import urllib.request
import urllib.error
import re

#pattern="yue"#普通字符串作为原子
#string="http://yum.iqianyue.com"
#result1=re.search(pattern,string)
#print(result1)#pattern在string中的位置，若没有显示none

#pattern=("\n")#非打印字符作为原子
#string='''http://yum.iqianyue.com
#http://baidu.com'''
#result1=re.search(pattern,string)
#print(result1)

#pattern ="\w.python\w"
#string="ddfdasdfasdf1212131pythond_ddd1"
#result=re.search(pattern,string)
#print(result)

#pattern1="\w\dpython[xyz]\w" #原子表，字符集
#pattern2="\w\dpython[^xyz]\w" 
#pattern3="\w\dpython[xyz]\W" 
#string="abcdfphp345pythony_py" 
#result1=re.search(pattern1,string) 
#result2=re.search(pattern2,string) 
#result3=re.search(pattern3,string) 
#print(result1) 
#print(result2) 
#print(result3)

#import re #元字符
#pattern=".python..." 
#string="abcdfphp345pythony_py" 
#result1=re.search(pattern,string) 
#print(result1)

#pattern1="^abd" #边界限制元字符
#pattern2="^abc" 
#pattern3="py$" 
#pattern4="ay$" 
#string="abcdfphp345pythony_py" 
#result1=re.search(pattern1,string) 
#result2=re.search(pattern2,string) 
#result3=re.search(pattern3,string) 
#result4=re.search(pattern4,string) 
#print(result1) 
#print(result2) 
#print(result3) 
#print(result4)

#pattern1="py.*n" #限定符
#pattern2="cd{2}" 
#pattern3="cd{3}" 
#pattern4="cd{2,}" 
#string="abcdddfphp345pythony_py" 
#result1=re.search(pattern1,string) 
#result2=re.search(pattern2,string) 
#result3=re.search(pattern3,string) 
#result4=re.search(pattern4,string) 
#print(result1) 
#print(result2) 
#print(result3) 
#print(result4)

#pattern="python|php" #模式选择符
#string="abpythoncdfphp345y_py"
#result1=re.search(pattern,string)
#print(result1)

#import re
#pattern1="(cd){1,}" 
#pattern2="cd{1,}"
#string="abcdcdcdcdfphp345pythony_py"
#result1=re.search(pattern1,string)
#result2=re.search(pattern2,string)
#print(result1)
#print(result2)

#import re  #不区分大小写
#pattern1="python"
#pattern2="python"
#string="abcdfphp345Pythony_py"
#result1=re.search(pattern1,string)
#result2=re.search(pattern2,string,re.I)
#print(result1)
#print(result2)

#import re 
#pattern1="p.*y"#贪婪模式
#pattern2="p.?y"#懒惰模式
#string="abcdfphp345pythony_py"
#result1=re.search(pattern1,string)
#result2=re.search(pattern2,string)
#print(result1)
#print(result2)

#import re 
#string="1apythonhellomypythonhispythonourpythonend" 
#pattern=".python." 
#result=re.match(pattern,string) 
#print(result) 

#import re 
#string="hellomypythonhispythonourpythonend" 
#pattern=".python." 
#result=re.match(pattern,string) 
#result2=re.search(pattern,string) 
#print(result) 
#print(result2)


#import re 
#string="hellomypythonhispythonourpythonend" 
#pattern=re.compile(".python.")#预编译 
#result=pattern.findall(string)#找出符合模式的所有结果 
#print(result)

#import re #整合
#string="hellomypythonhispythonourpythonend" 
#pattern=".python." 
#result=re.compile(pattern).findall(string) 
#print(result)

#import re 
#string="hellomypythonhispythonourpythonend" 
#pattern="python." 
#result1=re.sub(pattern,"php",string) #全部替换 
#result2=re.sub(pattern,"php",string,2) #最多替换两次 
#print(result1) 
#print(result2)

#import re   #匹配网址
#pattern="[a-zA-Z]+://[^\s]*[.com|.cn]" 
#string="<a href='http://www.baidu.com'>百度首页</a>" 
#result=re.search(pattern,string) 
#print(result)

#import re #匹配电话号码 
#pattern="\d{4}-\d{7}|\d{3}-\d{8}" 
#string="<a href='http:// www.baidu.com'>百度首页</a>032-92698876g033-45645677ggg" 
#result=re.compile(pattern).findall(string)
#print(result)


#import re #匹配邮件地址
#pattern="\w+@\w+[.com|.cn.|net]" 
#string="dfdf@qq.com'>百度首页</a>032-9ff2f@qq-fdf.comg033-45645677ggg" 
#result=re.compile(pattern).findall(string)
#print(result)
 
#import re 
#pattern="\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*" #匹配电子邮件的正则表达式 
#string="<a href='http:// www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址</a>" 
#result=re.search(pattern,string) 
#print(result)

##cookie使用
#import urllib.request 
#import urllib.parse 
#import http.cookiejar 
##url地址
#url = "http:// bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit =yes&loginhash=L768q"
##post 名称 密码
#postdata =urllib.parse.urlencode({ "username":"weisuen", "password":"aA123456" }).encode('utf-8') 
##组合成Request 
#req = urllib.request.Request(url,postdata)
##增加头文件，模拟访问
#req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0') 
##使用http.cookiejar.CookieJar()创建CookieJar对象
#cjar=http.cookiejar.CookieJar() 
##使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象 
#opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar)) 
##将opener安装为全局 
#urllib.request.install_opener(opener) 
#file=opener.open(req) 
#data=file.read() 
#file=open("D:/Python10.html","wb") 
#file.write(data) 
#file.close() 
#url2="http:// bbs.chinaunix.net/" 
#data2=urllib.request.urlopen(url2).read() 
#fhandle=open("D:/Python11.html","wb") 
#fhandle.write(data2) 
#fhandle.close()