"""
def counter():
    count = 0
    total = int(input())
    R, G, B = [int(x) for x in input().split()]
    for t in range(total):
        ll, lr = input().split()
        if ll == "L":
            if lr == "R" or lr == "Y" or lr == "M" or lr == "W":
                R -= 1
            if lr == "G" or lr == "C" or lr == "W" or lr == "Y":
                G -= 1
            if lr == "M" or lr == "B" or lr == "C" or lr == "W":
                B -= 1
        else:
            if lr == "R" or lr == "Y" or lr == "M" or lr == "W":
                R += 1
            if lr == "G" or lr == "C" or lr == "W" or lr == "Y":
                G += 1
            if lr == "M" or lr == "B" or lr == "C" or lr == "W":
                B += 1
        count += 1
        print(R,G,B)
        if R == G and R == B:
            return count, R
            break
    else:
        return "no"
    
print(counter())
"""

#FIND GROUPS OF SEQUENTIALS AND ADD THE MAX VALUES OF THOSE SEQUENTIALS#
"""
amount = int(input())

s = input()
matrix = list(map(int, s.split()))
#take multiple inputs and make it into a list of ints
matrix.sort()
#make nested lists of sequentials first
#calculate the sums of each lists's max

def groupSequence(lst):
    res = [[lst[0]]]
    summ = 0
    for i in range(1, len(lst)):
        if lst[i-1]+1 == lst[i]:
            res[-1].append(lst[i])
  
        else:
            res.append([lst[i]])
    for list in res:
        summ = summ + max(list)
    return summ

myThing = 
#big = []
#for thing in matrix:
#    if len(matrix) == 0:
#        break
#    else:
#        big.append(max(matrix))
#       print(big)
#       for n in range(len(matrix)):
#            if max(matrix) - n in matrix:
#               print(max(matrix) - n)
#                matrix.remove(max(matrix) - n)
#            else:
#               break

print(groupSequence(matrix))
"""

#台風域にいるか確認（方式は与えられている）
"""
xc, yc, r1, r2 = [int(x) for x in input().split()]
people = int(input())
coords = []

for person in range(people):
    s = input()
    coords.append(list(map(int, s.split())))
for coord in coords:
    x = coord[0]
    y = coord[1]
    if r1 ** 2 <= (x - xc) ** 2 + (y - yc) ** 2 and (x - xc) ** 2 + (y - yc) ** 2 <= r2 ** 2:
        print("yes")
    else:
        print("no")
"""

#B040:たのしい暗号解読
"""
#number is the number of times you run the input through the akphabet switcher
ftimes, codealpha = input().split()
times = int(ftimes)
ogalpha = list("abcdefghijklmnopqrstuvwxyz")
newalpha = list(codealpha)
iline = input()
line = list(iline)

for time in range(times):
    for letter in range(len(line)):
        if line[letter] == " ":
            line.append(" ")
        else:
            line.append(ogalpha[newalpha.index(line[letter])])
        #i thought you were supposed to switch directions but that just makes the output the same as the input
#        else:
#            if line[letter] == " ":
#                line.append(" ")
#            else:
#               line.append(newalpha[ogalpha.index(line[letter])])
    del line[:len(iline)]
final = "".join(line)
print(final)
#input
#100 poiuytrewqlkjhgfdsamnbvcxz
#snn xufu ngebmv qwtg
#output
#cpp java python ruby
"""

#ゲームの画面　C052 (7min)
"""
#when shifting the image to make it seem like its moving
#calculate the pixels u would need to newly generate 
#so that its the least burden
width, height = [int(x) for x in input().split()]
y, x = [abs(int(x)) for x in input().split()] 
total = width * x + height * y - x * y
print(total)
"""

