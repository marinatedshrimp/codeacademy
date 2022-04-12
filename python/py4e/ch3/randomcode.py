print('curse you perry the platypus')
#europe ground level is 0 and us is 1
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

xh = input("Enter hours: ")
xr = input("Enter rate: ")
xp = float(xh) * float(xr)
print("Pay:", xp)
"""you dont need a space cuz the comma
 adds a space automaticaly"""

"""if the code makes sense it runs the try section and
if it doesnt it runs except so the parts after dont just
not run"""
rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('yippie')
else:
    print('aw shucks')

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
