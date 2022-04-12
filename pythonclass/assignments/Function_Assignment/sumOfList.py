"""
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output: 20
"""
sumOfNum = 0
numList = []

def inputNum():
    print("type 'quit' once youre done")
    inputNumber = int(input("gimme another number: "))
    numList.append = inputNumber
    if inputNumber != "quit":
        numList.append = inputNumber
    else:
        return #can use break but not if inside a for loop or def
        
    



for num in range(len(numList)):
    sumOfNum = sumOfNum + numList[num]

print(sumOfNum)

