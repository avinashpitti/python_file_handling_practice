with open('data.txt','w') as f :
    f.write('python is a dynamic language')

with open('data.txt','r') as f :
    data = f.read()
    print(data)