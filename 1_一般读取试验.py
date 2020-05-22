import urllib.request
file=urllib.request.urlopen("http://www.baidu.com")
data=file.read()
dataline=file.readlines()
print(data)
#print(dataline)

#Method1
fhandle=open("D:/Python/1.html","wb")
fhandle.write(data)
fhandle.close()

##Method2
#filename=urllib.request.urlretrieve("http://www.163.com",filename="D:/Python/2.html")
#urllib.request.urlcleanup()

##
##file.info()
##print(file)
#file.getcode()
#print(file)
#file.geturl()
#print(file)