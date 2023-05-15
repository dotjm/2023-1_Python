# 002 수정

class Car:
    def __init__(self, speed=0, color=None, model=None):
        self.__speed = speed
        self.__color = color
        self.__model = model

    def print_obj(self):
        print(self.__speed, self.__color, self.__model)

    def drive(self):
        self.__speed = 60
        print(self.__speed)

    def getSpeed(self): # 접근자 (getter) - private에서 필요
        return self.__speed()
    
    def setSpeed(self, speed): # 설정자 (setter) - private에서 필요
        self.__speed = speed

    def getModel(self):
        return self.__model
    
    def setModel(self, model):
        self.__model = model


# myCar = Car(0, "blue", "E-class")
myCar = Car()

print("자동차 객체 생성")

myCar.print_obj()

myCar.drive()
myCar.print_obj()