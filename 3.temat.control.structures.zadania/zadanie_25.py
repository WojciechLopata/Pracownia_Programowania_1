a=int(input("Szerokosc: "))
b=int(input("Wysokosc: "))
for i in range(a):
    print("*",end="")
print("")
for i in range(b-2):
    print("*",end="")
    for n in range(a-2):
        print(end=" ")
    print("*")
for i in range(a):
    print("*",end="")