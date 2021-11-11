import compra

array_1=["water","book","sky"]
array_2=["water","book","sky"]
print("Array1: ",end="")
for i in array_1:
    print(i,end=" ")
print()
print("Array2: ",end="")
for i in array_2:
    print(i,end=" ")
if(compra.compare(array_1,array_2)):print("they are the same")
else:print("They are different")

array_1=[True,False]
array_2=[True,False,True]
print("Array1: ",end="")
for i in array_1:
    print(i,end=" ")
print()
print("Array2: ",end="")
for i in array_2:
    print(i,end=" ")
print()
if(compra.compare(array_1,array_2)):print("they are the same")
else:print("They are different")

array_1=[5,3,1]
array_2=[5,3,1]
print("Array1: ",end="")
for i in array_1:
    print(i,end=" ")
print()
print("Array2: ",end="")
for i in array_2:
    print(i,end=" ")
print()
if(compra.compare(array_1,array_2)):print("they are the same")
else:print("They are different")

array_1=[3,2,1]
array_2=[3,2]
print("Array1: ",end="")
for i in array_1:
    print(i,end=" ")
print()
print("Array2: ",end="")
for i in array_2:
    print(i,end=" ")
print()
if(compra.compare(array_1,array_2)):print("they are the same")
else:print("They are different")
