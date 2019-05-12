a=10
def test():
    global a
    a=100
    print("函数里变量a的值:{0}".format(a))



test()
print("函数外变量a的值:{0}".format(a))




