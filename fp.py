with open('info.txt','w+') as f :
    data=f.write("I am living in a chaotic country India")
    f.seek(0)
    data=f.read()
    print(data)