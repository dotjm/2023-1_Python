# 4장

import turtle

t = turtle.Turtle()
t.shape("turtle")

def draw():
    pass

def box():
    t.pendown()
    for i in range(4):
        t.fd(100)
        t.right(90)
    t.penup()

i = 0
while i < 3:
    box()
    t.fd(150)
    i += 1


turtle.mainloop()