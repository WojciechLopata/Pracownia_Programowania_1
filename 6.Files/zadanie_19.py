file_1=open("MeatAndFish.txt","r")
file_2=open("GrainsAndBread.txt","r")
file_3=open("ShoppingList.txt","w")
for line in file_1:
    file_3.write(line)
for line in file_2:
    file_3.write(line)
file_1.close()
file_2.close()
file_3.close()
