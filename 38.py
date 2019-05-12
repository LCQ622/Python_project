# 定义类
'''
语法格式：
class 类名(父类列表):
    属性

    方法


'''

class Person(object):
    name=None
    age=0
    gender=None

    def __init__(self,name,age,gender):
        '''
        构造函数，固定格式
        :param name:
        :param age:
        :param gender:
        '''
        self.name=name
        self.age=age
        self.gender=gender
    # 类定义方法的一个参数必须是self
    def run(self):
        print("会奔跑")

    def eat(self,food):
        print("吃{0}".format(food))


    def __str__(self):
        '''
        该方法类似java的toString方法，固定格式
        :return:
        '''
        return "姓名：{0}，年龄：{1}，性别：{2}".format(self.name,self.age,self.gender)


#对象的实例化
p1=Person(name="傻强",gender="男",age=20)
p2=Person("脏兮兮",18,"女")
print("p1:",p1)
print("p2:",p2)



