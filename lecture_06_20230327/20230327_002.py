import turtle

# 1번 입력 -> 삼각형 그리기
# 2번 입력 -> 사각형 그리기
# 3번 입력 -> 원 그리기

t = turtle.Turtle()
t.shape("turtle") # arrow, circle 다됨

while True:
    mode = int(input("모드 입력 : "))
    t.clear()

    if mode == 1:
        print(str(mode)+"번을 선택했군요. ")
        for i in range(3): # 삼각형 그리는 반복문
            t.fd(100)
            t.left(120)
    elif mode == 2:
        print(str(mode)+"번을 선택했군요. ")
        for i in range(4): # 사각형 그리는 반복문 
            t.fd(100)
            t.left(90)
    elif mode == 3:
        print(str(mode)+"번을 선택했군요. ")
        t.circle(50) # 원 그리는 함수
    else:
        print("종료합니다. ")
        break

# for i in range(4): # 사각형 그리는 반복문 
#     t.fd(100)
#     t.left(90)
# t.fd(100)
# t.right(90)
# t.fd(100)
# t.right(90)
# t.fd(100)
# t.right(90)
# t.fd(100)
# t.right(90)

# 펜들고 이동
# t.penup()
# t.fd(150)
# t.pendown() 

# for i in range(3): # 삼각형 그리는 반복문
#     t.fd(100)
#     t.left(120)

# 펜들고 이동
# t.penup()
# t.fd(150)
# t.pendown()

# t.circle(50) # 원 그리는 함수



turtle.mainloop()