'''
os.path 的使用。
'''

import  os
# 通过相对路径获取绝对路径。
print(os.path.abspath("./脏兮兮"))

# 拼接路径
p1=os.getcwd()
p2="testjoin"
print(os.path.join(p1,p2))
# 拆分路径
p1=r"D:\Project\Python project\test"
p=os.path.split(p1)
print(type(p))
print(p)

#获取拓展名
p1=r"D:\Project\Python project\test.abc"
file=os.path.splitext(p1)
print(type(file))
print(file)

# 判断是否为目录
p1=r"D:\Project\Python project"
print(os.path.isdir(p1))



# 判断文件是否存在
p1=r"D:\Project\Python project\a.txt"
print(os.path.isfile(p1))
#获取文件的目录
p1=r"D:\Project\Python project\a.txt"
print(os.path.dirname(p1))

# 获取文件名
p1=r"D:\Project\Python project\a.txt"
print(os.path.basename(p1))
