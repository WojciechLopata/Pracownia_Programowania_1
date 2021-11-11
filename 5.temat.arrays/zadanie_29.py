array_1=[1,2,3,4]
array_2=[1,3,4,2]
subset=True
if(len(array_1)<len(array_2)): print("The second one is not a subset")
else:
    for number_2 in array_2:
        test=False
        for number_1 in array_1:
            if(number_2==number_1):test=True
        if(test):subset=True
        else:
            subset=False
            break
if(subset):print("The second one is a subset")
else: print("The second one is not a subset")

        
        