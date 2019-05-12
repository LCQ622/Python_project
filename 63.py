class  person (object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def __str__(self):
        return "姓名：{0},年龄：{1}，性别：{2}".format(self.name,self.age,self.gender)




p=person("傻强",22,"男")

print(p)