import random
file=open("random_ints.txt","w")
for n in range(0,50):
    n=str(random.randint(100,999))
    file.write(n+"\n")
file.close()