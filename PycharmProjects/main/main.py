from tkinter import *


#This is me testing/doing tutorials in python to learn how to use the main functionality of the language
#Calc.py is the point of sale terminal 

def doNothing():
    f = open('myfile.txt', 'w')
    f.write('Hi There\n')

    print("ok")




class testButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton= Button(frame, text="File", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Exit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow THIS WORKS")



root = Tk()
a = testButtons(root)

# Menu Bar

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="Now", command=doNothing)
subMenu.add_separator()

subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="redo", command=doNothing)

# Creating the Toolbar

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT,padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


# Status Bar

status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)




def printB1(event):
    f = open('myfile.txt', 'a')
    f.write('$10.99\n')
    bill1 += 10.99
    return bill1

def printB2(event):
    f = open('myfile.txt', 'a')
    f.write('$5.99\n')
    bill2 += 5.99
    return bill2

def printB3(event):
    f = open('myfile.txt', 'a')
    f.write('$2.99\n')
    bill3 += 2.99
    return bill3

def printB4(event):
    f = open('myfile.txt', 'a')
    f.write('$29.99\n')
    bill4 += 29.99
    return bill4

def printB5(event):
    bill5=0
    f = open('myfile.txt', 'a')
    f.write('$16.99\n')
    return bill5 + 16.99


def printB6(event):

    f = open('myfile.txt', 'a')
    f.write(sumTotal)


topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

middleFrame = Frame(root)
middleFrame.pack(side=TOP)

b1 = Button(topFrame, text="B1", foreground="red")
b1.bind("<Button-1>", printB1)
#Must change topFrame to root if wanting to use grids
#b1.grid(row=0, sticky=W)

b2 = Button(topFrame, text="B2", background="green")
b2.bind("<Button-1>", printB2)
b3 = Button(topFrame, text="B3", fg="blue")
b3.bind("<Button-1>", printB3)
b4 = Button(bottomFrame, text="B4", fg="red")
b4.bind("<Button-1>", printB4)
b5 = Button(middleFrame, text="B5", fg="yellow")
b5.bind("<Button-1>", printB5)
b6 = Button(middleFrame, text="Total", fg="yellow")
b6.bind("<Button-1>", printB6)

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)



'''
one = Label(root, text="one", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="red", fg="white")
#Fill lets the button wrap in the horizontal direction when you stretch the window
two.pack(fill=X)
'''
'''
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

#Sticky places to the EAST, so right alligned
label_1.grid(row=0, sticky=E)
label_2.grid(row=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root, text="Remember")
c.grid(columnspan=2)
'''


'''
def printName(event):
    print("hello")

#TWO DIFFERENT WAYS
#button_1 = Button(root, text="Print Name", command=printName)
#button_1.pack()


b1 = Button(root, text="Print Name")
b1.bind("<Button-1>", printName)
b1.pack()

'''


# ******
#This is for clicking in a black space, not a button!!
'''
def leftClick(event):
    print("Left")

def middleClick(event):
    print("middle")

def rightClick(event):
    print("Right")

frame = Frame(root, width = 300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", rightClick)
frame.bind("<Button-3>", middleClick)

frame.pack()
'''



root.mainloop()
