import threading
import urllib.request
import urllib.error
import re
import queue
import time
import datetime


#当前数量，当前页码
#模拟人工输入
#异常状态处理

#模拟人工输入
urlqueue=queue.Queue()
#模拟成浏览器访问方式访问
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "Accept-Encoding":"utf-8,gb2312",
         "Accept-Language": "zh-CN,zh;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Connection": "keep-alive" ,
"referer":"baidu.com"}
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener=urllib.request.build_opener()
opener.addheaders=headall
urllib.request.install_opener(opener)

ac=1
i=0
now_page=0

#ArtMEt/1141 https://rtys6.com/ArtMET/list62.html 62-70
#线程2保存
class Save_file(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self) 
        self.urlqueue=urlqueue
    def run(self):
        while True:           
            global ac
            ac=ac+1
            global now_page
            imagename="E:/100_Python/120_Program/photo/pic0425/"+str(i)+"-"+str(ac)+".jpg"
            url=self.urlqueue.get()
            now_page=now_page+1
            #print(url)    
            try:    
                urllib.request.urlretrieve(url,filename=imagename)
                print(url+"  page no.==>"+str(now_page))  
                #print("Now pictures---->"+str(ac))
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                    time.sleep(2)
                    return
                if hasattr(e,"reason"):
                    print(e.reason)
                    time.sleep(2)
                    return
            except Exception as e:
                print("exception:------->"+str(e))
                #若为Exception异常，延时1秒执行
                time.sleep(1)



#读取真实具体地址并写入队列  
def craw(url):
    try:
        #url="https://rtys6.com/ArtZG/"+url
        #url="https://rtys6.com/ArtDD/"+url
        url="https://rtys8.cc/rtys/"+url
       
        #print(url)
        file1=urllib.request.urlopen(url).read() 
        file1=str(file1)
        #pat5="https://p.666ho.com/tu/allimg/(.+?)-lp\.jpg"
        #pat5="https://p.666ho.com/pic/(.+?-lp)\.jpg"  #20页之后更换
        pat5="https://p.rtys8.org/pic88/(.+?-lp)\.jpg" # 63
        #<img src="https://p.666ho.com/pic/2018/0507/164-lp.jpg">

        result5=re.compile(pat5).findall(file1)
        print(result5)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
            time.sleep(2)
            return
        if hasattr(e,"reason"):
            print(e.reason)
            time.sleep(2)
            return
    except Exception as e:
        print("exception:读了实际地址错误"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)    
    for link in result5:        
        #url="https://p.666ho.com/tu/allimg/"+link+".jpg"
        #url="https://p.666ho.com/pic/"+link+".jpg"  
        link=link.replace('-lp','')
        print(link)
        url="https://p.rtys8.org/pic88/"+link+".jpg"
        print(url)
        #global ac
        #ac=ac+1
        #追加队列
        urlqueue.put(url)
        urlqueue.task_done()
        #crawphoto(url)


 # 线程1读取总列表 及正则分列表
class Get_real_adress(threading.Thread):   
     def __init__(self): 
        #初始化该线程
         threading.Thread.__init__(self)         
     def run(self): #该线程要执行的程序内容 
         global i         
         for i in range(1,12):#ZG =128出现问题 DD42-49 410-422
            print(str(i)+"+++++++++++++++++++++++++")  
            #url="https://rtys6.com/ArtZG/list"+str(i)+".html"
            #url="https://rtys6.com/ArtDD/list"+str(i)+".html"
            #url="https://rtys6.com/ArtOM/list"+str(i)+".html"
            url="https://rtys8.cc/rtys/rtys"+str(i)+".html"
            try:
                file=urllib.request.urlopen(url).read() 
                file=str(file)
                pat1='<div class="imgholder">.+?</div>'
                result1=str(re.compile(pat1).findall(file))                
                #pat2='href="/ArtZG/.+?" target="_blank">'
                #pat2='href="/ArtDD/.+?" target="_blank">'
                pat2='href="/rtys/.+?" target="_blank">'
                result2=str(re.compile(pat2).findall(result1))
                print(result2)
                pat3="\d+"
                result3=re.compile(pat3).findall(result2)                
                result3=list(set(result3))                
                for link in result3:
                    print(link)
                    craw(link)   
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                    time.sleep(2)
                    continue
                if hasattr(e,"reason"):
                    print(e.reason)
                    time.sleep(2)
                    continue
            except Exception as e:
                print("exception:读总表及分列表错误"+str(e))
                #若为Exception异常，延时1秒执行
                time.sleep(1)
t1=Get_real_adress()
t1.start()
t2=Save_file(urlqueue)
t2.start()