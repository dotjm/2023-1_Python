import turtle

t = turtle.Turtle()
t.shape("turtle")

n = int(input("입력 : "))

for i in range(n):
    t.fd(100)
    t.left(360/n)
s = turtle.textinput("", "당신의 이름은?")
t.write(s + "씨 안녕하세요!")

turtle.mainloop()