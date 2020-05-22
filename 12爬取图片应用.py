import urllib.request
import urllib.error
import re


#url="https://rtys6.com/ArtZG/2142/1.html"

#def craw(url,page):
#    file=urllib.request.urlopen(url).read() 
#    file=str(file)
#    pat1='<div class="imgbox.+? <div id="contentsx">'
#   # pat1='<div id="plist".+? <div class="page clearfix">'
#    pat2='<img src="https://(.+?\.jpg)">'
#    result1=re.compile(pat1).findall(file)
#    result1=result1[0]
#    imagelist=re.compile(pat2).findall(result1)
#    print(imagelist)
#    x=1
#    for imageurl in imagelist:
#        imagename="E:/100_Python\120_Program"+str(page)+str(x)+".jpg"
#        imageurl="http://"+imageurl
#        try:    
#            urllib.request.urlretrieve(imageurl,filename=imagename)
#        except urllib.error.URLError as e:
#            if hasattr(e,"code"):
#                x+=1
#            if hasattr(e,"reason"):
#                x+=1
#        x+=1
#for i in range(1,43):
#    url="https://rtys6.com/ArtZG/2142/"+str(i)+".html"
#    craw(url,i)
x=0
def craw(url,i):
    imagename="E:/100_Python/120_Program/photo/20131224OM/"+"20131224OM"+str(i)+".jpg"
    print(url)    
    try:    
        urllib.request.urlretrieve(url,filename=imagename)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            x=1
            
        if hasattr(e,"reason"):
            x=1
    

for i in range(1,1500):
    
    #url="https://p.666ho.com/pic/2018/0601/"+str(i)+".jpg"
    url="https://p.666ho.com/Art/OM/201312/24/"+str(i)+".jpg"
    craw(url,i)
    


