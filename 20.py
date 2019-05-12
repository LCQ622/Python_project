# 该方法将字符串写入e:/a.txt中
def write(str, model):
    f = open("e:/a.txt", model, encoding="utf-8")
    f.write(str)
    f.close()

# 该方法用于将e:/a.txt 的文本内容读取出来
def read():
    f = open("e:/a.txt", "r", encoding="utf-8")
    str = f.read()
    f.close()
    return str

# 该方法将字符串转换成Unicode的list
def toUnicode(str):
    NameList = list(str)
    numList = list()
    for i in NameList:
        numList.append(ord(i))
    return numList

# 该方法用于将含有Unicode数字的list转换成字符串
def unicodeToStr(numlist):
    strlist = list()
    for i in numlist:
        strlist.append(chr(i))
    str = "".join(strlist)
    return str





write("我叫傻强","a")