class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)
    
    def setChannel(self, channel):
        self.channel = channel
    
    def getChannel(self):
        return self.channel
    
    def setVolume(self, volume):
        self.volume = volume
    
    def getVolume(self):
        return self.volume
    

tv = Television(11, 5, True)
tv.show()

tv.setChannel(100)
tv.show()

tv.setVolume(50)
tv.show()