import json
with open("euro_10.json") as file:
    read=json.load(file)
    print("date      ","sale","  buy")
    print("========================")
    test=False
    for i in read:
        if(test):test=False
        else:print(i["effectiveDate"],i["bid"],i["ask"])
    