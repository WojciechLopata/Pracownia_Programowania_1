quantity=0
number=1
sum_1=0
while(number!=0):
    number=int(input("Enter number: "))
    if(number==0):break
    sum_1=sum_1+number
    n=number
    quantity=quantity+1
    mean=sum_1/quantity
if(quantity==0): print("you didn't put in any meaningfull numbers")
else:
    print(f"RESULT: Quantity={quantity}, Sum={sum_1}, mean=",end="")
    print(round(mean,2))