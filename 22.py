'''
迭代器
'''

def test01():
    li=[1,2,3,4]
    # 使用for 迭代器
    a=(i for i in li)

# 使用iter得到迭代器对象
def test02():
    li = [1, 2, 3, 4]
    b=iter(li)
    print(type(b))
    print(next(b))

# 使用iter  得到input 多行输入
def test03():
    str=""
    for line  in iter(input,"end"):
        str+=line+"\n"
    return str

