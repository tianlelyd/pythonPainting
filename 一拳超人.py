# 一拳超人

import turtle

# 头的轮廓
turtle.pensize(2)
turtle.color('black', '#F5DEB3')
turtle.begin_fill()
turtle.left(40)
turtle.circle(180, 50)
turtle.circle(90, 180)
turtle.circle(180, 50)
turtle.circle(30, 60)
turtle.circle(100, 40)
turtle.end_fill()
turtle.penup()
turtle.goto(-90, 180)  # 脸的中间位置
turtle.dot(10, 'white')
turtle.penup()


# 耳朵

# turtle.penup()


# 眉毛
# turtle.goto(-30, 0)  # 脸的中间位置
turtle.goto(-16, 140)  # 右边的眉毛起始位置
turtle.pendown()
turtle.forward(13)
turtle.right(75)
turtle.forward(50)

turtle.penup()
turtle.goto(-60, 140)  # 左边的眉毛起始位置
turtle.pendown()
turtle.right(-150)
turtle.forward(13)
turtle.right(-75)
turtle.forward(37)
turtle.penup()



# 眼睛
turtle.color('black', 'white')
turtle.goto(-60, 125)  # 左眼睛起始位置
turtle.pendown()
turtle.begin_fill()
turtle.right(40)
turtle.circle(70, 30)
turtle.circle(5, 170)
turtle.circle(90, 10)
turtle.circle(5, 170)
turtle.end_fill()
turtle.penup()

turtle.goto(30, 125)  # 右眼睛起始位置
turtle.color('black', 'white')
turtle.pendown()
turtle.begin_fill()
turtle.right(30)
turtle.circle(70, 30)
turtle.circle(5, 170)
turtle.circle(90, 10)
turtle.circle(5, 170)
turtle.end_fill()
turtle.penup()

# 眼睛珠子
turtle.goto(-95, 118)  # 左眼珠子位置
turtle.dot(5, 'black')
turtle.penup()

turtle.goto(-5, 125)  # 右眼珠子位置
turtle.dot(5, 'black')
turtle.penup()

# 鼻子
turtle.goto(-38, 118)
turtle.pendown()
turtle.left(90)
turtle.circle(120, 20)
# turtle.dot(10, 'red')
turtle.penup()


# 嘴巴
turtle.goto(-58, 50)
turtle.pendown()
turtle.left(80)
# turtle.dot(10, 'red')
turtle.circle(150, 20)



turtle.mainloop()