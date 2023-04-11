# Python has function for creating, reading, updating, and deleting files 

# open a file 
myFile = open('myfile.txt','w')

# get some info
print('name', myFile.name)
print('Is cloased', myFile.closed)
print('Opening Mode', myFile.mode)


# Write to file 
myFile.write('I love python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file 
myFile = open('myfile.txt','a')
myFile.write('I also like php')


# Read from file 
myFile = open('myfile.txt','r+')
text = myFile.read(100)
print(text)