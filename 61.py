import urllib.request
import re
url="http://www.baidu.com"
page=urllib.request.urlopen(url).read()
page=page.decode('utf8') #转码
title=re.findall('<title>(.*?)</title>',page,re.S)#re.S表示.可以代表\n
print(title)
