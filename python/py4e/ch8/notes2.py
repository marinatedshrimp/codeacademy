
"""Slicing Strings"""

t = [8,4,3,5,64,53,21,3,5]
t[:3]
#[8,4,3]
t[3:7]
#[3,5,64,53]

stuff = list()
#make me a new list
stuff.append("book od shit")
#append adds list items to the end of the lists
stuff.append('actual shit')
stuff.append(98)
print(stuff)

#dont do stuff = stuff.append(smth)
#thatll fuck shit up

"""Lists For Stuff Dont Ask Me These Notes Are In Random Order"""

some = [8,36,25,14,13,24,64]
print(8 not in stuff)
print(25 in stuff)
print(len(some))
print(max(some))
print(sum(some))
print(sum(some)/len(some))

poops = ['shit','banana','diarrhea','asstrash']
print(poops[3])
poops.sort()
print(poops)
print(poops[3])
#sort makes the list sort it out itself in order

"""how to use this thing instead of what we did
in chapter 5"""

#ch5?
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count += 1
ave = total/count
print('Average:', ave)

#ch8
numlist = list()
while True:
    inp = input('Enter a num: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
ave = sum(numlist)/len(numlist)
print('Average:', ave)
#this needs to keep all the things in memory
#so if you need like millions of nums then the ch5 one is better
#but if you already have all the nums in a list the ch8 is cool
