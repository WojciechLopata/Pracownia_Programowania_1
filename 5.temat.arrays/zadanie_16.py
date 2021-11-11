integers=[12,6,4,9,10]
def star(n):
    return "*"*n
naj=max(integers)
naj=str(naj)
naj=len(naj)
for i in integers :
    liczba=str(i)
    teraz=len(liczba)
    print((naj-teraz)*" ",end="")
    print(f"{i}: ",end="")
    print(star(i))
    
    