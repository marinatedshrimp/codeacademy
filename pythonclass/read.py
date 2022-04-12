var = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/read.txt", "r")
content = var.read()
#read(10) will read the first 10 characters
print(content)

var.close()