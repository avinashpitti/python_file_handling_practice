with open('data.txt','r') as f :
    for line in f :
        print(line.strip())

with open('data.txt','a') as f :
    f.write('This is line 4')
    f.write('This is line 5')

with open('data.txt','a') as f :
    f.write('\nfunctions')
    f.write('\nvariables')
    f.write('\n objects\n')

with open('data.txt','a') as f :
    f.write('python\nmysql\nfastapi\n')