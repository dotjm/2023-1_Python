import turtle

t = turtle.Turtle()
t.shape('turtle')

lists = [[0, 0, "blue"], [-120, 0, "purple"], [60, 60, "red"], [-60, 60, "yellow"], [-180, 60, "green"]]
for x, y, color in lists:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color, color)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()


turtle.mainloop()