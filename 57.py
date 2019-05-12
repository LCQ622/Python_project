# for 循环 和可迭代对象遍历

# 可迭代对象遍历==>遍历列表
def for_list():
    for i in [10, 59 ,69 ,"真好玩",364]:
        print(i)

# 可迭代对象遍历==>遍历元组
def for_tuple():
    for i in (12,56,231,88,"好开心"):
        print(i)
# 可迭代对象遍历==>遍历字符串
def for_str():
    for i in "to be or not to be":
        print(i)
# 可迭代对象遍历==>遍历字典
def for_dict():
    d=dict(name="傻强",age=18,sex="男",job="学生")
    # 遍历所有的键
    for i in d.keys():
        print (i)
    # 遍历所有的值
    for i in d.values():
        print (i)
    # 遍历所有的键值对
    for i in d.items():
        print(i)


def for_range():
    # for  i in range(5):
    #     print(i)
    #
    # 起始为1，结束为4（包头不包尾）
    # for  i in range(1,5):
    #     print(i)

    #选择步长
    for i in range(1,10,3):
        print(i)


# 计算 1-100 之间数字的累加和
def for_sum():
    sum=0
    for i in range(101):
        sum=sum+i
    print(sum)


# 计算 1-100 之间偶数的累加和
def for_even_sum():
    sum=0
    for i in range(101):
        if i%2==0:
            sum=sum+i
    print(sum)
# 计算 1-100 之间奇数的累加和。
def for_odd_sum():
    sum=0
    for i in range(101):
        if  i%2!=0:
            sum=sum+i
    print(sum)

# 嵌套for循环
def nesting_for(counter):
    for i in range(counter):
        for j in range(counter):
            print(i,end="\t")
        print()


# 打印乘法表
def print_multiplication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print ("{0}*{1}={2}".format(j,i,j*i),end="\t")
        print()


def print_salary():
    r1=dict(name="傻强",age=18,salary=30000,city="北京")
    r2=dict(name="脏兮兮",age=19,salary=20000,city="上海")
    r3=dict(name="陆大喵",age=20,salary=10000,city="深圳")
    tb=[r1,r2,r3]
    for i in tb:
        if i.get("salary")>15000:
            print(i)


print_salary()