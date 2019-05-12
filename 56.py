#循环结构
def  sum(a):
    count=0
    sum=0
    while count<a:
        count+=1
        sum += count
    print(sum)



def even_sum(a):
    i=0
    sum=0
    while i<a:
        i += 1
        if i%2==0:
            sum+=i
    print(sum)

def odd_sum(a):
    i=0
    sum=0
    while i<a:
        i+=1
        if i%2!=0:
            sum+=i
    print(sum)


def  tese (a):
    i=0
    while i<a:
        i+=1
        if i%2==0:
            continue
        print(i,end="\t")

#  遍历字符串
def for1(str):
    for i in str:
        print(i)


# 遍历字典
def for2():
    d={"name":"傻强","age":18,"sex":"男"}
    #得到key值
    for i in d:
        print(i)
    # 得到key值
    for i in d.keys():
        print(i)
    # 得到values值
    for i  in d.values():
        print(i)
    #将字典中的键值对
    for i in d.items():
        print(i)

# 使用  range()生成可迭代对象
def for3():
    # 0-4
    for i in range(5):
        print(i)

    # 1-4 包头不包尾
    for i in range(1,5):
        print(i)

    for i in range(0,10,2):
        print(i)
for3()
