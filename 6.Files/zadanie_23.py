import csv
with open('Students.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    test=True
    for row in spamreader:
        if(test):test=False
        else: print(row[0],"\t",row[1],"\t",row[4])