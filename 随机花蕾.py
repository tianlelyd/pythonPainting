import turtle
import random
turtle.tracer(100)


def drawLine(drawColor,a,b,ra,rb):
    turtle.left(90)
    turtle.color(drawColor)
    turtle.pensize(1.8)
    turtle.circle(ra,a/2)
    turtle.pensize(1.6)
    turtle.circle(ra,a/2)
    turtle.pensize(1.4)
    turtle.circle(-rb,b/2)
    turtle.pensize(1.2)
    turtle.circle(-rb,b/2)
    turtle.penup()
    turtle.right(180)
    turtle.circle(rb,b)
    turtle.circle(-ra,a)
    turtle.left(180)
    turtle.pendown()
    turtle.right(90)

def flower1(mySize,myLen,myColor):  #花 六个花瓣  参数：画笔size  花瓣len  颜色color
    turtle.pensize(mySize)
    turtle.color(myColor)
    turtle.pendown()
    time=0
    while time<6:
        turtle.fd(myLen)
        turtle.left(120)
        turtle.fd(myLen)
        turtle.right(60)
        time+=1
    turtle.penup()

def rflower(left,s,rlena,rlenb,k,stepa,stepb):  #画花的范围left 间隔s  花瓣大小  rCur  花间间隔stepa stepb
    while k>left:
        turtle.right(90)
        turtle.fd(-k)
        k-=s
        turtle.fd(k)
        turtle.left(90)
        twoCircle=0
        while twoCircle<360:
            c=random.randint(0,1)
            if c:
                flower1(random.randint(2,5),random.randint(rlena,rlenb),"#FF1493")
            else:
                flower1(random.randint(2,5),random.randint(rlena,rlenb),"#FFB6C1")
            turtle.penup()
            step=random.randint(stepa,stepb)
            turtle.circle(k,step)
            twoCircle+=step
    return left-5



#turtle.setup(600,600)
turtle.getscreen().bgcolor("black")
#turtle.speed(2000)

turtle.penup()
turtle.fd(250)
turtle.left(90)
'''
#delect start..........
turtle.pendown()
turtle.color("#FFFFFF")
turtle.circle(250,360)
turtle.penup()
#delete end............
'''
turtle.pendown()

#    深粉色 #FF1493
#    浅粉红 #FFB6C1
### 步骤1 ###

oneCircle=0
while oneCircle<720:
    ra=random.randint(100,150)  #曲线半径
    a=random.randint(10,30)  #曲线第一段的弧度
    rb=random.randint(50,200)  #曲线半径
    b=random.randint(10,30)  #曲线第二段的弧度
    if oneCircle<360:
        drawLine("#FF1493",a,b,ra,rb)
    else:
        drawLine("#FFB6C1",a,b,ra,rb)
    step=random.randint(3,7)
    turtle.penup()
    turtle.circle(250,step)
    turtle.pendown()
    oneCircle+=step

### 步骤2 ###
turtle.penup()
k=245
k=rflower(220,random.randint(10,20),1,3,k,3,20)
k=rflower(150,random.randint(30,50),2,6,k,20,50)
k=rflower(85,random.randint(50,70),5,15,k,50,100)


turtle.update()

turtle.done()
