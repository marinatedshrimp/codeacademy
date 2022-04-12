#read the first n lines of a file

file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r")
lineNum = int(input("How many lines do you want to read: "))

for n in range(lineNum):
    line = file.readline()
    print(line)


file.close()