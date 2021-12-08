class Tv_Set():
    def __init__(self):
        self.channels_list=[]
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
    def set_channel_no(self,channel_no):
        self.channel_no=channel_no
    def set_channels(self,channels_list):
        for i in channels_list:
            self.channels_list.append(i)
    def show_channels(self):
        i=0
        for channel in self.channels_list:
            i+=1
            print(i,".",channel,sep=" ")
        
test=Tv_Set()
Tv_Set.show_status(test)
Tv_Set.turn_on(test)
Tv_Set.show_status(test)
Tv_Set.set_channels(test,["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"])
Tv_Set.show_channels(test)
Tv_Set.show_status(test)
Tv_Set.turn_off(test)
Tv_Set.show_status(test)


