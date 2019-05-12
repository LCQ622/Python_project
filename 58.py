# 计算学生成绩
students=[]
num=0
while True:
    score=input("请输入学生成绩，输入Q或者q退出")
    if score.upper()=="Q":
        break
    if float(score) >= 0:
        students.append(float(score))
        num+=1

else:
    print("输入完毕")

sum=0
for i in range(len(students)):
    sum+=students[i]
print("总分：{0},平均分：{1}".format(sum,sum/num))

str=input("输入任意键退出")

print("程序退出")