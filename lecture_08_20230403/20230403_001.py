import turtle

t = turtle.Turtle()
t.shape('turtle')

color_list = ["blue", "red", "green", "yellow", "purple"]

# t.fillcolor(color_list[0])
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.penup()
# t.fd(200)
# t.pendown()

# t.fillcolor(color_list[1])
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# 여기부턴 새로 추가한 코드
def back(): # 함수... 클래스를 만들어서 함수를 활용하는 것은 => 매서드
    t.penup()
    t.fd(-200)
    t.pendown()

def forward():
    t.penup()
    t.fd(100)
    t.pendown()

back()
# 이전시간 코드(005)에서 이어서 만든 반복문
for color in color_list:
    t.fillcolor(color)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # t.penup()
    # t.fd(100)
    # t.pendown()
    forward()

turtle.mainloop()