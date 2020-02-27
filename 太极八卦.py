# -*- coding: utf-8 -*-
import turtle as t

screen = t.Screen()
screen.bgcolor("white")

t.speed(10)
t.pensize(8)
t.shape('turtle')


def draw_circle():
    t.penup()
    t.right(90)
    t.fd(50)
    t.pendown()

    t.fillcolor('black')
    t.begin_fill()
    t.left(90)
    t.circle(100, 180)

    t.circle(50, -180)
    t.left(180)
    t.circle(50, 180)
    t.end_fill()

    t.fillcolor('white')
    t.circle(100, -180)

    t.penup()
    t.goto(0, -16)
    t.pendown()

    t.fillcolor('white')
    t.left(180)
    t.begin_fill()
    t.circle(16)
    t.end_fill()

    t.penup()
    t.goto(0, 84)
    t.pendown()

    t.fillcolor('black')
    t.begin_fill()
    t.circle(16)
    t.end_fill()


def draw_qian():
    t.penup()
    t.goto(-40, 250)
    t.pendown()
    t.fd(80)

    t.penup()
    t.goto(-40, 230)
    t.pendown()
    t.fd(30)
    t.color('white')
    t.fd(20)
    t.color('black')
    t.fd(30)

    t.penup()
    t.goto(-40, 210)
    t.pendown()
    t.fd(80)


def draw_xun():
    lenght = [200, 180, 160]
    for i in lenght:
        t.penup()
        t.home()
        t.goto(0, 50)
        t.left(45)
        t.fd(i)

        t.left(90)
        t.fd(40)
        t.pendown()
        t.right(180)
        t.fd(30)
        t.color('white')
        t.fd(20)
        t.color('black')
        t.fd(30)


def draw_kan():
    t.penup()
    t.home()
    t.goto(0, 50)
    t.fd(200)
    t.left(90)
    t.fd(40)
    t.right(180)
    t.pendown()
    t.fd(30)
    t.color('white')
    t.fd(20)
    t.color('black')
    t.fd(30)

    t.penup()
    t.goto(180, 90)
    t.pendown()
    t.fd(80)

    t.penup()
    t.goto(160, 90)
    t.pendown()
    t.fd(80)


def draw_gen():
    lenght = [200, 180, 160]
    for i in lenght:
        t.penup()
        t.home()
        t.goto(0, 50)
        t.right(45)
        t.fd(i)
        t.left(90)
        t.fd(40)
        t.right(180)
        t.pendown()
        t.fd(80)


def draw_kun():
    t.penup()
    t.home()
    t.goto(-40, -150)
    t.pendown()
    t.fd(30)
    t.color('white')
    t.fd(20)
    t.color('black')
    t.fd(30)

    t.penup()
    t.goto(-40, -130)
    t.pendown()
    t.fd(80)

    t.penup()
    t.goto(-40, -110)
    t.pendown()
    t.fd(35)
    t.color('white')
    t.fd(10)
    t.color('black')
    t.fd(35)


def draw_zhen():
    for i in range(3):
        t.penup()
        t.home()
        t.goto(0, 50)
        t.right(135)
        t.fd(200 - 20 * i)
        t.left(90)
        t.fd(40)
        t.right(180)
        t.pendown()
        if i == 0:
            t.fd(80)
        else:
            t.fd(30)
            t.color('white')
            t.fd(20)
            t.color('black')
            t.fd(30)


def draw_li():
    t.penup()
    t.home()

    t.goto(-200, 10)
    t.pendown()
    t.left(90)
    t.fd(30)
    t.color('white')
    t.fd(20)
    t.color('black')
    t.fd(30)

    t.penup()
    t.goto(-180, 10)
    t.pendown()
    t.fd(30)
    t.color('white')
    t.fd(20)
    t.color('black')
    t.fd(30)

    t.penup()
    t.goto(-160, 10)
    t.pendown()
    t.fd(80)


def draw_dui():
    lenght = [200, 180, 160]
    for i in lenght:
        t.penup()
        t.home()
        t.goto(0, 50)
        t.left(135)
        t.fd(i)
        t.left(90)
        t.fd(40)
        t.left(180)
        t.pendown()
        if i == 160:
            t.fd(30)
            t.color('white')
            t.fd(20)
            t.color('black')
            t.fd(30)
        else:
            t.fd(80)


draw_circle()
draw_qian()
draw_xun()
draw_kan()
draw_gen()
draw_kun()
draw_zhen()
draw_li()
draw_dui()
t.hideturtle()
t.mainloop()
