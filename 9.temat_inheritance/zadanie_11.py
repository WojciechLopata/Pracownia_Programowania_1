class student():
    album=100000
    def __init__(self,name,surname,field_of_study):
        self.name=name
        self.surname=surname
        self.field_of_study=field_of_study
        student.album+=1
        self.album=student.album
        self.univ="Uek Krakow"
        self.__name__=student.album
    def __str__(self):
        text=(self.name+" "+self.surname+" "+self.field_of_study+" "+str(self.album)+" "+self.univ)
        return text

student_1=student("marek","Nowak","Informatics")
student_2=student("Jan","Kowalski","Math")
student_3=student("Charlie","May","Economics")

print(student_1)
print(student_2)
print(student_3)