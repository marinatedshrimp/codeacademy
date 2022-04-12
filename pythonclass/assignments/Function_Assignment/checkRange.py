#check whether a number falls in a given range.

myNum = 89

def checkRange(Lnum, Tnum):
    if (myNum >= Lnum) and (myNum <= Tnum):
        return "it's in range try to make it smaller and guess my number"
    else:
        return "outside range boohoo try again"

lowNum = int(input("Gimme a number, it's gonna be the lower end of the range: "))
highNum = int(input("Gimme a number, it's gonna be the top end of the range: "))
print(checkRange(lowNum, highNum))
