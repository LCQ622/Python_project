score=int(input("请输入分数:"))
grade="ABCDE"
num=0
# 选择结构嵌套
if score<0 or score >=100:
    print("请输入一个0-100之间的数")
else:
    num=score//10
    if num<6:num=5

    print("分数是：{0},等级为：{1}".format(score,grade[9-num]))

