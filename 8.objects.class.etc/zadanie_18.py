class Konto():
    def __init__(self,adress):
        self.adress=adress
        self.balance=0
    def display(self):
        print("Bank Account No:",self.adress)
        print("Balance : PLN", self.balance)
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(self.balance-amount>=0):
            self.balance-=amount
        else:print("Insufficient funds on the account")
    def send(self,name,amount):
        self.balance-=amount
        name.balance+=amount
test=Konto("12 3456 5555 9090 1111 0000 7722")
test_2=Konto("12 3456 5555 9090 1111 0000 7721")
Konto.display(test)
Konto.deposit(test,25.30)
Konto.display(test)
Konto.withdraw(test,31.70)
Konto.display(test)
Konto.withdraw(test, 14)
Konto.display(test)
Konto.send(test,test_2,5)
Konto.display(test_2)