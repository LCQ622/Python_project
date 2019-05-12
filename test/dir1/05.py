'''
绘制奥运五环

'''
import turtle
turtle.width(5)


turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(-120,0)
turtle.pendown()
turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(-60,-40)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(60,-40)
turtle.pendown()
turtle.color("green")
turtle.circle(50)
