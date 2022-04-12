#Marina Tanaka
#Using a for loop, reverse a given integer
'''
print the number at the index of iNum in descending order,
making sure to subtract 1 so that it does not go out of the 
scope of the entered integer. add end so that it does not
print one number per line
'''

iNum = input("Gimme an integer: ")
sNum = str(iNum)    #make iNum a string so that you can get the range of it since 


for i in range(len(sNum)):
    print(iNum[len(sNum) - i -1], end = "")