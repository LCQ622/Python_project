# 文档字符串,对函数进行注释
import random


def sum(a,b):
    '''
    该函数用于进行加法运算
    :param a: 加数
    :param b: 另一个加数
    :return: 和
    '''
    return a+b
def sum(*args):
    li=list()
    for i in args:
        li.append(i*10)
    return  li

def sum (li):
    l=list()
    for i in li:
        l.append(i * 1000)
    return l


def createlist(len,start,end):
    '''
    该函数用于产生包含随机整数的列表
    :param len: 列表长度
    :param start: 随机数起始范围
    :param end: 随机整数结束范围
    :return:
    '''
    num=list()
    for i in range(len):
        num.append(random.randint(start,end))
    return num

s=createlist(10,1,10)
print(s)

print(sum(s))



