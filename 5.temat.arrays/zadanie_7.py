integers=[1,2,3,4,5,6,7,9,11,13,0]
odd=0
even=0
size=len(integers)
size=size-1
while(size>=0):
    if(integers[size]%2==0):even=even+1
    else: odd+=1
    size-=1
print(f"there are {even} even numbers")
print(f"there are {odd} odd numbers")