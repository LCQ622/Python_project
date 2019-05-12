'''
函数的定义
'''
# 无参数无返回值函数的定义
def myPrint():
    print("这是一个简单的函数")
    print("这是一个简单的函数")
    print("这是一个简单的函数")
# 无参数无返回值函数的调用
myPrint()


# 有参数 无返回值的函数
def myPrint(str):
    print(str)

myPrint("我叫傻强")

# 无参数 有返回值的函数
def getName():
    return "傻强"

print(getName())

# 有参数有返回值的函数
def sum(a,b):
    return  a+b


print(sum(2.6,63))

# 可变参数 有返回值 的函数
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum(1.03,2,64,5))