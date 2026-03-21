file_read = open('codingal.txt','r')
print("File in read mode...")
print(file_read.read())
file_read.close()

file_write = open('codingal.txt','w')
file_write.write("File in write mode...")
file_write.write("Hi! i am penguin-A i am 1 yr old")
file_write.close()

file_append = open('codingal.txt','a')
file_append.write("\n File in append mode...")
file_append.write("Hi! i am penguin-B .I am 2 yr old")
file_append.close()