di = {"脏兮兮": 18, "傻强": 21, "张大喵": 19}

t=1,2,3,65,6885,66,12,56,di

def printlen(tuple):
    print("该元组的长度为：{0}".format(len(tuple)))
names=tuple(di)

print(names)
ages=list()
for i in names:
    ages.append(di.get(i))
age=tuple(ages)

print(age)
