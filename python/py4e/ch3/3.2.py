hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("stop putting in words put in numbers like a normal person")
    quit()
#rate worked over 40hrs is 150%
if fh <= 40:
    pay = fh * fr
    print(pay)
else:
    pay = fr * 40 + (fh-40) * fr * 1.5
    print("Pay:",pay)
