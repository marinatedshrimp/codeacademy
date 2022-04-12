largest = None
smallest = None
while True:
    num = input("Enter a number(type done if done): ")
    if num == "done":
        break
    try:
        inum = int(num)
    except:
        print('Invalid input')
    if smallest is None:
        smallest = inum
    elif largest is None:
        largest = inum
    elif inum > largest:
        largest = inum
    elif inum < smallest:
        smallest = inum
print('Maximum is', largest)
print('Minimum is', smallest)
