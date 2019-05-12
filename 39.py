# self 的使用 及析构函数

# 析构函数就是对象被销毁时执行的函数


class Person(object):
    __name=None
    __age=0
    __gender=None

    def __init__(self,name,age,gender):
        self.__age=age
        self.__name=name
        self.__gender=gender


    def __str__(a):
        return "姓名：{0}，年龄：{1}，性别：{2}".format(a.__name,a.__age,a.__gender)





    def __del__(self):
        print("{0},已经销毁".format(self.__name))


p1=Person("脏兮兮",18,"女")
print(p1)
# 使用del 销毁对象
del p1

print(p1)


for i in range(23000000):
    pass