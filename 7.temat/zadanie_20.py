import json
with open("student_mock.json") as file:
    #num_lines = sum(1 for line in open('student_mock.json'))
    slow=file.read()
    data_i=[]
    write=open("mock_dump.json","w")
    for line in range(1000):
        slow_data=json.loads(slow)[line]
        data={}
        data.update({"first_name":slow_data["first_name"]})
        data.update({"last_name":slow_data["last_name"]})
        data.update({"email":slow_data["email"]})
        print(data)
        data_i.append(data)
        
    json.dump(data_i,write,indent=2)
    write.close()
    
    
        
    
        
    