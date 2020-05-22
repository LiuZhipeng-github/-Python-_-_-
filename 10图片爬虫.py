import urllib.request
import urllib.error
import re


#https://list.jd.com/list.html?cat=670,671,672&page=3&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main
#https://list.jd.com/list.html?cat=670,671,672&page=2&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main
#url="https://list.jd.com/list.html?cat=670,671,672&page=3&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"

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
