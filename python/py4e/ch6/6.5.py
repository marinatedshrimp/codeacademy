#use .find() and slicing to get just the numbers
text = "X-DSPAM-Confidence:    0.8475";
sp = text.find(' ')
spnum = text[sp:]
num = float(spnum.lstrip())
print(num)

#the teacher did this
col = text.find(':')
print(col)
piece = text[col+1:]
#or text[col + 2 :]
print(piece)
num = float(piece)
print(num)
