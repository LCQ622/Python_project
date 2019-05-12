# 对象的浅拷贝跟深拷贝
import  copy

class Computer:
    def __init__(self,cpu,memory):
        self.cpu=cpu
        self.memory=memory

class  CPU:
    pass
class Memory:
    pass


cpu=CPU()
memory =Memory()

computer=Computer(cpu,memory)
print(computer)



print("普通对象赋值")
# 普通对象赋值
a=computer
print(a,a.cpu ,a.memory)
print(computer,computer.cpu ,computer.memory)

print("********************************")
print("浅拷贝")
b=copy.copy(computer)
print(computer,computer.cpu,computer.memory)
print(b,b.cpu,b.memory)
print("********************************")
print("深拷贝")
c=copy.deepcopy(computer)
print(computer,computer.cpu,computer.memory)
print(c,c.cpu,c.memory)

