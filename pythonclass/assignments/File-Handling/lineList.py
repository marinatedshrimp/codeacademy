#read a file line by line and store it into a list

file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r")
lines = file.readlines()

"""
lineList = []
for line in lines:
    lineList.append(line)

print(lineList)
"""

print(lines)
file.close()