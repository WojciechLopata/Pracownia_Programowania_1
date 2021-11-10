def compare(array_1,array_2):
    size_1=len(array_1)
    size_2=len(array_2)
    
    if(size_1!=size_2):return False
    size_1-=1
    for i in range(0,len(array_1)):
        if(array_1[i]!=array_2[i]): return False
    return True
array_1=["water","book","sky"]
array_2=["water","book","sky"]
for i in array_1:
    print(i)
for i in array_2:
    print(i)

         
print(compare(["water","book","sky"],["water","book","sky"]))
print(compare([True,False],[True,False,True]))
print(compare([5,3,1],[5,3,1]))
print(compare([3,2,1],[3,2]))