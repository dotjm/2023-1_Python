import random
import turtle

t = turtle.Turtle()

screen = turtle.Screen()
image1 = "d:\\University\\Develop\\2023-1_Python\\lecture_09_20230404\\500-front.png"
image2 = "d:\\University\\Develop\\2023-1_Python\\lecture_09_20230404\\500-back.png"

screen.addshape(image1)
screen.addshape(image2)


print("동전 던지기 게임 시작")
coin = random.randrange(2)
print(coin)
if coin == 0:
    print("앞면")
    t.shape(image1)
    t.stamp()
else:
    print("뒷면")
    t.shape(image2)
    t.stamp()