#make all the words in the file line up in alphabetical Order

#me try no good
fname = input('Enter file name: ')
fh = open(fname)
prudent = []
for line in fh:
    line = line.rstrip()
    words = line.split()
    if words not in prudent:
        prudent.append(words)
print(prudent.sort())

fh = open(fname)
prudent=[]
for line in fh:
    words = line.split()
    for word in words:
        if word not in prudent:
            prudent.append(word)
prudenter = prudent.sort()
print(prudenter)

#answer wtf i dont fucking get it

fname = input("Enter file name: ")
fh = open(fname)
data - []
for each in fh:
    words = each.split()
    if word not in data:
        data.append(word)
print(sorted(data))
