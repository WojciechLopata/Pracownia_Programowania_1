import message
class Mail(message.Message):
    def __init__(subject,sender,recipient):
        self.subject=subject
        self.sender=sender
        self.recipient=recipient
    