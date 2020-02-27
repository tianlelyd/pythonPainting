import turtle
import math


#画一个边长为a的正方形
def drawSquare(width):
    turtle.pensize(2)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.fillcolor("orange")
    for i in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

#画棋盘
def drawChess(width):

    for y in range(-4 * width, -width + 1, width):
        for x in range(-4*width,4*width,width):
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            drawSquare(width)
    turtle.penup()
    turtle.goto(-4*width, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("orange")
    for i in range(2):
        turtle.forward(8*width)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

    for y in range(width ,4 * width+ 1, width):
        for x in range(-4*width,4*width,width):
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            drawSquare(width)
    #画将营
    turtle.penup()
    turtle.goto(-width, -4*width)
    turtle.pendown()
    turtle.pensize(1)
    turtle.left(45)
    turtle.forward(2*math.sqrt(2) * width)
    turtle.penup()
    turtle.goto(-width, 5*width)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(2 * math.sqrt(2) * width)
    turtle.penup()
    turtle.goto(-width, -2 * width)
    turtle.pendown()
    turtle.forward(2 * math.sqrt(2) * width)
    turtle.penup()
    turtle.goto(-width, 3*width)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(2*math.sqrt(2) * width)
    #写楚河汉界
    turtle.penup()
    turtle.goto(-3*width, 1/5*width)
    turtle.pendown()
    turtle.color("green")
    turtle.write("楚  河  汉  界", font=('楷体',24, ))

    #写字
    listRed = ['车', '马', '象', '士', '帅', '士', '象', '马', '车']
    listBlack = ['车', '马', '相', '士', '将', '士', '相', '马', '车']
    x = -4 * width
    for i in range(9):
        turtle.penup()
        turtle.color("Red")
        turtle.goto(x+ 1 / 4 * width , -4 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.pensize(3)
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(1 / 3 * width)
        turtle.end_fill()

        turtle.penup()
        turtle.color("green")
        turtle.goto(x+ 1 / 4 * width , 5 * width- 1 / 4 * width )
        turtle.pendown()
        turtle.pensize(3)
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(1 / 3 * width)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(x- 1 / 4 * width , -4 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.color("Red")
        turtle.write(listRed[i], font=('楷体', 20,))
        turtle.penup()

        turtle.penup()
        turtle.goto(x- 1 / 4 * width , 5 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.color("green")
        turtle.write(listBlack[i], font=('楷体', 20,))
        turtle.penup()
        x = x + width
    x = -4 * width
    for i in range(5):
        turtle.penup()
        turtle.color("Red")
        turtle.goto(x + 1 / 4 * width, -width - 1 / 4 * width)
        turtle.pendown()
        turtle.pensize(3)
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(1 / 3 * width)
        turtle.end_fill()

        turtle.penup()
        turtle.color("green")
        turtle.goto(x + 1 / 4 * width, 2 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.pensize(3)
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(1 / 3 * width)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(x - 1 / 4 * width, -width - 1 / 4 * width)
        turtle.pendown()
        turtle.color("Red")
        turtle.write('兵', font=('楷体', 20,))
        turtle.penup()

        turtle.penup()
        turtle.goto(x - 1 / 4 * width, 2 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.color("green")
        turtle.write('卒', font=('楷体', 20,))
        turtle.penup()
        x = x +2* width
    x = -3 * width

    for i in range(2):
        turtle.penup()
        turtle.color("Red")
        turtle.goto(x +1 / 4 * width, -2 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.pensize(3)
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(1 / 3 * width)
        turtle.end_fill()

        turtle.penup()
        turtle.color("green")
        turtle.goto(x + 1 / 4 * width, 3 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.pensize(3)
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(1 / 3 * width)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(x - 1 / 4 * width, -2 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.color("Red")
        turtle.write('炮', font=('楷体', 20,))
        turtle.penup()

        turtle.penup()
        turtle.goto(x - 1 / 4 * width, 3 * width - 1 / 4 * width)
        turtle.pendown()
        turtle.color("green")
        turtle.write('炮', font=('楷体', 20,))
        turtle.penup()
        x = x +6* width

if __name__ == '__main__':
    turtle.tracer(10) 
    turtle.update()
    #turtle.speed(10)
    width=50
    drawChess(width)
    turtle.hideturtle()
    turtle.update()
    turtle.done()
