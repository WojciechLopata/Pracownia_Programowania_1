import bubblesort
class Numbers():
    def __init__(self):
        self.array=[]
    
    def add(self,number):
        self.array.append(number)
    def display(self):
        for i in self.array:
            print(i,end=" ")
        print()
    def  maxi(self):
        a=bubblesort.bubblesort(self.array)
        print(a[-1])
    def  mini(self):
        a=bubblesort.bubblesort(self.array)
        print(a[0])
    def mean(self):
        sum=0
        for i in self.array:
            sum+=i
        print(sum/len(self.array))
    def median(self):
        a=bubblesort.bubblesort(self.array)
        if(len(a)%2==0):print(a[len(a)//2])
        else: print(a[len(a)//2]+a[len(a)//2+1])
    def display(self):
        Numbers.mini(self)
        Numbers.maxi(self)
        Numbers.mean(self)
        Numbers.median(self)


test=Numbers()
Numbers.add(test,3)
Numbers.add(test,2)
Numbers.add(test,7)
Numbers.add(test,5)
Numbers.display(test)