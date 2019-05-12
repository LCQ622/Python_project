
# 递归求阶乘

def test(n):
    if n==1:
        return 1
    else:
        return n*test(n-1)


def test02(n):
    print(n)
    if n==1:
       print("结束")
    else:
        test02(n-1)
    print(n)

test02(5)