import turtle

t = turtle.Turtle()
t.shape("turtle")

# radius = int(input("반지름 입력 : ")) # 일반 문장에서 입력
radius = int(turtle.textinput("반지름 입력창", "반지름 입력 : ")) # 터틀 문장에서 입력
# radius = 100

# t.circle(radius) # 반지름이 100인 원이 그려진다. 
# t.fd(50)
# t.circle(radius) # 반지름이 100인 원이 그려진다. 
# t.fd(50)
# t.circle(radius) # 반지름이 100인 원이 그려진다. 
# # t.fd(50)

# 반복되는 부분을 반복문으로 처리
for i in range(3):
    t.circle(radius) # 반지름이 100인 원이 그려진다. 
    t.fd(50)

# 다른 언어의 경우 아래와 같이 이용하여 브레이스? "{}"가 걸리는데, python은 그렇지 않다. 
# 파이썬은 들여쓰기로 구분한다. 
# for(i=0; i < 3; i++) {
#     t.circle(radius) # 반지름이 100인 원이 그려진다. 
#     t.fd(50)
# }


turtle.mainloop()
turtle.bye()