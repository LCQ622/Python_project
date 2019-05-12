# 递归函数
def test1(n):
    print("n={0}".format(n))
    if n==0:
        print("结束")
    else:
        test1(n-1)







def test02(n):
    print("n={0}".format(n))
    if n==0:
        print("over")
    else:
        test02(n-1)
    print("*n={0}".format(n))




def test03(n):
    '''
    计算阶乘
    :param n:
    :return:
    '''
    if n==1:
        return 1
    else:
        return n*test03(n-1)






def sum(n):
    '''
    使用递归设计的累加 1+2+3+4+...+n
    :param n:
    :return:
    '''
    if n==1:
        return 1
    else:
        return  n+sum(n-1)


print(sum(100))
