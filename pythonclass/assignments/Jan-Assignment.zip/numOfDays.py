#Marina Tanaka
'''
accept a number from 1 to 12 and display the name 
of the month and days in that month like 1 for January and 
number of days 31 and so
'''

'''
feb is special so have an if especially for that.
check to see if the month is divisible by 2, then if its before june
to determine the date, using nested if statements. 
use the list index to get the month name 
'''

iMonth = int(input("Gimme a month number: "))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if iMonth == 2:
    print("There are 28 days in February")
elif iMonth % 2 == 0:
    if iMonth <= 6:
        print("There are 30 days in {}".format(months[iMonth - 1]))
    else:
        print("There are 31 days in {}".format(months[iMonth - 1]))
else:
    if iMonth < 6:
        print("There are 31 days in {}".format(months[iMonth - 1]))
    else:
        print("There are 30 days in {}".format(months[iMonth - 1]))