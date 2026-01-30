with open('data.txt','w') as f :
    f.write('python is a dynamic language')

with open('data.txt','r') as f :
    data = f.read()
    print(data)

with open('info.txt','w+') as f :
    f.write('I learnt javascript basics today')
    f.seek(0)
    data=f.read()
    print(data)

with open('info.txt','a+') as f :
    f.write('52 weeks in a year')
    f.seek(0)
    data=f.read()
    print(data)

with open('info.txt','a+') as f :
    f.write('\nreact is the best javascript framework as of now')
    f.seek(0)
    print(f.read())

