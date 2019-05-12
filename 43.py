class Person(object):
    __name=None
    __age=0
    def __init__(self,name,age):
        self.__age=age
        self.__name=name

    def __str__(self):
        return"name:{0},age:{1}".format(self.__name,self.__age)


    def getName(self):
        return  self.__name

    def setName(self,name):
        self.__name=name
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age=age

class Student(Person):
    # 子类特有的属性
    __id=None
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
    def __init__(self,name,age,id):
        # 使用父类的东西
        super(Student,self).__init__(name,age)
        self.__id = id

    def __str__(self):
        return "name:{0},age:{1},id={2}".format(self.getName(),self.getAge(),self.getId())



s1=Student("脏兮兮",20,"3695546")

# # 输入对象的所有方法、属性
# print(dir(s1))

# # 对象属性字典
# print(s1.__dict__)


# 判断对象是不是另一个对象的实例

print(isinstance(s1,Student))