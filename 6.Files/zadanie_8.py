file=open("countries.txt","r")
line_count=1
for line in file:
    print(line_count,".) ",line,sep="",end="")
    line_count+=1
file.close()