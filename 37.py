import urllib.request
a=urllib.request.urlopen("https://www.baidu.com/")
print(a.read().decode("utf-8"))