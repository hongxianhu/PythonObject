class DimmerSwitch:
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiselevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerlevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print("Switch is On?", self.switchIsOn)
        print("Brightness is:", self.brightness)
