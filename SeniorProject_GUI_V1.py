#exact change only
import math
import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import *
from time import sleep
import Vending_module as Vm

class RvmApp(tk.Tk):
    global btnCanDrinkImage  # needed to save the image if not garbage collector will remove it
    global btnBottledDrinkImage  # needed to save the image if not garbage collector will remove it

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Arial', size=18, weight="bold")

        ##############This allows the program to launch in full screen
        self.attributes('-fullscreen', True)

        #This allows to press 'esc' key to exit full screen
        #If you want to close the program instead remove
        #self.attributes('-fullscreen', False) and add
        #self.destroy()
        self.bind('<Escape>', lambda e: self.attributes('-fullscreen', False))

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        pages = [StartPage, RecyclePage, RecycleScan, PurchasePage]  # pages holds all the windows
        for F in pages:  # for loop instantiates windows and places them
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="lightgreen", text="Please make a selection.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Recycle",
                            command=lambda: controller.show_frame("RecyclePage"))
        button2 = tk.Button(self, text="Purchase a Drink",
                            command=lambda: controller.show_frame("PurchasePage"))
        button1.pack()
        button2.pack()


class RecyclePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="lightgreen", text="What would you like to recycle?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Plastic Bottle",
                            command=lambda: [controller.show_frame("RecycleComplete"), openDoor()])
        button2 = tk.Button(self, text="Aluminum Can",
                            command=lambda: [controller.show_frame("RecycleScan"), Recycling()])
        button = tk.Button(self, text="Return to Main menu",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
        button.pack()


class RecycleScan(tk.Frame):  # window after the recycle button is clicked
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="White", text="Please scan your recycleables with the scanner.",
                         font=controller.title_font)
        label.pack(fill="x")
        check_sensor()  # used to scan the recyclable
        openDoor()  # used to open the coresponding door
        command = lambda: controller.show_frame("RecycleComplete")


class RecycleComplete(tk.Frame):  # window after the RecycleScan Window
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="White", text="Thank you for recycling.", font=controller.title_font)
        label.pack(fill="x")
        # create timer code so the frame will wait 3 seconds
        command = lambda: controller.show_frame("StartPage")


class PurchasePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="lightgreen", text="What would you like to purchase?", font=controller.title_font)
        label.grid(row = 0, column = 20, pady=10)

        PlasticBottleButton = tk.Button(self, text="Bottled Beverage",
                                        command=lambda: controller.show_frame(
                                            ""))  # need to add bottle servo dispensing code
        PlasticBottleButton.grid(row=2, column=3)

        CannedDrinkButton = tk.Button(self, text="Canned Beverage", bg="white", width="250",
                                      command=lambda: controller.show_frame(
                                          ""))  # need to add canned servo dispensing code
        CannedDrinkButton.grid(row=4, column=3)
        CheckoutButton = tk.Button(self, text="Checkout Here",
                                        command=lambda: controller.show_frame("CheckoutPage"))
        CheckoutButton.grid(row=4, column=40)

class CheckoutPage(tk.Frame):  #after purchase window
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, bg="White", text="Please you may insert exact change now.", font=controller.title_font)
        label.pack(fill="x")
        # display the total
        # as they insert subtract in money method
        # create timer code so the frame will wait 3 seconds
        command = lambda: controller.show_frame("StartPage")

#========================== photo instantiation ==============================#

        ##########BottledDrinkButtonPhoto
        btnBottledDrinkImage = PhotoImage(file="bottledDrinkButton.gif")
        ##########This is a form of 'concatenate' and allows to place the image in the button
        PlasticBottleButton.config(image=btnBottledDrinkImage, compound=BOTTOM)
        PlasticBottleButton.image = btnBottledDrinkImage


        # CannedDrinkButtonPhoto
        btnCanDrinkImage = PhotoImage(file="canDrinkButton.gif")
        ##########This is a form of 'concatenate' and allows to place the image in the button
        CannedDrinkButton.config(image=btnCanDrinkImage, compound=BOTTOM)
        CannedDrinkButton.image = btnCanDrinkImage

        counter = 0

        def counter_label(label):
            counter = 0

            def count():
                global counter
                counter += 1

        command = lambda: controller.show_frame("CheckoutWindow")

#-------------- Money calculation method-----------------#
def Money():
    plues = 0
    #If a quarter is read
    #if (pulse == 1)
        #do something
    #if a dime is read
    #if (pulse == 2)
        #do something
    #if a nickel is read
    #if (pulse == 3)
        #do something
    #if a dime is read
    #if (pulse == 4)
        #do something
    #if a penny is read
    #if (pulse == 5)
        #do something
    total = 0
    discount = 0


# =============== Recycling methods ====================== #
# ======================================================== #
def Recycling():  # when recyling button is pushed on the main menu
    check_sensor()  # this will
    openDoor()
    closeDoor()


def openDoor():
    print("opening recycling door")
    Vm.servo1_motor()


def check_sensor():
    print("Checking for objects")
    print("Nothing is detected")
    closeDoor()


def closeDoor():
    print("Closing door")


def dispense_drink(drink):
    print("dispensing " + str(drink))


if __name__ == "__main__":
    app = RvmApp()
    app.title("Recycling Vending Machine")
    app.geometry("425x150")
    app.mainloop()