

##代理服务器
#def use_proxy(proxy_addr,url):
#    import urllib.request
#    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
#    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#    data=urllib.request.urlopen(url).read().decode('utf-8')
#    return data
#proxy_addr="123.169.164.125:9999"
#data=use_proxy(proxy_addr,"http://www.baidu.com")
#print(data)

def use_proxy(proxy_addr,url):
    import urllib.request
    proxy= urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr="125.73.220.18:49128"
data=use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))