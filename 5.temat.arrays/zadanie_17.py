array_1=[4,36,12,28,9,44,5]
array_2=[5,1,36]
for a in array_1:
    test=True
    for b in array_2:
        if(a==b):test=False
    if(test):print(a,end=" ")
    