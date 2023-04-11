import turtle

t = turtle.Turtle()
t.shape("turtle")

i = 0
while i < 4:
    t.fd(100)
    t.right(90)
    i = i + 1

turtle.mainloop()