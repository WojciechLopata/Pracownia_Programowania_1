import contact
class Contact_List():
    def __init__(self):
        self.list=[]
    def add_cont(self,contact_1):
        self.list.append(contact_1)
    def display(self):
        for contact in self.list:
            print(vars(contact))
        