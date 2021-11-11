names=["Genowefa", "Onufry","Celestyna", "Alojzy", "Pankracy"]
amount=len(names)
amount=amount-1
max_i=len(names[amount])
longest=names[amount]
while(amount>=0):
    if(max_i<len(names[amount])):
        max_i=len(names[amount])
        longest=nammes[amount]
    amount-=1
print(longest)