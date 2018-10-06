import turtle
import time

t=turtle.Pen()
t.color(0.9,0.75,0)

def triangle_m(s,fill): #s(size), fill(색채우기 여부)
    if( fill == True):
        t.begin_fill()
    for x in range(1,4):
        t.forward(s)
        t.left(120)
    if fill == True:
        t.end_fill()

t.color(0.9,0.75,0)
triangle_m(50,True)
triangle_m(150,False)
time.sleep(10)
