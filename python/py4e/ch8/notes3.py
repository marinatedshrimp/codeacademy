
"""Split Strings"""

abc = 'Fun with English'
tsilist = abc.split()
print(stuff)
#['Fun','with','English']
print(len(stuff))
#3
print(stuff[0])
#'Fun'

for w in stuff:
    print(w)

"""Splitting With Other Stuff"""

line = 'A lot of          spaces'
etc = line.split()
print[etc]
#the () describes the delimiter
#when the delimiter is not specified it assumes its a space

line ='first;second;third'
thing = line.split()
print(thing)
#['first;second;third']
print(len(thing))
#1

thing = line.split(';')
print(thing)
#['first','second','third']
print(len(thing))
#3

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words[2])
#the third word will always be the day of the week so print it out

"""the other way to do this is by using find"""

for line in fhand:
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    #('plaplaplaplapla','uct.ac.za')
    print(pieces[1])
    #uct.ac.za
