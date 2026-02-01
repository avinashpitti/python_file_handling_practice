from _csv import reader
import csv
from _csv import writer
import csv

data=[
    {'id':1,'name':'Rahul','age':22},
    {'id':2,'name':'Asha','age':24},
    {'id':3,'name':'Mahesh','age':23}
]

with open('students.csv','w',newline='') as f :
    fieldnames=['id','name','age']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open('students.csv','r') as f :
    print(f.read())

with open('students.csv','a',newline='') as f :
    writer=csv.writer(f)
    writer.writerow([4,'Meena',20])

with open('students.csv','r') as f :
    print(f.read())

with open('students.csv','r') as f :
    reader=csv.DictReader(f)
    for row in reader:
        if int(row['age'])>21:
            print(row['name'],row['age'])


    
    