# 직접 만든 n각형 코드, 교수님 코드는 4번 참고
import turtle
t = turtle.Turtle()
t.shape('turtle')

def n_polygon(n, size):
    t.pendown()
    for i in range(n):
        t.fd(size)
        t.right(360/n)
    t.penup()

t.penup()
t.fd(-300)
t.left(90)
t.fd(-200)
t.right(90)
for i in range(10):
    n_polygon(i, 20)
    t.fd(45)

t.fd(-300)
t.right(90)
t.fd(100)
t.left(90)

n = int(input("몇 각형 : "))
n_polygon(n, 30)

turtle.mainloop()

