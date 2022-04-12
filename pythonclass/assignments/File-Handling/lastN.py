#read the last n lines of a file

from turtle import end_fill


file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r")
entire = file.readlines()
entire.reverse()

lastN = int(input("How many lines from the back to you wanna print: "))

"""for i in range(lastN):
    print(entire[i])"""

for n in range(lastN):
    line = file.readline()
    print(line)

file.close()