import json

with open('users.json','r') as f:
    data=json.load(f)

print(data)
print(type(data))

print(data["name"])
print(data['age'])
print(data['skills'][2])