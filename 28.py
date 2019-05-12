#eval()函数的使用
# 将字符串当成有效的表达式来求值并返回计算结果，也可以执行Python的代码
str="print('hello world')"
eval(str)

# 执行运算
a=10
b=30
print(eval("a+b"))

# 运算字典中的值=数值
di=dict(a=10,b=69)
print(eval("a+b",di))