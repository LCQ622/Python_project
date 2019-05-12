import time
a="to be or not to be"
#分割字符串
b=a.split()
print(a.split())

'''
join()合并字符串
拼接字符串要点：
使用字符串拼接符“+”，会生成新的字符串对象，因此不推荐使用“+”来拼接字符串。
推荐使用join函数，因为join函数在拼接字符串之前会计算所有字符串的长度，
然后逐一拷贝，仅创建一次对象。

'''

print(" ".join(b))

#必须在join前边添加"".

print("* ".join(b))

# 进行耗时测试
# 现实中应该避免写这样的代码
time01=time.time()
c=""
for i in range(1000000):
    c+="哈哈"
time02=time.time()
print("耗时："+str(time02-time01))


time03=time.time()
li=[]
for i in range(1000000):
    li.append("哈哈")
time04=time.time()
print("耗时："+str(time04-time03))

