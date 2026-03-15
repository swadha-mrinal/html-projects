file = open('codingal.txt','r')
counter = 0

content = file.read()

Colist = content.split('\n')

for i in Colist:
    if i:
        counter +=1
print("this is the number of lines in the file")
print(counter)