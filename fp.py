import csv

with open('employees.csv','w',newline='') as f :
    writing=csv.writer(f)

    writing.writerow(['id','name','salary'])
    writing.writerow([1,'Amit',50000])
    writing.writerow([2,'Neha',60000])
    writing.writerow([3,'srinivas',90000])

with open('employees.csv','r') as f :
    print(f.read())
