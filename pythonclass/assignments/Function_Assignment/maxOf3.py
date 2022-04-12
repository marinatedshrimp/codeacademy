#Write a Python function to find the Max of three numbers.

def max(a, b, c):
    if (a >= b) and (a >= c):
        maxnum = a
    elif (b >= a) and (b >= a):
        maxnum = b
    elif (c >= a) and (c >= b):
        maxnum = c
    return maxnum
    #cant print inside function
    

x = 10
y = 12
z = 78

print(max(x,y,z))

