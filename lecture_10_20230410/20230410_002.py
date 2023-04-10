import turtle

t = turtle.Turtle()
t.shape("turtle")

shape = turtle.textinput("도형 입력", "도형을 입력하세요")
if shape == "사각형":
    w = int(turtle.textinput("사이즈 입력", "가로 입력 : "))
    h = int(turtle.textinput("사이즈 입력", "세로 입력 : "))

    # t.fd(w)
    # t.left(90)
    # t.fd(h)
    # t.left(90)
    # t.fd(w)
    # t.left(90)
    # t.fd(h)
    # t.left(90)
    for i in range(2):
        t.fd(w)
        t.left(90)
        t.fd(h)
        t.left(90)
elif shape == "삼각형":
    size = turtle.textinput("사이즈 입력", "한변 길이 입력 : ")
    size = int(size)
    
    for i in range(3):
        t.fd(size)
        t.left(120)
elif shape == "원":
    rad = int(turtle.textinput("사이즈 입력", "반지름 입력 : "))

    t.circle(rad)

turtle.mainloop()