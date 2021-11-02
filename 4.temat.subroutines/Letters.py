def letters(x,y):
    x=x.lower()
    y=y.lower()
    n=0
    for i in range(len(x)):
        if(x[i]==y):n=n+1
    return n

