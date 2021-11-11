array=[1,2,3,4,5,6,7,8]
odd=[]
even=[]
for i in array:
    if(i%2==0):odd.append(i)
    else: even.append(i)
array=even+odd
print(repr(array).replace(" ",""))