def minmax(numbers):
    
    size=len(numbers)
    size=size-1
 
    mini=numbers[size]
    maxi=numbers[size]
    while(size>=0):
        size=size-1
        if(numbers[size]>maxi):maxi=numbers[size]
        if(numbers[size]<mini):mini=numbers[size]
    array_1=[]
    array_1.append(mini)
    array_1.append(maxi)
    return array_1
array=[4,2,8,4,7,9,5]
a=minmax(array)
print(str(a).replace(" ",""))