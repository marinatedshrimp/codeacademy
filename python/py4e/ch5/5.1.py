num = 0
tot = 0.0
while True:
    sval = input('Enter a number(if youre good say done): ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
        #use continue to escape the fucked up situation
    num = num + 1
    tot = tot + fval
    print(tot)

print('All done bitches')
print(f"total: {tot} you put in {num} numbers")
print('Average:',tot/num)
