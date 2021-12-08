class Tv_Set():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if(self.is_on):
            print("Tv is on, channel",self.channel_no)
        else: print("Tv is off")
    def set_channel(self,channel_no):
        self.channel_no=channel_no
test=Tv_Set()
Tv_Set.show_status(test)
Tv_Set.turn_on(test)
Tv_Set.show_status(test)
Tv_Set.set_channel(test,5)
Tv_Set.show_status(test)
Tv_Set.turn_off(test)
Tv_Set.show_status(test)

