#1
with open('info.txt','w+') as f :
    f.write('Hello Python') 
    print(f.tell())
    print(f.seek(0))
    print(f.read())

#2
with open('info.txt','r') as f :
    print(f.readline(4))
    print(f.seek(0))
    print(f.read())