# 方法的重写

class Person:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age = age

    def say_name(self):
        print("我的名字是：{0}".format(self.__name))

    def __str__(self):
        return "name:{0},age:{1}".format(self.__name, self.__age)



class Student(Person):

    def __init__(self, name, age):
        super(Student,self).setName(name)
        super(Student,self).setAge(age)

    # 重写say_name方法
    def say_name(self):
        print("报告老师，我叫{0}".format(self.getName()))



p1=Person("傻强",18)
print(p1)
p1.say_name()

s1=Student("傻强",18)
print(s1)
s1.say_name()