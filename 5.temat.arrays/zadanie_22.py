def roznica(numbers):
    
    size=len(numbers)
    size=size-1
 
    mini=numbers[size]
    maxi=numbers[size]
    while(size>=0):
        size=size-1
        if(numbers[size]>maxi):maxi=numbers[size]
        if(numbers[size]<mini):mini=numbers[size]
    return maxi-mini
array=[5,1,9,6,1]
print(roznica(array))
#print(max(array)-min(array))