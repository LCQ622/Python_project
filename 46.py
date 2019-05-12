# super()获得父类的定义

class Person:

    def __init__(self,name):
        self.name=name

    def say(self):
        print("{0},你好".format(self.name))




class Student(Person):
    def __init__(self,name):
        super(Student,self).__init__(name)




s=Student("傻强")
print(s.name)



