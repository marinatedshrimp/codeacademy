from getpass import getpass
import math

#lists and tuples are sequence datatypes
#ictionary is a mapping datatype

notallowedVarName = "my-var, 9myvar"

operators = "+ - * / ** %"
5 // 2  #will return 2(an integer value)
a = 25
print(math.sqrt(a))

equal = "is an assignment operator"
print(equal[0])
print(equal[3:10])
print(equal[:10])
print(equal[10:])
#[]doesnt include the final character so [3:10] is 3-9
print(equal * 2)
#prints it twice

a = 1
a += 4
if a == 2:
    print(a)
    print("yay you did it it's two")
elif a != 2:
    print("lol not 2")

comparison_operators = [">","==", "etc."]
logical_operators = ["and", "or","nor","exor","not"]



#start terminal interactive w "python" and exit w "exit()"

datatypes = ["strings", "numbers", "lists", "tuples", "dictionaries"]

"""
git clone
git add .
git commit -m"wee"
git push
"""

print(type(x)) #to get the type of variable it is
#ex. int float complex string tuple list range bool etc.

#In interactive mode, use _ as the answer button
v = 9
very = v + 78
veryy = 58 + _

#print(int(2.999)) is similar to math.floor(2.999) == 2

opposite = math.ceil(2.999) == 3

abs(-45.600) == 45.6


