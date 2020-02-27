# 使用python turtle 进行书法和印章，需要注意：
# 1、由于不同平台上的字体大小似乎有不一致情况，需做微小调整,比如我发现在mac上面的字体比windows下的要小;
# 2、字体名称不平同台可能也会不同,比如「沙孟海书法字体」在mac下导入发现名字叫「uming」
from turtle import *

def writeT(mystr, fontsize=60):
    pendown()
    write(mystr, font=('uming', fontsize, 'normal'))
    penup()
def yinzhang():
    pensize(2)
    pencolor('red')
    pendown()
    for i in range(4):
        forward(56)
        left(90)
    goto(-156, -70)
    write('匠一\n人石', font=('经典繁方篆', 25, 'normal'))
    penup()
def yinzhang2():
    pensize(3)
    pencolor('white')
    fillcolor('red')
    begin_fill()
    for i in range(4):
        forward(56)
        left(90)
    end_fill()
    goto(-156, -140)
    write('匠一\n人石', font=('经典繁方篆', 25, 'normal'))
    penup()
def action():
    penup()
    goto(30, -200)
    writeT('用\n心\n若\n镜', 60)
    goto(-70, -200)
    writeT('胜\n物\n不\n伤', 60)
    goto(-140, 0)
    writeT('一\n石', 15)
    goto(-160, -70)
    yinzhang()
    goto(-160, -140)
    yinzhang2()
    hideturtle()
def action2():
    penup()
    goto(30, -200)
    write('无\n用\n之\n用', font=('迷你繁篆书', 70, 'normal'))
    goto(-70, -200)
    write('是\n为\n大\n用', font=('迷你繁篆书', 70, 'normal'))
    goto(-140, 0)
    writeT('一\n石', 15)
    goto(-160, -70)
    yinzhang()
    goto(-160, -140)
    yinzhang2()
    hideturtle()

action()
# action2()
done()
