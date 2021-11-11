def compare(array_1,array_2):
    size_1=len(array_1)
    size_2=len(array_2)
    
    if(size_1!=size_2):return False
    size_1-=1
    for i in range(0,len(array_1)):
        if(array_1[i]!=array_2[i]): return False
    return True