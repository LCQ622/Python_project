def Test1():
    a=int(input("请输入数字"))
    if a>0:
        print("{0}".format(a)+" 大于零")
    elif a==0:
        print("{0}".format(a)+" 等于零")
    else:
        print("{0}".format(a)+" 小于零")

#测试空列表 列表是一个false
def  Test2():
    b=[]
    if b:
        print("b是一个非空列表")
    else:
        print("b是一个空列表")

# 空字符串 也是false 非空则反之
def Test3():
    c=""
    if c:
        print("c是一个字符串")
    else:
        print("c是一个空字符串")

# 数字 非零为 true 零则为false
def Test4():
    d=3
    if d:
        print("d是非零的数字")
    else:
        print("d是零")
