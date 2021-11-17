file=open("Shopping.txt","a")
new_product=input("What do you want to buy? ")
file.write(new_product+"\n")
file.close()