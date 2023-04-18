import turtle

t = turtle.Turtle()
t.shape('turtle')

s = turtle.Screen()

def draw(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('red')
    square()
    t.end_fill()

def square():
    for i in range(4):
        t.fd(100)
        t.right(90)

s.onscreenclick(draw)

turtle.mainloop()