#B096:爆弾の大爆発
#place bombs on grid, count squares affected if bomb spreads to entire row,col
#output is affected area including initial bomb
"""
row, col = [int(x) for x in input().split()]
total = []
for y in range(row):
    eachRow = list(input())
    total.append(eachRow)

columnBombXtra = 0
rowBomb = 0
colBomb = 0
Xtra = 0
repeat =[]

for eachRow in total:
    if "#" in eachRow:
        rowBomb += col
        columnBombXtra += 1
#        repeat.append(eachRow.index("#"))

flipped = list(map(list, zip(*total)))
#flip row, col of 2d array
for column in flipped:
    if "#" in column:
        colBomb += row
        Xtra += 1
        

affect = rowBomb + colBomb - columnBombXtra * Xtra
print(affect)
"""   

#B091:山頂を探せ
#find cells of square grid that is taller than all adjacent cells
#takes too much time
"""
n = int(input())
total = []
chou = []
already = 0
already2 = 0

for rows in range(n):
    total.append(list([int(x) for x in input().split()]))

for j in range(n):
    for i in range(n):
        if total[j] == total[0]:
            if already == 1:
                pass
            if already == 0:
                already += 1
            if total[j][i] > total[j + 1][i]:
                if i == 0:
                    if total[j][i] > total[j][i + 1]:
                        chou.append(total[j][i])                    
                elif i == n - 1:
                    if total[j][i] > total[j][i - 1]:
                        chou.append(total[j][i])
                else:
                    if total[j][i] > total[j][i + 1] and total[j][i] > total[j][i - 1]:
                        chou.append(total[j][i])
        elif total[j] == total[-1]:
            if already2 == 1:
                pass
            else:
                already2 += 1
            if total[j][i] > total[j - 1][i]:
                if i == 0:
                    if total[j][i] > total[j][i + 1]:
                        chou.append(total[j][i])
                elif i == n - 1:
                    if total[j][i] > total[j][i - 1]:
                        chou.append(total[j][i])
                else:
                    if total[j][i] > total[j][i + 1] and total[j][i] > total[j][i - 1]:
                        chou.append(total[j][i])
        elif total[j][i] > total[j + 1][i] and total[j][i] > total[j - 1][i]:
            if i == 0:
                if total[j][i] > total[j][i + 1]:
                    chou.append(total[j][i])
            elif i == n - 1:
                if total[j][i] > total[j][i - 1]:
                    chou.append(total[j][i])
            else:
                if total[j][i] > total[j][i + 1] and total[j][i] > total[j][i - 1]:
                    chou.append(total[j][i])
            
        else:
            if total[j][i] > total[j + 1][i] and total[j][i] > total[j - 1][i]:
                print(total[j][i])
                if total[j][i] > total[j][i + 1] and total[j][i] > total[j][i - 1]:
                    chou.append(total[j][i])
                    
chou.sort(reverse = True)
print(*chou, sep = "\n")
"""

#C014:ボールが入る箱 
#see if ball goes in box of diff dimensions
"""
import math
boxes, radius = [int(x) for x in input().split()]
boxList = []

for box in range(1, boxes + 1):
    h, d, w = [int(x) for x in input().split()]
    if h * d * w >= radius ** 2 * math.pi and h >= radius * 2 and d >= radius * 2 and w >= radius * 2:
        boxList.append(box)
    
print(*boxList, sep="\n")
"""


#B079:相性チェック
#add values of letters in two names, if sum of two neighboring go over 101, take the value of sum - 101
#switch the first and second name and output the largest possible value
"""
n1, n2 = input().split()
indexog = 0
n1st = list(n1) + list(n2)
n2nd = list(n2) + list(n1)
alphabet = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
        
new = []
newN2 = []

for times in range(len(n1st) - 1):
    if new:
        limit = len(new)
        for number in range(len(new) - 1):
            add = new[number] + new[number + 1]
            if add > 101:
                new.append(add - 101)
            else:
                new.append(add)
        for number in range(limit):
            new.pop(0)
            
    else:
        for letter in range(len(n1st) - 1):
            add = alphabet[n1st[letter]] + alphabet[n1st[letter + 1]]
            if add > 101:
                new.append(add - 101)
            else:
                new.append(add)
    
for times in range(len(n2nd) - 1):
    if newN2:
        limit = len(newN2)
        for number in range(len(newN2) - 1):
            add = newN2[number] + newN2[number + 1]
            if add > 101:
                newN2.append(add - 101)
            else:
                newN2.append(add)
        for number in range(limit):
            newN2.pop(0)
            
    else:
        for letter in range(len(n2nd) - 1):
            add = alphabet[n2nd[letter]] + alphabet[n2nd[letter + 1]]
            if add > 101:
                newN2.append(add - 101)
            else:
                newN2.append(add)        
new.append(*newN2)
print(max(new))
"""

