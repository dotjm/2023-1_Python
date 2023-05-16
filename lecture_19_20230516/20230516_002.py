from random import randint

class Dice:

    def __init__(self, value = 1, size = 30):
        self.__value = value
        self.__size = size
    
    def read_dice(self):
        return self.__value
    
    def print_dice(self):
        print(self.__value)

    def roll_dice(self):
        self.__value = randint(1, 6)


dc = Dice()
dc.roll_dice()
dc.print_dice()