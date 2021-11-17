Import bubblesort

def median(array):
    if(len(array)%2==0):return (array[len(array)//2]+array[(len(array)//2)-1])/2
    else: return array[(len(array)//2)]
array=[1,2,3,4]
print(median(bubblesort.bubblesort(array)))
