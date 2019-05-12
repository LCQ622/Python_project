#类的的定义
class Student:

    def __init__(self,name,age,gender):
        '''
        构造函数，固定格式：__init__函数名，第一个参数必须为self
        :param name:
        :param age:
        :param gender:
        '''
        self.name=name
        self.age=age
        self.gender=gender
    def say_info(self):
        '''
        函数的第一个使用
        :return:
        '''
        print("姓名：{0},年龄：{1}，性别：{2}".format(self.name,self.age,self.gender))




s1=Student("脏兮兮",18,"女")
s1.say_info()