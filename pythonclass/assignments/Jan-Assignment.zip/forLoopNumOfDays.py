#Marina Tanaka
'''
Using a for loop, write a program to accept a number from 1 to 12
and display the name of the month and days in that month like 
1 for January and number of days 31 and so on
'''

iMonth = int(input("Gimme a month number: "))
sMonth = str(iMonth)    #make it a string to iterate through 
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for i in sMonth: #if iMonth is used it will print out iMonth lines saying the same thing
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
#iterate through all the months and look at the entered month to get the 
#correct data about it