#--MULTISTRING PRINT--

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#produces the following output (note that the initial newline is not included):
"""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

#--PRINT THE LITERAL \n--

#>>> print('C:\some\name')  # here \n means newline!
#C:\some

#>>> print(r'C:\some\name')  # note the r before the quote
#C:\some\name

#--CONCATENATED STRINGS--

text = ('Put several strings within parentheses', 'to have them joined together.')
print(text)
'Put several strings within parentheses to have them joined together.'

"""
Python does not support a character type;
a single character is treated as strings of length one.
"""


#======LISTS======#

squares = [1, 4, 9, 16, 25]

newSquares = squares.copy()
newSquares2 = list(squares)
#makes shallow list of squares

#python supports concatenation
num_list = squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#strings are immutable but lists are mutable
cubes = [1, 8, 27, 64]
cubes[3] = 64
#cubes == [1, 8, 27, 64]

cubes.append(125)
cubes.append(6 ** 3)
#cubes == [1, 8, 27, 64, 125, 216]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
#letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']

letters[2:5] = []
#letters == ['a', 'b', 'f', 'g']

#empty the list by replacing all elements with an empty list
letters[:] = []
#letters ==[]

del letters[0:79]
#letters == []
#it doesnt give u error if u go out of range
#you can even add numbers and extend a list this way

#nest lists inside lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
y = a + n
z = a.extend(n)
#x,y,z == [['a', 'b', 'c'], [1, 2, 3]]

#find individual lists or elemetns from nested lists
x[0] == ['a', 'b', 'c']
x[0][1] == 'b'

l = [None] * 10
print(len(l))
#10 not 0

#commas add an automatic space
#do + to eliminate space
a, b = 0, 1
while a < 10:
    print('You have done', a, 'European loops')
    a, b = b, a+b

#join elements together and link them with smth
greetings = ["hi", "there"]
print("-".join(greetings))

#go through all items and modify them
am = [1,2,3,4,5]
pow = [2 * x for x in am]
print(pow)

limp = ["xyz", "zara", "pynative"]
print(max(limp))
#zara
limp[2] = "PYnative"
print(max(limp))
#zara
#ABC has smaller value than abc cuz alphabetical order puts
#upper case before lower case

unsorted = [1,4,3,6,5,4,8,6,4]
print(sorted(unsorted))
#arranges list into ascending order

print(max(unsorted))
print(min(unsorted))
#prints max/min value of list

#//-----FOR LOOPS-----//

words = ["eh", "aboot", "oot"]
for i in words:
    print(i)
i = "user-declared variable"
inin = "membership operator"

for p in range(5):
    print(p)
    #01234
    
for p in range(3,5):
    print(p)
    #34

for num in range(2,-5,-1):
    print(num, end=", ")
    # 2, 1, 0, -1, -2, -3, -4

marker = ["blueberry", "orange", "red"]
bird = ["wings", "beak", "feetieweeties"]

for i in marker:
    print(i,bird[marker.index(i)])
#blueberry wings
#orange beak
#red feetieweeties

for i in marker:
    for u in bird:
         print(i,u)
'''
blueberry wings
blueberry beak
blueberry feetieweeties
orange wings
orange beak
orange feetieweeties
red wings
red beak
red feetieweeties
'''

print("Hello" , end = ' ')
print("world")
#Hello world

print("Hello")
print("World")

"""
Hello
world
"""

for i in range(11):
    if i % 3 == 0:
        continue
    print(i)
# 12457810 but all in new lines

for i in "string":
    if i == "i":
        break
    print(i, end = ' ')

i = 0
while i < 11:
    if i % 5 == 0:
        break
    print(i)
    i += 1

#---INTERPOLATION---#
txt1 = "My name is {fname} and I am {age} years old".format(fname = "Johnny", age = 34)
txt2 = "My name is {0} and I am {1}".format("Mark", 44)
txt3 = "My name is {} and I am {}".format("Marc", 33)

#---TUPLES---#
lists_mutable = ["1", "2", "3"]
tuples_immutable = ("1", "2", "3")

tuple[0] = "100" #would not work
listInTuple = ("1", "2", "model", ["100", "200", "300"])
#immutabiliry makes it process faster
#creates a 

tuple1 = ("hello") #type == str
tuple2 = ("hello", ) #makes it a tuple once you add a comma
tuple3 = "hello", #parenthesis is optional
#tuples can hold a mix of var types

a, *b, c = (1, 2, 3, 4)
print(a, c)
#output 1 4

#--DICTIONARY--#
dict = {"key: value"}
dikt = {"brand": "Chevy", "model": "Impala", "year": "1964"}
print(dikt["brand"])
print(dikt.keys())  #function prints dict_keys(['brand', 'model', 'year'])

print(dikt.values())    #prints dict_values(['Chevy', 'Impala', '1964'])

#example
tables = {
    1: {"name": "Tina", "vipStatus": "True", "order": "apple juice"},
    2: {},
    3: {},
    4: {},
}

def tables(tableNum, name, vipStatus = False):
#False is the default value
    tables[tableNum]["name"] = name
    tables[tableNum]["vipStatus"] = vipStatus
    tables[tableNum]["order"] = ""

def assignPrintOrder(tableNum, *orderItems):
    tables[tableNum]["order"] = orderItems
    print(tableNum)
    for order in orderItems:
        print(order)
#*takes into account the varying num of args


#---FUNCTIONS---#

def killbill():
    print("lol you're such a bum")
killbill()

def funcWPara(fname, lname):
    print(fname, lname + " is a bad name")
funcWPara("smithsonian", "mermaid")

def add(number1, number2):
    return number1 + number2 

anum = int(input("Gimme num: "))    #if no int() it just combines two strings
bnum = int(input("anotha one: "))
add(anum, bnum)

#when you set it up the info in the () is known as parameters, 
#when you call it they're called arguments

def infinite(*kids):
    print("The youngest child is " + kids[2]) #need to input more args than 3

infinite("kite", "bite", "fight", "night", "light", "Sight", "site" ) #main func

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))   #multiplies it like a nesting doll

num = math.floor(float(input("gimme a number but ill only take positive integers: ")))
print("the factorial of", num, "is", factorial(num))


#FIBONACCI

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))


num = (abs(int(input("gimme a number but ill only take positive integers: "))))
if num > 10:
    num = 10


for i in range(num):
    print(fib(i))
    

#-----LAMBDA OR ANONYMOUS FUNCTION-----#

#cannot 

def add(x):
    return 3 * x + 1
add(2)
#    |
#    |
#    \/
g = lambda x: 3 * x + 1
g(2)
#to be used just once or twice

fullName = lambda fn,ln : fn.strip().title() + " " + ln.strip().title()
#can't say fn.blah, ln.blah cus then it's like ur making a tuple
fullName("  leonard", "EULER")
#"Leonard Euler"

#sorting list of strings
artists = ["Ariana Grande", "Caroline Constar", "Aoyah Emile Somoa"]
artists.sort(key = lambda name: name.split(" ")[-1].lower()) 
print(artists)

def quadratic(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
"""
g = quadratic(2, -3, 9)
g(8)
"""
#a better way to put it is
quadratic(3,4,5)(8)

"""
u can't make two lambda functions in one reg func and expect it to know which one g(8) is for
cant define functions inside a loop so we use lambda to create one-line fuctions
"""

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
check_if_A_grade(98)
#output: Got an A!

#------ACCESSING FILES MID-CODE-----#

#if ur in f1.py in python folder and r1.txt is also in python folder
var = open("r1.txt", "r")

#if r1.txt is in a seperate folder, u need to say the end path
var = open("/Users/marinatanaka/Documents/codeacademy/pythonclass/r1.txt", "r") #"r" means ur in read mode
contents = var.read()
#read(10) will read the first 10 characters
print(contents)

var.close() #close or else it will crash

#-----LIST COMPREHENSION-----#
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square) 

def updateOrder(newItem, currentOrder = None):
#= None creates a default value for when no value is entered
    if currentOrder is None:
        currentOrder = []
    currentOrder.append(newItem)
    return currentOrder
order1 = updateOrder({"item":"cookie", "cost":"1.00"})
order2 = updateOrder({"item":"BBQ sauce", "cost":"4:50"})
#None - when printing order2, only the info inputted in order2 will be stored in the var
#w/out None, it would storethe accumulated info

#---WORKING W A VARIABLE NUM OF ARGS---#
def printOrder(*items):
    print(items)
printOrder("apple", "table", "cup")


#Procedural, Functional, Object Oriented Programming
#   ObjO can do abstraction, encapsulation, inheritance through 
#   Objects and Classes(attributes, methods, functions, sub-classes)

class User:
    pass
user = User() #user is an object
user.fname = "ahhh"
user.lname = "nomnom"
print(user.fname, user.lname)
user2 = User()
user2.fname = "david"
user2.lname = "lalala"
print(user2.fname, user2.lname)
user.age = 89
user2.favBook = "The Wilted Flower"
#use classes instead of dicts because you can store methods and functs
#inside classes


#what if the attribute we want to set is the value of another 
person = User()
firstKey = "first"
firstVal = "Corey"

#person.firstKey = firstVal would not work

setattr(person, "first", "Corey")
#or
setattr(person, firstKey, firstVal)
print(person.first)
#output: Corey

first = getattr(person, firstKey)
print(first)
#output: Corey

personInfo = {"first": "Corey", "last": "Schafer"}
for key,value in personInfo.items():
    setattr(person, key, value)
print(person.first)
print(person.last)
"""
Corey
Schafer
"""

for key in personInfo.keys():
    print(getattr(person, key))



#INHERITANCE#
"""
class ParentClass:
    pass

