import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
mean=0
for number in temperatures:
    number=int(number)
    mean=mean+number
mean=mean/len(temperatures)
print(mean)
