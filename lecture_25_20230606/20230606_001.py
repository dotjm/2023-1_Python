class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def getDesc(self):
        return "차량 = ("+str(self.make)+","+\
            str(self.model)+","+\
            str(self.color)+","+\
            str(self.price)+")"
    

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterySize = batterySize

    def setBatterySize(self, batterySize):
        self.batterySize = batterySize

    def getBatterySize(self):
        return self.batterySize

    # getDesc는 여기서 작성하지 않아 배터리 관련 정보가 없음
    
def main():
    pass # 여기에 메인 코드를 작성하는 방식도

main()

myCar = ElectricCar("Tesla", "Model S", "white", 10000, 0)
myCar.setBatterySize(100)
print(myCar.getDesc())
print(myCar.getBatterySize())