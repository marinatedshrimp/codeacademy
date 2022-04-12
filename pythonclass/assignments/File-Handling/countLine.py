#count the number of lines in a text file. 
#(Hint: Look up and use “enumerate” in for loop instead of “range”)

file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r")
eachLine = file.readlines()

for count, lines in enumerate(eachLine):
#not possible with enumerate(file) because it cannot read an entire file 
    pass 

print("There are ", count + 1, "lines")

file.close()