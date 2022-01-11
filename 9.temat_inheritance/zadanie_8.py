class phone():
    def __init__(self,maker,year_of_prod,model,ram,storage,owner):
            self.maker=maker
            self.year_of_prod=year_of_prod
            self.model=model
            self.ram=ram
            self.storage=storage
            self.owner=owner
            self.status=False
        
    def turn_on(self):
        self.status=True
    def turn_off(self):
        self.status=False
    def change_storage(self,storage):
        self.storage=storage
    def display(self):
        print(self.maker,
            self.year_of_prod,
            self.model,
            self.ram,
            self.storage,
            self.owner,
            self.status)
phone_1=phone("apple",2012,"iphone 14","4gb","128gb","Marek")
phone_2=phone("xiaomi",2016,"redmi  14","8gb","64gb","Simon")
phone_1.turn_on()
phone_2.turn_on()
phone_1.display()
phone_2.display()
phone_2.turn_off()
phone_2.display()
phone_1.change_storage("512gb")
phone_1.display()
        