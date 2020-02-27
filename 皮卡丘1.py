import turtle as t


def nose():
    t.penup()
    t.seth(90)
    t.fd(100)
    t.pendown()
    t.begin_fill()
    t.fillcolor('black')
    t.seth(45)
    t.fd(25)
    t.seth(135)
    t.circle(25,90)
    t.seth(315)
    t.fd(25)
    t.end_fill()


def eyes(seth,fd,c):
    t.penup()
    t.seth(seth)
    t.fd(fd)
    t.pendown()
    t.begin_fill()
    t.fillcolor('black')
    t.circle(50)
    t.end_fill()

    t.penup()
    t.circle(50, c)
    t.pendown()
    t.begin_fill()
    t.fillcolor('white')
    t.circle(20)
    t.end_fill()


def face(seth,fd):
    t.penup()
    t.seth(seth)
    t.fd(fd)
    t.pendown()
    t.begin_fill()
    t.fillcolor('red')
    t.circle(70)
    t.end_fill()

def lip():
    t.penup()
    t.seth(135)
    t.fd(250)
    t.pendown()
    t.seth(-300)
    t.circle(30, -65)
    t.begin_fill()
    t.fillcolor('Firebrick')
    t.seth(165)
    t.fd(140)
    t.seth(195)
    t.fd(140)
    t.seth(-360)
    t.circle(30, -65)
    t.penup()
    t.seth(-60)
    t.circle(30, 65)
    t.pendown()
    t.seth(-70)
    t.fd(240)
    t.circle(55, 140)
    t.seth(70)
    t.fd(240)
    t.end_fill()
    t.seth(-110)
    t.fd(80)
    t.begin_fill()
    t.fillcolor('Firebrick1')
    t.seth(120)
    t.circle(120, 123)
    t.seth(-70)
    t.fd(165)
    t.circle(55, 140)
    t.seth(72)
    t.fd(165)
    t.end_fill()

def setting():
    t.pensize(4)
    t.hideturtle()
    t.setup(1000, 600)
    t.speed(10)
    t.screensize(bg='yellow')

def main():
    setting()
    nose()
    eyes(160, 250, 60)
    eyes(-9.5, 530, 230)
    face(195, 600)
    face(-11, 720)
    lip()
    t.done()

if __name__ =='__main__':
    main()





