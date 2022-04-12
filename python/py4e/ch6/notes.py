print("---INDEX OF A WORD---")
#looking inside strings
fruit = 'banana'
letter = fruit[1]
print(letter)
#this will reslut in a
print(len(fruit))
#that's 6

print("---PRINT OUT THE LETTERS ONE BY ONE---")
#this is a long sad version
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
#of what these two lines could do
for letter in fruit:
    print(letter)
#letter is an iteration variable

#SLICING STRINGS
print("---SLICE MONTY PYTHON---")
s = 'Monty Python'
print(s[0:4])
#0 up to but not including 4
print(s[6:7])
#P
print(s[6:20])
#NOT traceback
#Python
"""if the ends are not filled in Python
will assume ur talking abt the beginning"""
print(s[:2])
#Mo
print(s[:])
#Monty Python

print("---IS A CERTAIN THING IN A WORD?---")
print('n' in fruit)
#True
print('nan' in fruit)
#True
print('k' in fruit)
#False
if 'an' in fruit:
    print('Found it yall')

print("---WHERE IS A CERTAIN THING IN A WORD?---")
pos = fruit.find('na')
print(pos)
#2
aa = fruit.find('z')
print(aa)
#not found = -1 so itll return -1

zot = 'abc'
try:
    print(zot[8])
except:
    print('fuck you')

#Upper case < lower case

print("---TWIDDLE WITH WORDS USING str.something()---")
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
#hello Bob
#return the lower case version
zappy = greet.upper()
print(zappy)
#HELLO BOB
rep = greet.replace('Bob','Jane')
print(rep)
#Hello Jane

greet = '      Hello Bob   '
print(greet.lstrip())
#'Hello Bob   '
print(greet.rstrip())
#'       Hello Bob'
print(greet.strip())
#'Hello Bob'

print("--PREFIXES--")
line = 'Please go fuck yourself'
print(line.startswith('Please'))
#True

print('abc'.capitalize())
#Abc

print("---APPLY IT TO AN EMAIL---")
email = 'From brourso.fuckingstupid@ups.kuroneko.jp Sat Jan 5 09:14:16 2020'
atpos = email.find('@')
print(atpos)
#21
sppos = email.find(' ',atpos)
print(sppos)
#look for a space after atpos
host = email[atpos + 1 : sppos]
print(host)
#ups.kuroneko.jp
#from after the @ to before the space
