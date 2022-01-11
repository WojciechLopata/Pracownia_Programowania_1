class Message():
    def __init__(self):
        self.message_text = ''
    def set_message(self,message):
        is_first=True
        message_1=""
        for letter in message:
            if(is_first):
                message_1+=letter.upper()
                is_first=False
            else:message_1+=letter.lower()
        message_1+=" BYE"
        return message_1