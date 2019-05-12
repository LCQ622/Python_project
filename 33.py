import  datetime






# 时间的加减
t1=datetime.datetime.now()
t2=datetime.datetime(1997,8,1)
t3=t1-t2
print(t3)
print(type(t3))
#提起到t3的天
print(t3.days)
# 提取到t3除天数外的秒数
print(t3.seconds)