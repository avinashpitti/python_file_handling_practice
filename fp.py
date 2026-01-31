import csv

with open('students.csv','r') as f :
    reader=csv.reader(f)
    for row in reader:
        print(row)

with open('students.csv','r')as f:
    reader=csv.reader(f)
    next(reader) # skip header
    for row in reader :
        print(row)


with open('students.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
