class Tv_Set():
    def __init__(self):
        self.channels_list=[]
        self.is_on=False
        self.channel_no=1
        self.volume=0
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if(self.is_on):
            if(self.channel_no<len(self.channels_list)):
                print("Tv is on, channel",self.channel_no,self.channels_list[self.channel_no-1],"volume",self.volume)
            else:print("Tv is on, channel",self.channel_no,"volume",self.volume)
                
            
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
    def inc_vol(self):
        if(self.volume<10):
            self.volume+=1
    def dec_vol(self):
        if(self.volume>0):
            self.volume-=1
        
test=Tv_Set()
Tv_Set.show_status(test)
Tv_Set.turn_on(test)
Tv_Set.show_status(test)
Tv_Set.set_channels(test,["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery","Kanał sportowy","TVP Kultura","Disney XD"])
Tv_Set.show_status(test)
for i in range(1,11):
    Tv_Set.set_channel_no(test,i)
    Tv_Set.show_status(test)
Tv_Set.inc_vol(test)
Tv_Set.inc_vol(test)
Tv_Set.inc_vol(test)
Tv_Set.dec_vol(test)
Tv_Set.set_channel_no(test,4)
Tv_Set.show_status(test)
Tv_Set.turn_off(test)
Tv_Set.show_status(test)
