from tkinter import *

root =Tk()
#always need to make the root widget first


#-----LABELS-----#
#create a Label widget
label1 = Label(root, text = "hi there let's play")
label2 = Label(root, text = "do you wanna play some libby?")
label3 = Label(root, text = "?          ?")


#shove into root w pack so the window is bare min to fit text
#label1.pack()
#will keep text in the middle of screen


label1.grid(row = 0, column = 0)
#will keep it in teh left top corner
label2.grid(row = 2, column = 5)
#column = 5 would be the same as 2-4 here cuz its all relative to eachother
label3.grid(row = 1, column = 1)


#is possible to just slap the grid onto the og text but better to do the seperate way for cleanliness
label4 = Label(root, text = "hola").grid(row = 3, column = 4)


#-----BUTTON/INPUT-----#

def click():
    hello = "Hello there " + input1.get()
    label5 = Label(root, text = hello)
    label5.grid(row = 5, column = 3)

input1 = Entry(root, width = 20, bg = "pink", borderwidth = 5)
input1.grid(row = 3, column = 3)
input1.insert(0, "Enter your name: ")#0th box, text already inside box
#but it will also type out Enter your name: so u dont need it

button1 = Button(root, text = "Enter your name: ", padx = 50, pady = 20, command = click, bg = 'green', fg = "DarkOliveGreen") #not click()
button1.grid(row = 4, column = 3)
#cuz button1 is wide the text is a lot more spread out



root.mainloop()