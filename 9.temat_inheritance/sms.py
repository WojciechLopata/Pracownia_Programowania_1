import message
class SMS(message.Message):
    def __init__(self,sender_num,recip_num,message):
        self.sender_num=sender_num
        self.recip_num=recip_num
        super().set_message(message)
    def send(self):
        return "Sending  sms... \n"+"sender number "+self.sender_num+"\nrecipient number "+self.recip_num+self.message
    
test=SMS("3141","533125","eLuwiNa")
print(SMS.send(test))