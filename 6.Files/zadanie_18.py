file=open("Films.txt","r")
copy=open("Copylines.txt","w")
for line in file:
    copy.write(line)
file.close()
copy.close()