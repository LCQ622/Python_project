# 访问限制，在属性前添加两个下划线，使其变成私有的 private
class Person (object):
    __name=None
    __age=0
    __gender=None

    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender


    def __str__(self):
        return "姓名：{0},性别：{1}，年龄：{2}".format(self.__name,self.__gender,self.__age)


    # 添加访问限制后，外部是不能直接访问到内部的属性，需要通过get 、set 方法来访问或者修改属性
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender


    def setName(self,name):
        self.__name=name

    def setAge(self,age):
        self.__age=age

    def setGender(self,gender):
        self.__gender=gender



p1=Person("张大彪",30,"男")

print(p1)

p1.setName("脏兮兮")
print(p1.getName())


p1.setAge(18)
p1.setGender("女")
print(p1)
