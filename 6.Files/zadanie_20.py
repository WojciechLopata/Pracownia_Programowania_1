file=open("integers_20.txt","w")
for n in range(1,51):
    n=str(n)
    file.write(n+"\n")
file.close()