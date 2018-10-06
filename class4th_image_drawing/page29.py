import turtle
import time
t=turtle.Pen()
def circle_m(r,g,b,s): # r(red), g(green), b(blue),s(size)
    t.color(r,g,b)
    t.begin_fill()
    t.circle(s)
    t.end_fill()

circle_m(0,1,0,50)
t.up()
t.forward(100)
t.down()
t.forward(50)
circle_m(0,0.5,0,100)

time.sleep(10)