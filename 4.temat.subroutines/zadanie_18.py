def dig_sum(n):
    pom=n
    wiel=0
    suma=0
    while(pom>0):
        pom=pom//10
        wiel=wiel+1
    while(n>0):
        wiel=wiel-1
        suma=suma+(n//10**wiel)
        n=n%(10**wiel)
    return(suma)