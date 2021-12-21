import random
class Termometr():
    def __init__(self):
        self.is_on=False
    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False
    def measure(self):
        self.temp=random.randint(340,420)/10
    def display(self):
        if(self.turn_on):
            print("temperature:",self.temp,end=" ")
            if(self.temp>=37):
                print("(fever)",end=" ")
            if(self.temp>=41):
                print("(CRITICAL TEMPERATURE!!)",end="")
            print()
pacjent=Termometr()
Termometr.turn_on(pacjent)
Termometr.measure(pacjent)
Termometr.display(pacjent)
Termometr.turn_off(pacjent)
