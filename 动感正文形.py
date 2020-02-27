# -*- coding: utf-8 -*-
import turtle
turtle.speed(0)
class cube:
  def __init__(self, side,angle):
    self.s = side
    self.a=angle
    turtle.seth(self.a)
    for i in range(4):
      turtle.fd(self.s)
      turtle.lt(90)
for i in range(1,5):
  cl=["","red","green","blue","rose"]
  turtle.pencolor(cl[i])
  for j in range(12):
    turtle.pensize(i)
    #turtle.clear()
    cube(i*50,j*30)