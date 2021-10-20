for i in range (7):
    for n in range (7):
        n=1+n*7+i
        if(n<10): print("",n,end=" ")
        #if(n==8 or n==9) print(" ",n,end=" ")
        else:print (n,end=" ")
    print()