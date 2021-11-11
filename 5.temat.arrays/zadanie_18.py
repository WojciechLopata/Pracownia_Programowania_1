def bubblesort(array):
    size=len(array)
    size=size-1
    a=size
    
    while(a>0):
        i=0
        while(a>i):
            if(array[i]>array[i+1]):
                pom=array[i]
                array[i]=array[i+1]
                array[i+1]=pom
            i=i+1
        a=a-1
    return array
array=[4,2,5,1,7]
print(bubblesort(array))
array=[331,531,64,-21]
print(bubblesort(array))
array=[321839821,3123191341,31231,2,6543,31]
print(bubblesort(array))
