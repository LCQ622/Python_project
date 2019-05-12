# break语句
# 在while中使用break 语句
def while_break():
    i = 0;
    while True:
        print(i)
        if i == 10:
            break
        i = i + 1


# 在while 中使用continue语句
def while_continue():
    i = 0
    while True:
        i = i + 1
        if i == 6:
            continue
        if i == 10:
            break
        print(i)

# 【操作】要求输入员工的薪资，若薪资小于 0 则重新输入。最后打印出录入员工的数量和
# 薪资明细，以及平均薪资
def  Salary():
    num=0
    SalarySum=0
    salarys=[]
    while True:
        s=input("请输入员工的薪资（按Q或者q退出）：")
        if s.upper()=="Q":
            print( "录入完成"if num != 0 and SalarySum != 0 and salarys != None else "程序已经退出")
            break
        if float(s)<0:
            continue
        num+=1
        salarys.append(float(s))
        SalarySum+=float(s)

    if num!=0 and SalarySum!=0 and salarys!=None:
        print("员工总人数：{0}".format(num))
        print("录入薪资：{0}".format(salarys))
        print("平均工资：{0}".format(SalarySum/num))

Salary()
