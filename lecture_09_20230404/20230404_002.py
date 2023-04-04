import turtle

def draw():
    t.penup()

    t.goto(105, 100)
    t.write("거북이가 여기로 오면 양수입니다")

    t.goto(105, 0)
    t.write("거북이가 여기로 오면 0입니다")

    t.goto(105, -100)
    t.write("거북이가 여기로 오면 음수입니다")

def pics():
    draw()

    t.goto(-200, 0)
    t.pendown()

t = turtle.Turtle()
t.shape("turtle")

pics()

sel = int(input("입력"))



if sel > 0:
    t.goto(100, 100)
elif sel == 0:
    t.goto(100, 0)
elif sel < 0:
    t.goto(100, -100)

turtle.mainloop()