import turtle
import time

t=turtle.Pen()
def ms(size):
    for i in range(1,4):
        t.forward(size)
        t.left(120)

ms(10)
ms(25)
ms(50)
ms(75)
ms(100)
time.sleep(10)
