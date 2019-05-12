#效率测试

import math
import time


jd=0
#测试全局变量
def test01():
    start = time.time()
    for i in range(100000000):
        math.sqrt(30)
    end=time.time()
    return (end-start)

# 测试局部变量
def test02():
    sqrt=math.sqrt
    start = time.time()
    for i in range(100000000):
        sqrt(30)
    end = time.time()
    return (end - start)

def test03():
    print("进行一亿次数学运算")
    test1=test01()
    print("全局变量耗时：{0}".format(test1))
    test2=test02()
    print("局部变量耗时：{0}".format(test2))
    print("效率差异：{0}".format((test1-test2)))

test03()