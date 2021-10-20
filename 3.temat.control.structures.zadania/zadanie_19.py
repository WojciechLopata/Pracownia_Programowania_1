dogs_age=int(input("Enter the dog's age in human years: "))
x=0
if dogs_age<=2: x=dogs_age*10,5
else :
    dogs_age=dogs_age-2
    x=dogs_age*4+21

print(f"the dogs age in dog's years is {x} years")