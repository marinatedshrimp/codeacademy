"""print out the contents of word.txt
in uppercase and with no blank lines"""

fname = input("Enter file name:")
try:
    fh = open(fname)
except:
    print("Fuck you")
    quit()

for boobs in fh:
    boobs = boobs.upper()
    boobs = boobs.rstrip()
    print(boobs)

#I kept doing for boobs in fname
#I forgot to write boobs = before the stuff
