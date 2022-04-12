
"""Basically Just List Basics"""

cheese = ['parmesean','cheddar','gouda']
#list constants are surrounded by square brackets
#lists can contain lists or nothing at all
count = 0
listie = [1,3,2,5,4,'nopopo']
for items in listie:
    count += 1
    print('fuck off poopoo')
    print(count)
#read the square brackets as 'sub'
print(cheese[0])

fruit = 'Banana'
try:
    fruit[0] = 'b'
except:
    print('strings are immutable, meaning we cannot change its contents')
x = fruit.lower()
print(x)

"""fuit.lower() makes a copy of Banana and the prints
a lower case copy of it so it doesnt truly change it"""

lottery = [0,43,65,765,13,44,3,9]
print(lottery)
lottery[2] = 34
print(lottery)

print(range(4))
#this will print out the numbers from 0 to but
#not including 4 much like [0,4]

print(len(cheese))
#3
print(range(len(cheese)))
#[0,1,2] becasue it means print(range(3))

for i in range(len(cheese)):
    cheesetits = cheese[i]
    print('Wow you taste great:', cheesetits)
"""instead of doing like cheesetits = 0 and stuff you can
have it done for you in case youre like huh i want to send
this to the cheese in 2nd position idk"""

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













