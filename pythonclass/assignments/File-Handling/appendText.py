#append text to an empty file and display the text

text = input("what dp you wish to write: ")

with open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/empty.txt", "w") as f:
    #can use "a" aka append which will not overwrite pre-existing text
    f.write(text)
#use encoding = "utf-8" if you wanna write in like japanese or use emojis and stuff like that

file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/empty.txt", "r")
entire = file.read()
print(entire)
file.close()

#"w" will either open a new file if it doesnt exist or overwrite the existing one
#"x" will create a new file or give an error if one already exists