from operator import indexOf


def print_message(day):
    messages = {
        'monday': 'Hello, world!',
        'tuesday': 'Today is Tuesday!',
        'wednesday': 'It is the middle of the week.',
        'thursday': 'Today is Donnerstag in German!',
        'friday': 'Last day of the week!',
        'saturday': 'Hooray for the weekend!',
        'sunday': 'Aw, the weekend is almost over.'
    }
    print(messages[day])

def print_friday_message():
    print_message('Friday')
print_friday_message()

"""
How many levels does the traceback have?
    3
What is the function name where the error occurred?
    print_friday_message()
On which line number in this function did the error occur?
    16
What is the type of error?
    KeyError
What is the error message?
    "Friday" is not an integer therefore it cannot be used as an index 
"""

def another_function():
    print('Syntax errors are annoying.')
    print('But at least Python tells us about them!')
    print('So they are usually not too hard to fix.')


"""
#Read the code below, and (without running it) try to identify what the errors are.
    There is an incorrect indent in the function, the function name is not followed by
    a parenthesis and colon, 
Run the code, and read the error message. Is it a SyntaxError or an IndentationError?
    Syntax Error
Fix the error.
Repeat steps 2 and 3, until you have fixed all the errors.
"""

message = ""
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + 'a'
    else:
        message = message + 'b'
    
print(message)

"""
Read the code below, and (without running it) try to identify what the errors are.
    Number should be number, a should be "a", message is not initialized
Run the code, and read the error message. What type of NameError do you think this is? In other words, is it a string with no quotes, a misspelled variable, or a variable that should have been defined but was not?
    NameError: misspelled variable
Fix the error.
"""

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])
"""
Read the code below, and (without running it) try to identify what the errors are.
    the fourth element is at index 3,and 4 will cause an out of range error
Run the code, and read the error message. What type of error is it?
    IndexError: list index out of range
Fix the error.
"""

