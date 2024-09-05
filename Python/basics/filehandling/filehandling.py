# Ex:1
f = open('sample.txt','r')
f.write('Learning C is also Easy\n')

# to read the file Data
read = f.read()
print(read)

f.close()

# Ex:2
f1 = open('mydetails.txt','r')
f1.write('Hi, I am Sai Kumar\n')
f1.writelines('I want to become Python Developer\n')
readData = f1.read()
print(readData)
f1.close()

# Ex:3
with open('mydetails.txt','r') as file:
    file.write('This is with example in file handling')
    readWith = file.read()
print(readWith)