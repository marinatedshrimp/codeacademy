#read an entire text file
"""
with open ("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r") as file
"""

file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r")
entire = file.read()
print(entire)
file.close()