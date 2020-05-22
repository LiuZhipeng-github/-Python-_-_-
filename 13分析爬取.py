import urllib.request
import urllib.error
import re
import queue
import time
import datetime

#'''批量'''
ac=1

def crawphoto(url):  
    global ac
    imagename="E:/100_Python/120_Program/photo/0407/"+str(ac)+".jpg"
    print(url)    
    try:    
        urllib.request.urlretrieve(url,filename=imagename)
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
        print("exception:"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)
    
def craw(url):
    try:
        url="https://rtys6.com/ArtZG/"+url
        print(url)
        file1=urllib.request.urlopen(url).read() 
        file1=str(file1)
        pat5="https://p.666ho.com/tu/allimg/(.+?)-lp\.jpg"
        #pat5="https://p.666ho.com/pic/(.+?)-lp\.jpg"  20页之后更换
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
        print("exception:"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)
    
    #dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #ts=int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
    for link in result5:        
        url="https://p.666ho.com/tu/allimg/"+link+".jpg"
        #url="https://p.666ho.com/pic/"+link+".jpg"
        crawphoto(url)
        global ac
        ac=ac+1

def geturl():
    for i in range(124,1000):#124
        print(str(i)+"+++++++++++++++++++++++++")  
        url="https://rtys6.com/ArtZG/list"+str(i)+".html"
        try:
            file=urllib.request.urlopen(url).read() 
            file=str(file)
            pat1='<div class="fzltp">.+?</ul>'
            result1=str(re.compile(pat1).findall(file))
            #print(result1)
            pat2='href="/ArtZG/.+?" target="_blank">'
            result2=str(re.compile(pat2).findall(result1))
            #print(result2)
            pat3="\d+"
            result3=re.compile(pat3).findall(result2)
            #print(result3[2])
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
            print("exception:"+str(e))
            #若为Exception异常，延时1秒执行
            time.sleep(1)
    
geturl()

    