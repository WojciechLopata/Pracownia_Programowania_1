file=open("integers_22.txt","w")
for n in range(1,11):
    first=str(n)
    second=str(n**2)
    third=str(n**3)
    file.write(first+","+second+","+third+"\n")
file.close()