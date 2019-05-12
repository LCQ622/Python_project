# 嵌套函数


def printName(Chinese,Name,LastName):
    def init(a,b):
        print("姓名：{0}{1}".format(a,b))
    if Chinese:
        init(Name,LastName)
    else:
        init(LastName,Name)




#nonlocal关键字的使用 类似global 。

def test():
    b=20

    def inner():
        nonlocal b
        print(b)
        b=10
        print(b)
    inner()
    print(b)


test()