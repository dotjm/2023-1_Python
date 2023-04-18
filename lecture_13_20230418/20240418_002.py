import turtle

t = turtle.Turtle()
t.shape('turtle')

s = turtle.Screen()

def draw(x, y):
    t.goto(x, y)

t.pensize(10)

s.onscreenclick(draw)

turtle.mainloop()