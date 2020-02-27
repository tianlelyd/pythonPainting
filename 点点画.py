import turtle as t
screen = t.Screen()
t.getscreen()
t.tracer(100)
screen.setup(600,600)
t.hideturtle()
colors = ["red","green","yellow","blue4","blue","pink"]
for i in range(36):
    a=10*i
    for d in range(26):
        t.pu()
        t.home()
        t.seth(a)
        t.pd()
        b=3+d/18
        t.right(b*(d+1))
        t.pu()
        t.fd((10+d**2/29)*3.14*(b*(d+1)/180+2))
        t.pd()
        t.pencolor(colors[i%3*2+d%2])
        t.begin_fill()
        t.fillcolor(colors[i%3*2+d%2])
        t.circle(d/3)
        t.end_fill()    
t.pu()
t.home()
