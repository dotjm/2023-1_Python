class TV:
    serialNumber = 0 # 클래스 변수

    def __init__(self, channel, volume, on) -> None:
        self.channel = channel
        self.volume = volume
        self.on = on

        TV.serialNumber += 1
        self.serialNumber = TV.serialNumber

    def show(self):
        print("Channel : ", self.channel, "Volume : ", self.volume, "On : ", self.on, "serialNumber : ", self.serialNumber, "classSerialNumber : ", TV.serialNumber)


def setSilentMode(t):
    t.volume = 2

myTV = TV(2, 15, True)
myTV2 = TV(2, 15, True)
myTV.show()

setSilentMode(myTV)
myTV.show()

myTV2.show()