#B073 イルミネーションの調査
#check trees and if they are less than minimum required, add until at least minimum
"""
trees, minimum = [int(x) for x in input().split()]
matrix = input().split()
chick = []
for n in matrix:
    chick.append(int(n))

times = int(input())

for time in range(times):
    s, e = [int(x) for x in input().split()]
    sum1 = sum(chick[s-1:e])
    diff = e - s + 1
    ave = sum1 / diff
    while ave < minimum:
        for poop in range(diff):
            chick[e - 1 - poop] += 1
        ave += 1
print(*chick)
"""
"""
10 1 #trees, minimum average lights
3 3 7 3 7 5 8 3 5 3 #num of kights on qo trees
5 #checking 5 times
1 7 #check 1st to 7th lights and see if average if above 1
6 9
5 7
1 2
4 8
output: 3 3 7 3 7 5 8 3 5 3 since min is 1 so no need to chenge anything
"""

#C106:メダル授与式 再チャレンジ採点結果
#give top ppl medals, but if theres two Golds, the next top gets a silver
#if theres three people or more with the top two scores, theres no bronze
#if three+ slots are already taken, the next score gets Nothing
"""
people = int(input())
matrix = input().split()
chick = []
for n in matrix:
    chick.append(int(n))

myList = list(dict.fromkeys(chick))
myList.sort()
ogSort = chick.copy()
ogSort.sort()

for item in chick:
    if item == myList[-1]:
        print("G")
    elif item == myList[-2]:
        if item == ogSort[-2]:
            print("S")
        elif item == ogSort[-3]:
            print("B")
        else:
            print("N")
    elif item == myList[-3]:
        if item < ogSort[-3]:
            print("N")
        else:
            print("B")
    else:
        print("N")
"""
#B106:席替えの席決め
#there are more seats tahn students so if theres a gap 
#push the student up to the front
"""
rows, columns, students = [int(x) for x in input().split()]
line = [0] * rows * columns
for i in range(1, students + 1):
    seatNum = int(input())
    line[seatNum - 1] = i

chunkedList = [line[x:x+columns] for x in range(0, len(line), columns)]

flipped = list(map(list, zip(*chunkedList)))

for eachList in flipped:
    index = 0
    for i in eachList:
        if i > 0:
            eachList[eachList.index(i)] = 0
            eachList[index] = i
            index += 1

reflipped = list(map(list, zip(*flipped)))
for eachline in reflipped:
    print(*eachline)
"""
"""
6 4 5 rows columns students
4 number where student is sitting
12
6
24
9
so the seating chart number is 
1 2 3 4
5 6 7 8
...
output:
5 3 0 1
0 0 0 2
0 0 0 4
0 0 0 0
0 0 0 0
0 0 0 0
"""

#B081:花壇のロープ
#given the grid and placement of flowerbeds, 
#surround them with rope only if sides are not connected to another flowerbed
"""
height, width = [int(x) for x in input().split()]
matrix = []
for h in range(height):
    listt = list(input())
    matrix.append(listt)

total = 0

        
counter = 0
for list in matrix:
    
    for plot in range(len(list)):
        if list[plot] == "#":
            if plot == 0 or plot == width - 1: #outside of left/right perimeter
                total += 1
            if list is matrix[0] or list is matrix[height - 1]: #chcek outside of top/bottom perimeter
                total += 1
            if plot == 0 and list[plot] != list[plot + 1]: #inside of left perimeter
                total += 1
            if plot == width - 1 and list[plot] != list[plot - 1]: #chcek inside of right perimeter
                total += 1
            if list == matrix[0] and list[plot] != matrix[1][plot]: #inside of top perimter
                total += 1
            if list == matrix[-1] and list[plot] != matrix[-2][plot]: #inside of bottom perimeter
                total += 1

            if counter != 0 and counter != height - 1:
                if matrix[counter][plot] != matrix[counter - 1][plot]:
                    total += 1
                if matrix[counter][plot] != matrix[counter +  1][plot]:
                    total += 1
            if plot != 0 and plot != width - 1:
                if list[plot] != list[plot - 1]:
                    total += 1
                if list[plot] != list[plot + 1]:
                    total += 1 
            
    counter += 1            
print(total)
"""

