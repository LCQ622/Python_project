# 测试异常

class Print(object):
    flag=False

    def division(self,a,b):

        try:
            return a/b

        except ZeroDivisionError:
            if self.flag:
                print("除数不能为零！！！")
            else:
                raise



p=Print()
p.flag=True
print(p.division(12,0))