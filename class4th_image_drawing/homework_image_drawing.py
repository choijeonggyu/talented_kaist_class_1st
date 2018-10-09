import turtle
import time

turtle.title("FloorTiles & Cat's Foot Prints")
turtle.setup(500, 500, 0, 0)

# 배경은 파랑
turtle.bgcolor("blue")

# 거북이를 바닥의 맨 왼쪽으로 위치
turtle.up()
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(250)
turtle.right(180)
turtle.down()

turtle.speed(0)

# 바닥타일
for i in range(10):
    for j in range(10):

        if (i + j) % 2 == 1:
            turtle.pencolor("grey")
            turtle.fillcolor("grey")
        else:
            turtle.pencolor("black")
            turtle.fillcolor("black")

        turtle.begin_fill()
        # 타일 하나 그리기
        for k in range(4):
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(50)
    turtle.left(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)

# 고양이 발바닥
x = -40
y = -230
for i in range(10):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.color("white")

    # 큰발바닥
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    # 1th 발가락
    turtle.penup()
    x -= 15
    y += 30
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()
    # 2nd 발가락
    turtle.penup()
    x += 10
    y += 4
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()
    # 3rd 발가락
    turtle.penup()
    x += 10
    y += 0
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()
    # 4th 발가락
    turtle.penup()
    x += 10
    y -= 4
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()

    # 발자국은 지그재그로
    if i % 2 == 1:
        x += 80
    else:
        x -= 80
    y += 70

time.sleep(30)
