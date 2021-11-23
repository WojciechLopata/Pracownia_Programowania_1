import re
with open("Lorem.txt",'r') as file:
        b=file.read()
        a=re.findall("\w{6,}",b)
print(a)
file.close()

    