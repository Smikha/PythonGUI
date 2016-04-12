from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from subprocess import call

'''
Stevan Mikha
200 300 944
GUI For Point of Sale Terminal
Capstone Project 2016

This program will create a GUI to simulate a POS terminal. The user will be able
to buy items, see their total, print their items to a text based file, and execute a C file to
send the file over Bluetooth to their Android phone.
'''


'''
This class incorporates all the functions required to produce the GUI
First, I will create the total tab
Next, I will create the buttons themselves and assign them the functions to look for when pressed
Next, I will place the buttons onto the screen/grid
Next, I will create the tasks for which the buttons will perform when pressed
Lastly, I will call my C program and execute when a user signals to print the receipt
'''

class SaleTerminal:

    def __init__(self, master):
        self.master = master
        master.title("Point of Sale")
# Initializing the counter so that the user can see their sum for their items purchased
        self.total = 0
        self.entered_number = 0
# Creating the box and total area for an active sum update
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")
# Testing the method of inputting how much your item should cost, but will take this out if not working by PRoject Demo
        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
# Here I create the vast majority of the buttons, I set them to look for their respective functions "Bx" and
# execute when the left click on the mouse is performed on the specific button
        self.B1 = Button(master, text="Coca-Cola", command=lambda: self.update("B1"))
        self.B2 = Button(master, text="Lays", command=lambda: self.update("B2"))
        self.B3 = Button(master, text="MJ Thriller", command=lambda: self.update("B3"))
        self.B4 = Button(master, text="Time Mag", command=lambda: self.update("B4"))
        self.B5 = Button(master, text="USB", command=lambda: self.update("B5"))
        self.B6 = Button(master, text="Star Wars", command=lambda: self.update("B6"))
        self.B7 = Button(master, text="Total", command=lambda: self.update("B7"))
        self.B8 = Button(master, text="Print", command=lambda: self.update("B8"))
        self.subtract_button = Button(master, text="Save $10", command=lambda: self.update("subtract10"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))


        # Here I set the layout for the buttons, I can specify where on the main window I would like everything.

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.B1.grid(row=2, column=0)
        self.B2.grid(row=2, column=1)
        self.B3.grid(row=3, column=0)
        self.B4.grid(row=3, column=1)
        self.B5.grid(row=3, column=2)
        self.B6.grid(row=2, column=2)
        self.B7.grid(row=1, column=3)
        self.B8.grid(row=3, column=4)

        self.subtract_button.grid(row=3, column=3)
        self.reset_button.grid(row=2, column=3, sticky=W+E)


# For the input of value for specific items in the box provided
    def validate(self, new_text):

        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True


# These functions help define what a button does when pressed
    def update(self, method):
# Create or Append a text file wit hthe given name
        f = open("Receipt.txt", "a")
# If B1 is pressed, then add the price of B1 to the total and print this string to the text file
#This process is duplicated for each button given their unique message and price
        if method == "B1":
            #self.total += self.entered_number
            self.total += 2.76


            print("Coca-Cola (12 Pack)             $2.76", file=f)
        elif method == "B2":
            self.total += 2.99

            print("Lays Classic                    $2.99", file=f)
        elif method == "B3":
            self.total += 7.00

            print("Michael J.- Thriller            $7.00 ", file=f)
        elif method == "B4":
            self.total += 3.50

            print("Time Magazine                   $3.50", file=f)
        elif method == "B5":
            self.total += 19.99

            print("USB 3.0 Cruzer                  $19.99", file=f)
        elif method == "B6":
            self.total += 9.98

            print("Star Wars: V                    $9.98", file=f)
        elif method == "subtract10":
            self.total -= 10
            SubTot = self.total

            print("Discount                       -$10.00",file=f)
        elif method == "B7":
            roundedTotal = round(self.total, 2)


            print("\n------------------------------------ \n    Your total today is: $", roundedTotal, file=f)
            print("\n\n    Payment: Android Pay \n    Technology: Bluetooth and NFC \n    APPROVED", file=f)
            print("\n \n \n        Thank you very much.\n" "        Please come back again.", file=f)
            call(["./rpi", "args", "to", "rpi"])
            # Here we call a program called "Hello World" to execute. This program is the GCC make of the C file
            # essentialy, the IDE will create this build when you compile
        elif method == "B8":
            call(["sudo", "./helloworld", "args", "to", "helloworld"])
        elif method == "reset":
            # Here I reset the counter
            self.total = 0

            print("             KWIK-E Mart \n         ******************** \n         * 123 Evergreen Tr. * \n              * S4S 0A2 *\n         * (306) 591-0909 *\n         ********************  \n         Welcome to KWIK-E Mart\n \n \n \n------------------------------------ \n ", file=open("Receipt.txt", "w"))
        else: # reset
            self.total = 0

        roundedTot = round(self.total,2)
        self.total_label_text.set(roundedTot)
        self.entry.delete(0, END)

root = Tk()
my_gui = SaleTerminal(root)
root.mainloop()
