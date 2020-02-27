#补圆
import turtle as t
import math as ma
t.pu()
t.goto(0,-150)
t.pd()
y=60
t.left(60)
a=3
c=ma.radians (360)
for j in range (6):
    t.color(1-j/6,1,j/6)
    t.begin_fill()
    for i in range (a):
        d=ma.sin(c/(a*2))
        t.fd(200*d*2)
        t.left(360/a)
    t.end_fill()
    a=a*2
    y=y/2
    t.right (y)
t.right(y)
t.color ("black")
t.circle(200)

t.done()
    

