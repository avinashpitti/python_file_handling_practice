import json

with open('users.json','r') as f:
    data=json.load(f)

print(data)
print(type(data))