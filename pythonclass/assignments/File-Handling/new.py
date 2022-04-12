def all():
    file = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/File-Handling/passage.txt", "r")
    line = file.readlines()
    for l in range(len(line)):
        print(line[l])
    file.close()

all()