#B016:ここはどこ？
#the edges all connect to eachother so 
#if u move off the right edge u go in from the left edge
#got some wrong answers
"""
width, height, times = [int(x) for x in input().split()]
ix, iy = [int(x) for x in input().split()]


for time in range(times):
    direction, spaces = input().split()
    spaces = int(spaces)
    match direction:
        case "U":
            iy += spaces
        case "D":
            iy -= spaces
        case "R":
            ix += spaces
        case "L":
            ix -= spaces

if ix > width:
    while ix > width:
        ix -= width
elif ix < 0:
    while ix < 0:
        ix += width
if iy > height:
    while iy > height:
        iy -= height
elif iy < 0:
    while iy < 0:
        iy += height

print(ix, iy)
"""
"""
7 6 1 width, height, times you will move
3 4 initial starting point
U 3 move up 3
output:
3 1
"""

#see if a player can move from one room to their desired one
#if there is already a player in the desired room they cant go
#if the desired room is the same room as their previous one they can go
"""
rooms, players, times = [int(x) for x in input().split()]
playRoom = []
for player in range(players):
    playRoom.append(int(input()))
    
for time in range(times):
    prevr, nextr = [int(x) for x in input().split()]
    if playRoom[prevr - 1] != nextr:
        if nextr in playRoom:
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")
"""
"""
15 10 10
1
2
3
4
5
11
12
13
14
15
1 6
5 6
6 6
8 6
5 11
6 11
9 11
10 11
6 2
8 3
output:
Yes
Yes
Yes
Yes
No
Yes
No
No
No
No
"""
#model
"""
n, m, q = map(int, input().split())
s = [int(input()) for _ in range(m)]

s.insert(0, -1)
for _ in range(q):
    e, t = map(int, input().split())
    if s[e] == t:
        print("Yes")
        continue

    for i in range(1, m + 1):
        if i != e and s[i] == t:
            print("No")
            break

        if i == m:
            print("Yes")
            """

#A052:階段登り
#theres c total steps and you can take
#a or b steps at a time
#calculate the steps that wont get stepped on 
#you can do 3,3,2 if a3, b5, c8 and ignore the set steps rule
#for the last bit
"""
stairs = int(input())
fstep, sstep = [int(x) for x in input().split()]
stairList = []
erase = []

for i in range(1, stairs):
    stairList.append(i) #make a list of all steps then start removing what gets stepped on 

for x in range(int((stairs - stairs % fstep) / fstep) + 1):
    for y in range(int((stairs - stairs % sstep) / sstep) + 1):
        if fstep * x + sstep * y <= stairs:
            erase.append(fstep * x + sstep * y)

erase.append(stairs)
erase = list(dict.fromkeys(erase))
erase.pop(0)
print(stairs - len(erase))
"""
"""
8 #num of stairs
3 5 #steps at a time
output:
4

7
3 5
output:
3
"""

#B107:カードシャッフル
#take x cards, seperate into groups of y,
#reverse order of groups z times
"""
from itertools import chain

cards, groups, times = [int(x) for x in input().split()]

stack = list(range(1, cards + 1)) #make list of ints 1 ~ cards
chunked =[]

for time in range(times):  
    for i in range(0, cards, groups):
        chunked.append(stack[i: i + groups])
    chunked.reverse()
    stack = list(chain(*chunked)) 
    #chain connects two lists and * connects all of them
    chunked.clear() #clears list
    
print(*stack, sep = "\n")
"""
"""
10, 3, 2
output:
3
6
1
2
9
4
5
10
7
8
"""