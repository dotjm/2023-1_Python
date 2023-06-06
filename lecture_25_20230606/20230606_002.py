class Animal:
    def __init__(self, age = 0):
        self.age = age


    def eat(self):
        print("동물이 먹고 있다")


class Dog(Animal):
    def __init__(self, age=0, name=""):
        # super().__init__(age)
        self.name = name

    # 부모 클래스의 생성자가 호출되지 않으면 age 변수가 생성되지 X

    def getName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def printName(self):
        print(self.name)

dog = Dog()
print(dog.age) # 부모클래스의 생성자가 호출되지 않아 없으면 오류 발생
dog.printName()