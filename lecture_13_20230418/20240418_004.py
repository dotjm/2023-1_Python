import turtle

t = turtle.Turtle()
t.shape("turtle")

slist = [120, 56, 309, 220, 156, 23, 98]

def drawpic(h):
    t.left(90)
    t.fd(h)
    # t.write(str(h))
    t.right(90)
    t.fd(5)
    t.write(str(h))
    t.fd(35)
    t.right(90)
    t.fd(h)
    t.left(90)


for i in slist:
    drawpic(i)


turtle.mainloop()