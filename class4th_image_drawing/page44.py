import turtle
import time

turtle.title("gradient")
turtle.setup(500,500,0,0)

xpos = 0
ypos = 0

blue = 1.0

size = 200

turtle.hideturtle()

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

time.sleep(10)

