while True:
    line = input("put in quotations> ")
    if line == "done":
        break
    else:
        print(line)
print("DoNe;)")

#continue skips back to the beginning of the loop
#break skips out of the loop
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Donitty done')
#those indented parts are called code blocks

friends = ['Joseph', 'Malory', 'Mackarel Shit Crumble']
for friend in friends:
    print('Happy new year', friend)
print('Done!')

#Loops and Iterations: Finding the Largest Value
print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')

largest_so_far = -1
#-1 is a flag value. if the nums were
#less than that it would be wack
print('Before', largest_so_far)
for num in [9,41,12,3,55,78,908,74]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)
print('After', largest_so_far)

#count the number of things
count = 0
print('Before', count)
for thing in [9,41,12,3,55,78,908,74]:
    count = count + 1
    print(count, thing)
print('After', count)

#add all 'thing's
sum = 0
print('Before', sum)
for thing in [9,41,12,3,55,78,908,74]:
    sum = sum + thing
    print(sum, thing)
print('After', sum)

#get the average of the things(values)
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,55,78,908,74]:
    count = count + 1
    sum = sum + Value
    print(count, sum, value)
print('After', count, sum, float(sum / count))

smallest = None
#None is a None type variable like booleans and
#floats but it only includes None. Nothing else.
#It means that we have seen nothing so far.
print('Before we go shit')
for value in [9,41,12,3,55,78,908,74]:
    if smallest is None:
        smallest = value
#only for the first time cuz smallest is None
    elif value < smallest:
        smallest = value
#every other time smallest has a num so this is ok
    print(smallest, value)
print('After', smallest)
#use if for True etc for num use ==
