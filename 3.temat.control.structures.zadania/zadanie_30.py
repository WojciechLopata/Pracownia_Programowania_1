n=int(input("Wpisz ile liczb pierwszych chcesz wyliczyć: "))
licz=1
while(n>0):
    dziel=1
    n=n-1
    while(dziel!=0):
        dziel=0
        pom=2
        licz=licz+1
        while(pom<=licz):
                if(licz%pom==0):dziel=dziel+1
                pom=pom+1
        if(dziel==1):
            print(licz)
            dziel=0
                
        
        