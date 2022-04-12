'''
for i in range(5):
    if i == 1:
        continue
    else:
        print(" "*(i),"* "*(5-i))
        print()
'''


'''
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for space in range(rows - i):
        print(end = " ")
    for star in range(rows, 0, -1):
        print(end = "* ")
    print()
'''

rows = int(input("Gimme the number of rows: "))


for i in range(rows, 0, -1):

    for space in range(rows - i):
        print("  ", end = "") #print spaces on the same line using end
    
    for star in range(2 * i - 1):
        print("* ", end = "") #print stars on ethe same line using end

    print() #printing empty line to skip a line