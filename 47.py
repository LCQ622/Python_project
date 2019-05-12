# 多态

# 1.多态是方法的多态，属性没有多态
# 2.多态需要两个条件：继承、方法的重写
class  man(object):
    def eat(self):
        print("吃饭")


class Chinese(man):
    def eat(self):
        print("中国人用筷子吃饭")

class English(man):
    def eat(self):
        print("英国人用刀叉吃饭")


class African(man):
    def eat(self):
        print("非洲人用手吃饭")



def manEat(m):
    if isinstance(m,man):
        m.eat()
    else:
        print("不能吃饭")


manEat(Chinese())
manEat(English())
manEat(African())