def Test01():
    for i in range(3):
        a = int(input("请输入一个数:"))
        if a < 10:
            print("小于10")
        if a > 10:
            print("大于10")
        if a == 10:
            print("等于10")


# 单分支选择结构

def one():
    if True:
        print("我叫傻强")


# 双分支结构
def double():
    if int(input("请输入数字：")) < 10:
        print("小于10")
    else:
        print("大于或等于10")





# 三目运算符
def three_orders():
    print("小于10") if int(input("请输入一个数：")) < 10 else print("大于等于10")




def grade():
    score = int(input("请输入分数："))
    if 90 <= score <= 100:
        print("优秀")
    elif 80 <= score <= 89:
        print("良好")
    elif 60 <= score <= 79:
        print("及格")
    elif score > 100:
        print("不在范围内")
    else:
        print("不及格")


# 多分支结构的另外的思路
def Grade():
    score = int(input("请输入分数："))
    str = ""
    if score < 60:
        str = "不及格"
    elif score < 80:
        str = "及格"
    elif score < 90:
        str = "良好"
    else:
        str = "优秀"
    # 这里使用的是占位符
    print("分数是：{0} 等级是：{1}".format(score, str))


#小练习：已知坐标X、Y，判断其在第几象限
def quadrant():
    x = int(input("请输入x坐标"))
    y = int(input("请输入y坐标"))
    if x == 0 and y == 0:
        print("点（{0}，{1})".format(x, y) + "在原点")
    elif x > 0 and y > 0:
        print("点（{0}，{1})".format(x, y) + "在第一象限")
    elif x < 0 and y > 0:
        print("点（{0}，{1})".format(x, y) + "在第二象限")
    elif x < 0 and y < 0:
        print("点（{0},{1}）".format(x, y) + "在第三象限")
    elif x>0 and y<0:
        print("点（{0},{1}）".format(x, y) + "在第四象限")



