import re
with open("grades.txt","r") as file:
    text=file.read()
    grades=re.findall("\d{1}[.]\d{1}",text)
    suma=0
    licz=0
    for grade in grades:
        grade=float(grade)
        suma=suma+grade
        licz+=1
file.close()
print(suma/licz)
    