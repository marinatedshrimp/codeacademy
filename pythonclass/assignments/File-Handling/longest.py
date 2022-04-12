#find the longest words

file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r")
entire = file.read()
words = entire.split()
longest = ""

for word in words:
    if  len(word) > len(longest):
        longest = word
    else:
        continue

print("The longest word is:", longest)
file.close()