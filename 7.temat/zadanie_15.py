import json
student={
    "Name":"Marek",
    "surname":"Kowak",
    "year of birth":"2002",
    "recrutation points":123,
    "average of grades":4.3,
    "Erasmus": False,
    "exam results": None
    }
file=open("student.json","w")
json.dump(student,file,indent=4)
file.close()
    
    
    