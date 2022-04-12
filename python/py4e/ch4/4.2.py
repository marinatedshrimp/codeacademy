"""Write a program to prompt the user for hours and rate
per hour using input to compute gross pay. Pay should
be the normal rate for hours up to 40 and time-and-a-half
for the hourly rate for all hours worked above 40 hours.
Put the logic to do the computation of pay in a function
called computepay() and use the function to do the
computation. The function should return a value.
Use 45 hours and a rate of 10.50 per hour to test the
program (the pay should be 498.75). You should use input
to read a string and float() to convert the string to a
number."""

#my try was shit as fuck ew
def computepay(h,r):
    h = input("Enter hours:")
    fh = float(h)
    r = input("Enter rate:")
    fr = float(r)
    if fh <= 40:
        fp = fh * fr
        print("Pay",fp)
        return("Pay",fp)

    else:
        fp = fr * 40 + fr * 1.5 * (fh - 40)
        print("Pay",fp)
        return("Pay",fp)
computepay(10,20)

#answer was so much better i mean duh but still
def computepay(h,r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        pay = 40 * r + (h - 40) * r * 1.5
        return pay
"""or budle up the returns and insert unindent them
below the else statement"""
hrs = input("Enter hours:")
h = float(hrs)
rate = input("Input rate:")
r = float(rate)
p = computepay(h,r)
print("Pay", p)
