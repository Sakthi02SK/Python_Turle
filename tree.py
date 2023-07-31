import turtle as s
s.bgcolor("black")
s.left(90)
s.speed(100)
s.pencolor("white")
s.pensize(3)
def t(i):
    if i<10:
        return
    else:
        s.fd(i)
        s.lt(30)
        t(3*i/4)
        s.rt(60)
        t(3*i/4)
        s.lt(30)
        s.bk(i)     
t(60)
s.mainloop()