class childClass(ParentClass):
    pass
"""

class Rocket():
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    
    def launch(self):
        return "%s has reached %s" %(self.name, self.distance)

class MarsRover(Rocket): #inheriting from Rocket
    def __init__(self, name, distance, maker):
        #you wanna inherit name and distance from Rocket
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def getMaker(self):
        return "%s launched by %s" %(self.name, self.maker)

a = Rocket("rocket", "till stratosphere")
b = MarsRover("mars rover", "till mars", "NASA")

print(a.launch())
print(b.launch())
print(help(MarsRover))
#to see how the child class works

"""
rocket has reached till stratosphere
mars rover has reached till mars
mars rover launched by nasa
"""

#SUPERCLASS#

#-----ERRORS-----#
"""
Syntax error
Run time
Compile Time

Error handling
"""
try:
    #where you try a thing when ur not sure if it would work
    pass
except Exception: 
    #runs when there are errors in code in try
    #Exception accepts any exception but u can say ValueError, etc if u wanna be specific abt it
    pass
else:
    #runs if there's no problems with the actions in try
    pass
finally:
    #will run no matter what


    try:
        var = 3
        raise NameError("leave me alone")
    except NameError: # the fact that u raised in the try caused a NameError
        print("ummm")
        raise #raises whatever you said even if it doesn't match the error idk man


