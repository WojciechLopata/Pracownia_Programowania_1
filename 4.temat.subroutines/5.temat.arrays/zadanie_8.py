numbers=[-15,8,-31,47,-2,19]
size=len(numbers)
size=size-1
a=min(numbers)
b=max(numbers)
#min i maxi robia to samo co ta petla poniżej 
mini=numbers[size]
maxi=numbers[size]
while(size>=0):
    size=size-1
    if(numbers[size]>maxi):maxi=numbers[size]
    if(numbers[size]<mini):mini=numbers[size]
print("min to",mini)
print("max to",maxi)