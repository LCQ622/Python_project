#coding:utf-8
import turtle

def nose(x,y):#鼻子
    turtle.penup()#提起笔
    turtle.goto(x,y)#定位
    turtle.pendown()#落笔，开始画
    turtle.setheading(-30)#将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    turtle.begin_fill()#准备开始填充图形
    a=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            turtle.left(3) #向左转3度
            turtle.forward(a) #向前走a的步长
        else:
            a=a-0.08
            turtle.left(3)
            turtle.forward(a)
    turtle.end_fill()#填充完成

    turtle.penup()
    turtle.setheading(90)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(10)
    turtle.pendown()
    turtle.pencolor(255,155,192)#画笔颜色
    turtle.setheading(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160,82,45)#返回或设置pencolor和fillcolor
    turtle.end_fill()

    turtle.penup()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.pendown()
    turtle.pencolor(255,155,192)
    turtle.setheading(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160,82,45)
    turtle.end_fill()

def head(x,y):#头
    turtle.color((255,155,192),"pink")
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(180)
    turtle.circle(300,-30)
    turtle.circle(100,-60)
    turtle.circle(80,-100)
    turtle.circle(150,-20)
    turtle.circle(60,-95)
    turtle.setheading(161)
    turtle.circle(-300,15)
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pendown()
    turtle.setheading(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            turtle.lt(3) #向左转3度
            turtle.fd(a) #向前走a的步长
        else:
            a=a-0.08
            turtle.lt(3)
            turtle.fd(a)
        turtle.end_fill()

def ears(x,y): #耳朵
    turtle.color((255,155,192),"pink")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(100)
    turtle.circle(-50,50)
    turtle.circle(-10,120)
    turtle.circle(-50,54)
    turtle.end_fill()

    turtle.penup()
    turtle.setheading(90)
    turtle.forward(-12)
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(100)
    turtle.circle(-50,50)
    turtle.circle(-10,120)
    turtle.circle(-50,56)
    turtle.end_fill()

def eyes(x,y):#眼睛
    turtle.color((255,155,192),"white")
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(-20)
    turtle.setheading(0)
    turtle.forward(-95)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.color("black")
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(12)
    turtle.setheading(0)
    turtle.forward(-3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

    turtle.color((255,155,192),"white")
    turtle.penup()
    turtle.seth(90)
    turtle.forward(-25)
    turtle.seth(0)
    turtle.forward(40)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.color("black")
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(12)
    turtle.setheading(0)
    turtle.forward(-3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

def cheek(x,y):#腮
    turtle.color((255,155,192))
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

def mouth(x,y): #嘴
    turtle.color(239,69,19)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(-80)
    turtle.circle(30,40)
    turtle.circle(40,80)

def setting():          #参数设置
    turtle.pensize(4)
    turtle.hideturtle()        #使乌龟无形（隐藏）
    turtle.colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    turtle.color((255,155,192),"pink")
    turtle.setup(840,500)
    turtle.speed(10)

def main():
    setting()           #画布、画笔设置
    nose(-100,100)      #鼻子
    head(-69,167)       #头
    ears(0,160)         #耳朵
    eyes(0,140)         #眼睛
    cheek(80,10)        #腮
    mouth(-20,30)       #嘴
    turtle.done()

if __name__ == '__main__':
    main()