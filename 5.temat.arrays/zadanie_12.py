array=[15, 8, 31, 47, 2, 19]
reverse_array=[]
print("existed array",end=" ")
size=len(array)
size=size-1
i=0
while(size>=i):
    print(array[i],end=" ")
    i=i+1
print()
size=len(array)
size=size-1
print("reversed",end="")
while(size>=0):
    reverse_array.append(array[size])
    print(array[size],end=" ")
    size=size-1