array=[2,3,2,5,8,1,9,8]

for a in range(0,len(array)):
    test=True
    licz=0
    for b in range(0,len(array)):
        if(array[a]==array[b]):
            licz=licz+1
            if(licz>1):test=False
    if(test):print(array[a],end=" ")
    