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
array=[5,1,9,6,1,12]
array=bubblesort(array)
print(array[-2])
