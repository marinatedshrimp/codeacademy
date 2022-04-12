#Marina Tanaka
'''
"Hello" if a number entered by the user is a multiple of five, 
otherwise print "Bye".
'''
#below the typeHello program is the complete the code challenge and a while loop

num = int(input("Gimme a number: "))

if num % 5 == 0:    #check the modulo 5 of num
    print("Hello")
else:
    print("Bye")


#temp holds information temporarily so that the two values can be swapped
#Complete the following code:
x = 5
y = 10

temp = x
x = y 
y = temp
print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))

#while loop
while num % 5 != 0:
    print("I am gonna keep adding one until {} becomes a multiple of 5".format(num))
    num += 1
print("okay cool now you have {} it's a good number".format(num))