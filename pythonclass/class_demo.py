import datetime

"""class User:
    #__init__ is a default method
    def __init__(self, fullName, birthday): #attributes
        self.fullname = fullName
        nameBits = fullName.split() #split makes it into a lsit
        self.fname = nameBits[0]
        self.lname = nameBits[-1] #just in case there's a middle name
        self.birthday = birthday
    
    def age(self): #default arg of self
        return datetime.date(2022, 2, 22)
    
user = User("marina splenda", "1998-10-31")
print(user.birthday)
print(user.fullname)
print(user.fname)
print(user.lname)

print(user.age())"""

"""
import numpy as np

def route():
    size, limit = [int(x) for x in input().split()]
    matrix = []
    for i in range(size):
        matrix.append(input().split())
    
    flipped = np.array(matrix).T.tolist()
    count = 0
    a = []
    for rain in flipped:
        count += 1
        for spe in rain:
           
            if int(spe) >= limit:
                break
        else:
            a.append(count)
    if a:
        return " ".join([str(i) for i in a])
    else:
        return "wait"
                
print(route())
"""


#ERRORS
"""try:
    f = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/assignments/read.txt")
    #var = bad_var #theres no name for this error so it goes under Exception
except FileNotFoundError:
    print("no such file")
except Exception:
    print("wtf kind of var is that")
else:
    print(f.read())
    f.close()
finally:
    print("wanna do some more?")
"""

#ADD POINTS TO POINT CARD 3% IF DATE INCLUDES 3, 5% IF INCLUDES 5, 1% IF NEITHER
"""
import math
times = int(input())
sum = 0
for i in range(times):
    day, amount = [int(x) for x in input().split()]
    if "3" in str(day):
        sum += math.floor(amount * 0.03)
    elif "5" in str(day):
        sum += math.floor(amount * 0.05)
    else:
        sum += math.floor(amount * 0.01)
print(sum) 
"""

#FURTHEST THE BUBBLE WENT WITHOUT TOUCHING THE GROUND C057
"""
time, xi, yi = [int(x) for x in input().split()]
xout = [xi]
yhigh = [yi]

for count in range(time):
    #x,y mark the diff in x,y between a set amount of time, not the acc coords
    x, y = [int(x) for x in input().split()]
    xi += x
    yi += y
    if yi <= 0:
        break
        #quit if the bubble touches ground
    xout.append(xi)
    yhigh.append(yi)

print(xout)
print(max(xout))
#smth went wrong w this code idk what
"""

#complete folling codes
a=5
b=0
try:
    result=a/b
except ZeroDivisionError:
    print("you cant divide by zero")

print(result)

#//////////

a = [1, 3, 5]
try:
    a.get()
except:
    print("what are yo utrying to get im so confused")

print(a)

#/////////

a="Hello World!"
try:
    a + 10
except:
    msg = "you cant add stuff"
    print(msg)



#//////////

lst=[5, 10, 20]

try:
    print(lst[5])
except:
    msg = "out of range dude"
    print(msg)



