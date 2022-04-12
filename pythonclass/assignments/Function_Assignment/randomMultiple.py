"""
func will take one argument & multiply it by an unknown given number. 
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
"""

def multi(intNum):
    dub = "Double the number of " + str(intNum) + " = " + str(intNum * 2) 
    trip = "Triple the number of " + str(intNum) + " = " + str(intNum * 3)
    quad = "Quadruple the number of " + str(intNum) + " = " + str(intNum * 4)
    quin = "Quintuple the number of " + str(intNum) + " = " + str(intNum * 5)
    return [dub, trip, quad, quin]

number = int(input("gimme a number: "))
print(*multi(number), sep = "\n")
#why does (multi(number)) w/out asterisk not work?

