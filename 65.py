# 测试多个异常捕捉

def testException1():
    '''
    多个except 字句
    :return:
    '''
    try:
        a = int(input("请输入第一个数字："))
        b = int(input("请输入第二个数字："))
        print(a / b)
    except ZeroDivisionError:
        print("除数不能为0！！！")
    except ValueError:
        print("请输入整数！！！")



testException1()

def testException():
    '''
    使用一个except字句捕获多个异常，在元组中定义这些异常，
    :return:
    '''
    try:
        a=int(input("请输入第一个数字："))
        b=int(input("请输入第二个数字："))
        print(a/b)
    except (ZeroDivisionError ,ValueError) :
        print("您的输入有误，请检查您的输入！！！")
