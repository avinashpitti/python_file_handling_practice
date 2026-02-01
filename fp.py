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
    