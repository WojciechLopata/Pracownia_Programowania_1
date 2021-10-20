
amount=int(input("Enter the amount in pln: "))
x=amount
fiv=x/5
fiv=int(fiv)
x=x%5
two=x/2
two=int(two)
x=x%2
print(f"the amount of {amount} in coins is:\n 5 zł-{fiv} \n 2zł-{two} \n 1 zł-{x}")