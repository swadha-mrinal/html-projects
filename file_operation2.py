file_read = open('codingal.txt','r')
print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open('codingal.txt','w')
file_write.write("File in write mode ....")
file_write.write("Hi i am swadha.I am 10 yr. old")
file_write.close()

file_append = open('codingal.txt','a')
file_append.write("\n File in append mode....")

file_append.write("Hi! i am ritisha. I am 11 yr.old")
file_append.close()