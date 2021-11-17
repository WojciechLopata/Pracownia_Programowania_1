name=input("What's the file name? ")
file=open(name,"r")
count=0
for line in file:
    count+=1
print("File name:",name)
print("number of lines:",count)