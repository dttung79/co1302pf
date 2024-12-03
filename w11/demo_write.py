f = open('authors.txt', 'r')
authors = f.readlines()
print(f'{"Author":20}{"Email":20}')
for author in authors:
    if '@gmail' in author:
        name = author.split(' <')[0]
        email = author.split('<')[1].split('>')[0]
        print(f'{name:20}{email:20}')

f.close()