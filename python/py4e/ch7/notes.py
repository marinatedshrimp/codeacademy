"""handle = open("mbox.txt", "r")"""
#r = read
"""print(handle)"""
#this doesn't open the file but shows info on the file

stuff = "Hello\nWorld!"
print(stuff)
#\n stands for newline and it is one character
#that means the Enter key
mummy = "X\nY"
print(mummy)
print(len(mummy))
#its 3 characters not 2 or 4

#xfile is a file handle
#for statement iterates through all the lines in xfile
xfile = open("mbox.txt")
for cheese in xfile:
    print(cheese)

"""modes: X = create file,return error if preexisting"""

self.assert_(boolean expression, 'message')
f = open("mybox.txt","x")

fhand = open("mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print("Line Count:", count)



fhand = open("mbox.txt")
for line in fhand:
    if line startswith("From:"):
        print(line)
"""theres a blank line between every result cuz the file already
has \n and print functions automatically add a \n"""

fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if line startswith("From:"):
        print(line)
"""use smth.rstrip() to rid of the \n
\n is an invisible function? so it counts as a whitespace"""

 fhand = open("mbox.txt")
 for line in fhand:
     line = line.rstrip()
if not line.startswith("From:"):
    continue
    #continue makes you finish the current iteration
print(line)

fname = input("Enter file name bitch:   ")
fhand = open(fname)
count = 0
for line in fhand:
    if line startswith("Subject:"):
        count = count+1
print('There were', count, 'subject lines in', fname)
#Enter the fi;e name: mbox.txt
#There were 789798900098 subject lines in mbox.txt

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line startswith("Subject:"):
        count = count+1
print('There were', count, 'subject lines in', fname)
#Enter the file name: nanananaan
#File cannot be opened nanannana
