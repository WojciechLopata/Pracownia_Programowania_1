file=open("Lorem_Ipsum.txt","r")
count=0
for line in file:
    print(line,end="")
    count+=1
    if(count%5==0):input()