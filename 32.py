# 时间模块的使用
import time

#
# # 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间以秒为单位的浮点小数,来表示当前时间戳
# t1=time.time()
# print(t1)
#
# t2=time.time()
# t2=time.gmtime(t2)
# print(type(t2))
# print(t2)
#
# # 本机时间元组
# t3=time.time()
# localtime=time.localtime(t3)
# print(localtime)
#
#
#
#
#
#
#
#
# # 将本机时间转换成时间戳
#
# print(time.mktime(time.localtime()))
#
#
#
# # 将时间元组转换成字符串
# print("本机时间：",time.asctime(time.localtime()))
# print("格林尼治时间：",time.asctime(time.gmtime()))
#
# # 时间戳转换为字符串
# print(time.ctime(time.time()))
#


# # 格式化日期,将时间元组转换成格式化字符串
# t1=time.localtime()
# s=time.strftime("%Y-%m-%d %H:%M:%S",t1)
# print(s)

# # 将字符串格式化为时间元组
# str="2050-02-25 21:09:22"
# print(time.strptime(str,"%Y-%m-%d %H:%M:%S"))

# 休眠（延迟）一个时间，参数为整型或者浮点型的秒

for i in range(10):
    time.sleep(1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
