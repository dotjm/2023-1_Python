import random
import turtle

t = turtle.Turtle()

screen = turtle.Screen()
# image1 = "d:\\University\\Develop\\2023-1_Python\\lecture_09_20230404\\500-front.gif" # 500원 동전 이미지 뒷면
# image2 = "d:\\University\\Develop\\2023-1_Python\\lecture_09_20230404\\500-back.gif" # 500원 동전 이미지 뒷면
image1 = "d:\\University\\Develop\\2023-1_Python\\lecture_09_20230404\\a.gif" # 교재 이미지 - 동전 앞면 (교수님 제공)
image2 = "d:\\University\\Develop\\2023-1_Python\\lecture_09_20230404\\b.gif"  # 교재 이미지 - 동전 뒷면 (교수님 제공)

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

turtle.mainloop()