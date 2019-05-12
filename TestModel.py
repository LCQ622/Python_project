# 该模块用于测试模块的导入及使用

# 变量
name="傻强"
# 普通求和函数
def sum(a,b):
    print("{0}+{1}={2}".format(a,b,a+b))
#     累加和
def cusum(*args):
    sum=0
    for i in args:
        sum+=i
    print("累加和：{0}".format(sum))

if __name__=="__main__":
    print("我是主程序")
else:
    print("我是被当做模块被调用的")