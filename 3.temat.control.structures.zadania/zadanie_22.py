for i in range(1,31):
    b=1
    if(i%3==0):
      
        if(i%5==0):
            print("BINGO")
            b=0
        else:print("THREE")
    if(i%5==0 and b==1):
        print("FIVE")
        b=0
    elif(b==1): print(i) 