#黄昏 --运行出错，待修复 by liyd
from turtle import*
#设置画布大小位置
hideturtle()
penup()
speed(300)
goto(-300,-50)
rgb=[255,0,15]
pensize(3.5)
num=0
pendown()
#绘制黄昏渐变色天空
for i in range(0,100):
    rgb=[255,75+num,15]
    color(rgb[0],rgb[1],rgb[2])
    forward(600)
    if num%2==0:
        left(90)
        forward(3.5)
        left(90)
    else:
        right(90)
        forward(3.5)
        right(90)
    num=num+1
#绘制渐变色海洋
penup()
goto(-300,-50)
num=0
pensize(2.5)
pendown()
for i in range(0,100):
    rgb=[255,75+num,50]
    color(rgb[0],rgb[1],rgb[2])
    forward(600)
    if num%2==0:
        right(90)
        forward(2.5)
        right(90)
    else:
        left(90)
        forward(2.5)
        left(90)
    num=num+1
#绘制落日
speed(8)
penup()
goto(216.5,-50)
left(120)
pendown()
color(235,217,0)
begin_fill()
circle(250,120)
left(120)
fd(433)
end_fill()
#绘制落日在海中的倒影
right(150)
color(232,201,23)
begin_fill()
circle(-433,60)
right(150)
fd(433)
end_fill()
#绘制波浪
penup()
pensize(3)
color(130,55,12)
goto(-300,-50)
pendown()
fd(600)
num=0
for i in range(0,5):
    if num%2==0:
        right(90)
        penup()
        fd(50)
        right(90)
    else:
        left(90)
        penup()
        fd(50)
        left(90)
    fd(30)
    pendown()
    fd(30)
    penup()
    fd(20)
    pendown()
    fd(10)
    penup()
    fd(80)
    pendown()
    fd(20)
    penup()
    fd(10)
    pendown()
    fd(10)
    penup()
    fd(120)
    pendown()
    fd(20)
    penup()
    fd(80)
    pendown()
    fd(30)
    penup()
    fd(70)
    pendown()
    fd(15)
    penup()
    fd(75)
    num=num+1
#绘制船体
goto(-30,-65)
color(26,130,38)
pensize(2)
left(180)
begin_fill()
pendown()
fd(60)
left(45)
fd(28.28)
left(135)
fd(100)
left(135)
fd(28.28)
end_fill()
penup()
#绘制船帆
left(45)
goto(-25,-35)
color(242,217,175)
begin_fill()
pendown()
fd(50)
left(90)
fd(60)
left(90)
fd(50)
left(90)
fd(60)
end_fill()
penup()
#绘制桅杆
goto(0,-45)
color(89,61,13)
pendown()
left(180)
pensize(3)
fd(90)
right(90)
penup()
goto(-10,35)
pensize(3)
pendown()
fd(20)
pensize(1)
penup()
goto(-15,10)
pendown()
fd(30)
penup()
goto(-15,-5)
pendown()
fd(30)
penup()
goto(-15,-20)
pendown()
fd(30)
#绘制海鸥
penup()
goto(-200,150)
left(45)
color(26,54,94)
pensize(3)
pendown()
fd(40)
penup()
goto(-186,164)
left(30)
pendown()
fd(40)
penup()
goto(-186,164)
left(60)
pendown()
fd(15)
left(110)
fd(30)
penup()
goto(-120,230)
right(200)
pendown()
fd(40)
penup()
goto(-106,244)
left(30)
pendown()
fd(40)
penup()
goto(-106,244)
left(60)
pendown()
fd(15)
left(110)
fd(30)