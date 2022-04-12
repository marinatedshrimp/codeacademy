import math
from tkinter import *
#combine html,css,python,flask(sqlite)

root =Tk()
root.title("simple calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10) #so it spans all 3 boxes below it

#enter number
def bCLick(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def bClear():
    e.delete(0, END)

def bAdd():
    fnum = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(fnum) #made fnum a global var aka can be used across func
    e.delete(0, END) #clear entry so u can put in the next value

def bEquals():
    s_num = e.get() #grabs whatever is in the textbox
    e.delete(0, END) #just in case there's smth in the textbox

    """
    e.insert(0, f_num + int(s_num)) #we needed f_num to be global so we could access it here
    #only works for addition so it needs to be diff for +*-/
    #if statements to make it work?
    """
    if (math == "add"):
        e.insert(0, f_num + int(s_num))
    elif (math == "sub"):
        e.insert(0, f_num - int(s_num))
    elif (math == "multi"):
        e.insert(0, f_num * int(s_num)) 
    elif (math == "div"):
        e.insert(0, f_num / int(s_num))

#make color change when hovering



def bSub():
    fnum = e.get()
    global f_num #no need to change var name
    global math
    math = "sub" #only need to change this fromt he add func
    f_num = int(fnum)
    e.delete(0, END)

def bMulti():
    fnum = e.get()
    global f_num
    global math
    math = "multi"
    f_num = int(fnum)
    e.delete(0, END)

def bDiv():
    fnum = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(fnum)
    e.delete(0, END)

#define buttons
b1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: bCLick(1))
b2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: bCLick(2))
b3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: bCLick(3))
b4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: bCLick(4))
b5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: bCLick(5))
b6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: bCLick(6))
b7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: bCLick(7))
b8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: bCLick(8))
b9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: bCLick(9))
b0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: bCLick(0))
bPlus = Button(root, text = "+", padx = 39, pady = 20, command = bAdd) #no () cuz were not passing anything
bEquals = Button(root, text = "=", padx = 101, pady = 20, command = bEquals)
bClear = Button(root, text = "Clear", padx = 90, pady = 20, command = bClear) #no need for ()
bSub = Button(root, text = "-", padx = 41, pady = 20, command = bSub) 
bMulti = Button(root, text = "*", padx = 40, pady = 20, command = bMulti) 
bDiv = Button(root, text = "/", padx = 40, pady = 20, command = bDiv) 

#put button on screen
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)

b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)

b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)

b0.grid(row = 4, column = 0)
bClear.grid(row = 4, column = 1, columnspan = 2)

bEquals.grid(row = 5, column = 1, columnspan = 2)
bPlus.grid(row = 5, column = 0)

bSub.grid(row = 6, column = 0)
bMulti.grid(row = 6, column = 1)
bDiv.grid(row = 6, column = 2)

root.mainloop()

