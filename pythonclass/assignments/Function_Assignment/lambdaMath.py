"""
lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y 
and prints the result. 
Sample Output:
25
48
"""



add = lambda num: num + 15
multi = lambda x, y: int(x) * int(y)

number = int(input("gimme a number: "))
print(add(number))

number1, number2 = input("gimme two numbers and seperate w a space: ").split(" ")
#cant do int() cuz its not a string its a list
#need to make it an int somehow or else it wont be able to be multiplied
print(multi(number1, number2))