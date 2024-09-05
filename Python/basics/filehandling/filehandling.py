# f = open('sample.txt','r')
# f.write('Learning C is also Easy\n')

# # to read the file Data
# read = f.read()
# print(read)

# f.close()

f1 = open('mydetails.txt','r')
f1.write('Hi, I am Sai Kumar\n')
f1.writelines('I want to become Python Developer\n')
readData = f1.read()
print(readData)
f1.close()