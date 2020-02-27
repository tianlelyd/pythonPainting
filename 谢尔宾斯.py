#x谢尔宾斯
from turtle import*
a=0
def san(long):
    global a
    s=['yellow','red','blue']
    fillcolor(s[a%3])
    begin_fill()
    for i in range(3):
        fd(long)
        right(120)
    end_fill()
def xie(size,n):
    global a
    if n==1:
        san(size)
    else:
        xie(size/2,n-1)
        if n==3:
            a+=1
        right(60)
        fd(size/2)
        left(60)
        xie(size/2,n-1)
        if n==3:
            a+=1
        fd(size/2)
        left(120)
        fd(size/2)
        right(120)
        xie(size/2,n-1)
        if n==3:
            a+=1
        fd(-size/2)
pu()
goto(-130,150)
left(60)
speed(0)
st=['第一阶','第二阶','第三阶','第四阶','第五阶']
for b in range (1,6):
    pu()
    a=0
    clear()
    goto(-200,200)
    pd()
    co=pencolor()
    pencolor('black')
    write(st[b-1],font=("Arial", 18, "normal"))
    pencolor(co)
    pu()
    goto(-130,150)
    pd()
    for m in range(6):
        a=0
        xie(150,b)
        right(60)
        fd(150)
hideturtle()
update()
