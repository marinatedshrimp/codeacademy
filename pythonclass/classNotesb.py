"""
single inheritace
    A -> B 
multi-level inheritance
    A -> B -> C (C can have attributes frm A)
multiple 
    A -> B
      -> C
"""

#super.ClassName() #changed value in child class but want to use og values

class Employee:
    def __init__(self, empName):
        self.empName = empName 
    
    def calcWage(self, hours):
        self.hours = hours
        return hours * 20.00
        #dont need self.hours for parent class
    
class PartTime(Employee):
    def calcWage(self, hours):
        self.hours = hours
        return self.hours * 12.00 #child class so needs self.
        #this method overrides the past calcWage so if u run this code 
        #itll return hours * 12
    
    def fullTimeWage(self, hours):
        return super(PartTime, self).calcWage(hours)
        #override the calcWage method in the PartTime class
        #return super(overriddenclassName, self).overriddenMethodWithinClass(parameters)
    
a = PartTime("miss piggy")
print(a.fullTimeWage(10))

#TERNARY CODE (SHORTEN IF ELSE CODE)
condition = True
if condition:
    x = 1
else:
    x = 0

# ||
# ||

x = 1 if condition else 0

#COMMA REPLACEMENT IN CODE
num = 10000000000
# ||
# ||
num = 10_000_000_000
"""the _ wont effect the program in any way
   the _ won't appear in the ouput so if you want it to"""
print(f"{num:,}")
#output: 10_000_000_000


#CONTEXT MANAGER WHEN OPEN/CLOSE FILE
with open("text.txt", "r") as f:
    file_contents = f.read()
"""
instead of doing open, close as seperate things
"""

words = file_contents.split(' ')
wordCount = len(words)


#ENUMERATE/ZIPPPPPPPP
names = ["Corey", "Capeca", "Corne", "Coocoo"]

"""
index = 0
for name in names:
    print(index, name)
    index += 1
"""

for index, name in enumerate(names, start = 0):
    print(index, names)

#enumerate(names) if starting from 0
#enumerate(names, start = 2) if wanting to start index at 2

normNames = ["peter parker", "Clark kent", "wade wilson", "bruce wayne"]
heroes = ["spiderman", "superman", "deadpool", "batman"]

"""
for index, name in enumerate(normNames, heroes):
    hero = heroes[index]
    print(f"{name} is actually {hero}")
"""
for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")
#can use zip for more than one list just add to two parameters

for value in zip(names, hero):
    print(value)
    #output: ("peter parker", "spiderman")
    #         etc....


#UNPACKING
a, b = (1, 2) #might need 
a, _ = (1, 2) #tells that were not planning on using the variable

a, b, c = (1, 2) #won't work cuz theres not enough values to unpack

a, b, c = (1, 2, 3, 4, 5) #valueError: too many values to unpack
a, b, *c = (1, 2, 3, 4, 5) #assign c to all values after 2
"""a = 1, b = 2, c = [3, 4, 5]"""

a, b, *c, d = (1, 2, 3, 4, 5) #c = all values other than first two and last one
"""a = 1, b = 2, c = [3, 4], d = 5"""

a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(b)
print(d)
"""1, 2, 7"""
#can use multiple _ if wanting to ignore multiple parts


#how to hide password when typing it in
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")
print("Logging In...")



#----NAMESPACE----#
"""
a namespace is a dict that contains names and the objects that they refer to.

BUILT-IN NAMESPACE = all key words that come with python(there are 152). This does not count the imported words.
print(dir(__builtins__))

GLOBAL NAMESPACE = all variables used in global space of code(doesn't include vars inside functions).
When importing datetime, etc. the program creates a new global namespace for all of the keywords within the module
but the module name itself will appear in the global namespace.
    globals()
    x = "foo"
    print(x) == print(globals()["x"])

LOCAL NAMESPACE = namespace within a function. 

ENCLOSING NAMESPACE = Enclosing namespaces are created specifically when working with nested functions 
and just like with the local namespace, will only exist until the function is done executing. 
if theres a nested f() within g(), g is the enclosing and f is the enclosed function. 
any name in g() will be in the snclosing namesoace relative to f()

"""

#-----SCOPE-----#
"""
nonlocal varName makes the varName mutable from outside the scope but is specific to nested functions
global varName allows mutation of global variable in a local scope so its more broad than nonlocal

Python will look from local, enclosing global, then built-in when called = LEGB

"""

#HIGHER ORDER FUNCTIONS
"""
Higher-order functions are functions that operate on other functions by taking another 
function as an argument, returning another function, or both.
"""

def total_bill(func, value):
  total = func(value)
  return ("The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total

def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total

total_bill(add_tax, 100) 
total_bill(add_tip, 100) #MAKE A FUNC TO CALL FUNCS SO THAT YOU CAN HAVE A STREAMLINED OUTPUT MORE CONVENIENTLY



def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,        
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length*width*height
 
    return volume #returns value of volume func
 
box_volume_height15 = make_box_volume_function(15)
print(box_volume_height15(3,2))

box_volume_height10 = make_box_volume_function(10)
print(box_volume_height10(3,2))


#-----MAP-----#
"""
thing = map(function, iterable)

if kept like this, printing thing will get you the place in memory, so u should do

thing = list(map(func, iterable))
"""

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]

print(list(map(double, numbers)))

#output: [2, 4, 6, 8, 10]

#-----FILTER-----#
"""
filters and returns the items in an iterable that fit the conditions given
"""

names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
 
M_names = list(filter(lambda name: name[0] == "M" or name[0] == "m", names)) 
 
print(M_names)

#output: ['margarita', 'Masako', 'Maki']

#-----REDUCE-----#
"""
returns a single value. In ex below, x = 3, y = 6 then x = 18, y = 9 until it multiplies the last element
"""
from functools import reduce
 
int_list = [3, 6, 9, 12]
reducedInt = reduce(lambda x,y: x*y, int_list)
print(reducedInt)
#output: 1944

"""
can use to join a list of letters into one word
"""

letters = ['r', 'e', 'd', 'u', 'c', 'e']
word = reduce(lambda x, y: x + y, letters)
print(word)
#output: reduce

#-----RETURNING FUCTIONS-----#
def getMath(operation):
    def add(x, y):
        return x + y
    def sub(x, y):
        return x - y

    if operation == "+":
        return add
    elif operation == "-":
        return sub

addFunc = getMath("+")
print(addFunc(4, 6))

#equal to
addFunc = getMath("+")(4, 6)


#-----DECORATORS-----#
def titler(nameFunc):
    def wrapper():
        print("prof:")
        nameFunc()
    return wrapper

@titler
def printName():
    print("marina")

@titler
def printCapeca():
    print("capeca")
"""
printDecorated = titler(printCapeca)
printDecorated()
"""
printName()
printCapeca()
"""
most times the decorator func is stored in a seperate file, like a library file.
Not really a good idea to use them and nested for loops and nested stuff in general
"""



























