# __str__ 和__repr__



# __str__ ():在调用print打印对象的时候自动调用，是给使用户一个描述对象的方法，类似于java的toString方法


# __repr__():是给命令行使用的，在Python解释器里面直接敲对象的名称回车后的调用的方法。


class Person (object):
    name=None
    age=0
    gender=None

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender


    # def __str__(self):
    #     return ("__str__姓名：{0},年龄：{1},性别：{2}".format(self.name,self.age,self.gender))

    def __repr__(self):
        return ("__repr__姓名：{0},年龄：{1},性别：{2}".format(self.name,self.age,self.gender))









p1=Person("傻强",18,"男")
print(p1)
