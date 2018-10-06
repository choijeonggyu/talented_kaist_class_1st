import turtle
import time



def backFill(b, c, x, y, l, h):
    b.penup()
    b.setpos(x, y)
    b.color(c)
    b.pendown()
    b.begin_fill()
    for side in range(2):
        b.forward(l)
        b.left(90)
        b.forward(h)
        b.left(90)
    b.end_fill()

def drawCloud(c, x, y):
    c.penup()
    c.setpos(x, y)
    c.pendown()
    c.color("grey")
    c.begin_fill()
    for side in range(5):
        c.circle(10)
        c.left(80)
    c.end_fill()

def main():
    print("Cars")
    joe = turtle.Turtle()
    joe.speed(0)

    backFill(joe,"green",-200,-100,400,25)
    backFill(joe,"black",-200,-75,400,75)
    backFill(joe,"green",-200,0,400,25)
    backFill(joe,"sky blue",-200,25,400,110)

    x=-192.5
    for side in range(10):
     backFill(joe,"yellow",x,-40,25,5)
     x=x+40

    x=-180
    y=100
    for side in range(15):
     drawCloud(joe,x,y)
     x=x+40
     y=y-10

main()

turtle.title("gradient")
turtle.setup(500,500,0,0)

xpos = 0
ypos = 0

blue = 1.0
red = 1.0
green = 1.0


size = 200

turtle.hideturtle()
turtle.bgcolor(0.5,0.5,0.5)

turtle.up()
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(250)
turtle.right(180)

turtle.down()

# 바다 그리기
turtle.pencolor(0, 0, blue)
turtle.fillcolor(0, 0, blue)
turtle.begin_fill()

turtle.forward(500)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(500)
turtle.end_fill()

turtle.up()

# 구름 그리기
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.down()

#기반 구릅
turtle.pencolor(0.4, 0.4, 0.4)
turtle.fillcolor(0.4, 0.4, 0.4)
turtle.begin_fill()

turtle.forward(500)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(500)
turtle.end_fill()

# 짙은 구름
turtle.pencolor(0.45, 0.45, 0.45)
turtle.fillcolor(0.45, 0.45, 0.45)
turtle.begin_fill()

turtle.right(160)
turtle.forward(250)
turtle.right(110)
turtle.forward(90)
turtle.right(90)
turtle.forward(210)
turtle.end_fill()

# 용오름








"""
for x in range(10):
    turtle.pencolor(0,0,blue)
    turtle.fillcolor(0,0,blue)
    turtle.begin_fill()
    for y in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

    xpos +=10
    ypos -=10
    blue -=0.1
    size -=20

    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
"""
time.sleep(10)

