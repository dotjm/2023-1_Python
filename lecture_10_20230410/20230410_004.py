import turtle, random
t = turtle.Turtle()
t.shape("turtle")

# for i in range(6):
#     t.circle(100)
#     t.left(360/6)

for i in range(30):
    num = random.randint(1, 100)
    t.fd(num)
    num = random.randint(-180, 180)
    t.left(num)

turtle.mainloop()