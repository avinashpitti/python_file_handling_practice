import json

with open('users.json','r') as f:
    data=json.load(f)

print(data)
print(type(data))

print(data["name"])
print(data['age'])
print(data['skills'][2])

#student.json

data={
    'name':'Rahul',
    'age':29,
    'city':'wayanad'
}

with open('student.json','w')as f :
    json.dump(data,f)


# students.json

info=[
    {'name':'Avinash','age':21,'loc':'hyderabad'},
    {'name':'Srinivas','age':29,'loc':'nalgonda'},
    {'name':'Amar','age':27,'loc':'Guntur'}
]

with open('students.json','w') as f :
    json.dump(data,f)

