class Monster:
    WEAK = 0
    NORMAL = 10
    STRONG = 20

    def __init__(self):
        self.__health = Monster.NORMAL # 10

    def print(self):
        print(self.__health)

    def eat(self):
        self.__health = Monster.STRONG # 20
    
    def attack(self):
        self.__health = Monster.WEAK # 0


ms = Monster()
ms.print() # 10
ms.eat()
ms.print() # 20
ms.attack()
ms.print() #0