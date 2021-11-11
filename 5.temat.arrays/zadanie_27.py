def array2str(array):
    together=""
    for digit in array:
        together+=str(digit)
        together+=","
    return together
array=[5,4,3,2,6,5]
print("Array:",repr(array).replace(" ",""))
print("String:",array2str(array))