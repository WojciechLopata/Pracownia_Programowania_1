def sum(array):
    suma=0
    for digit in array:
        suma+=digit
    return suma

def array2str(array):
    together=""
    for digit in array:
        together+=str(digit)
        together+=" "
    return together

array=[4,3,7,1,3]
print("Array:",array2str(array))
print("sum of values",sum(array))
