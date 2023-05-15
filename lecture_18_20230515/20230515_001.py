class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def print_obj(self):
        print(self.speed, self.color, self.model)

    def drive(self):
        self.speed = 60


myCar = Car(0, "blue", "E-class")

print("자동차 객체 생성")
myCar.print_obj()

myCar.drive()
myCar.print_obj()
print(myCar.speed)
print(myCar.color)
print(myCar.model)


# 과제
# 객체를 만들어보자
# class 작성 후
# class 내부에서 사용될 함수 정의
# 이때 정의는 private과 public 변수 모두 사용
