file1 = open('codingal.txt','r')
file2 = open('codingal_updated.txt','w')

for line in file1.readlines():

    if not (line.startswith('coding')):
        print(line)


        file2.write(line)

file2.close()
file1.close()