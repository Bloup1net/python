with open('test.log', mode='w', encoding='utf-8') as a_file :
    a_file.write('test succeded')
with open('test.log', encoding='utf-8') as a_file :
    print (a_file.read())
with open('test.log', mode='a', encoding='utf-8') as a_file :
    a_file.write('and again')
with open('test.log', encoding='utf-8') as a_file :
    print (a_file.read())
