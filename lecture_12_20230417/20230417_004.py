import turtle
t = turtle.Turtle()
t.shape('turtle')

n = int(input("몇 각형 : "))
cnt = int(input("몇 개 : "))

def draw(n):
    for i in range(n):
        t.pendown()
        t.fd(100)
        t.right(360/n)

t.penup()
for i in range(cnt):
    t.right(360/cnt)
    draw(n)

turtle.mainloop()
