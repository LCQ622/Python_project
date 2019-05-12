#绘制多个坐标的折线，并计算A，B两点的距离
import turtle
import math

#定义多个点的坐标
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100

#绘制多个点的折线
turtle.penup()
turtle.goto(x1,y1)
turtle.write("A")
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
turtle.write("B")

#计算A，B两点的距离
value= math.sqrt((x1-y1)**2+(x4-y4)**2)

#将坐标移动到0,0
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
#写出计算A，B两点的距离
turtle.write(value)
