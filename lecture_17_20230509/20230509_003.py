class Circle:
    def __init__(self, rad=0):
        self.rad = rad
    
    def getArea(self):
        return 3.14*self.rad*self.rad # pi math... math.pi

    def getPrimeter(self):
        return 2*3.14*self.rad
    

c = Circle(10)
print("원 면적 :", c.getArea())
print("원 둘레 :", c.getPrimeter())