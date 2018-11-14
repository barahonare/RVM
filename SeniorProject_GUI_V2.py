#---GUI todo list ---- #
#add servo done
#add metal detector code done
#metal detector - figure out how to send a boolean done
#add sleep mode / still integrating with rangefinder

#----------anthony / jose
#add coin acceptor done
#add discounts
#add images to recycle window
#photo shop images to prevent copywrite stuff

#--------------notes--------------
#counter to detect how many sodas or waters are on the cart
#coin acceptor calling stepper for dispening if total is 0



import math
import RPi.GPIO as GPIO #uncomment when running on pi
import time
import tkinter as tk
# import Vending_module as Vm #import the door source file
from Selling_Module import POS
from Selling_Module import Stepper_Motor as STM
from tkinter import font as tkfont
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import *
from time import sleep


class RvmMainApp(tk.Tk):
    #initalizes the class
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #sets the font title
        self.title_font = tkfont.Font(family='Arial', size = 18, weight="bold")
        #allows the program to launch in full screen
        self.attributes('-fullscreen', True)
        #press escape to minimize program / if close instead change self.attributes('-fullscreen',False) to self.destroy()
        self.bind('<Escape>', lambda e: self.attributes('-fullscreen', False))
        #This creates a container to hold all of the frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        #This creates frames to store into the container
        self.frames = {}
        self.pages = [MainMenu, RecycleMenu, PurchaseMenu, CheckoutMenu, ScanningStage, OpeningPlasticDoor, OpeningAluminumDoor]
        #we are using a for loop to instantiate new windows as we develop more windows
        #but the window names must be put into the self.pages = [] in order for it to
        #find the windows you are traversing to
        for F in self.pages:
            page_name = F.__name__
            self.frame = F(parent=self.container, controller = self)
            self.frames[page_name] = self.frame
            #This allows us to put the frames on a stack and pull the frame we are viewing on top
            self.frame.grid(row =0, column = 0, sticky = 'nsew')
        self.show_frame("MainMenu")
    #This method will show the frame for the current page name
    def show_frame(self, page_name):
        self.frame = self.frames[page_name]
        self.frame.tkraise()

class MainMenu(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Would you like to Recycle or Purchase an item?", font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.RecycleSelectionButton = tk.Button(self, text="Recycle Here",command = lambda: [controller.show_frame("RecycleMenu"), print("moving to recycle menu")])
        self.PurchaseSelectionButton = tk.Button(self, text = "Purchase Here", command = lambda: [controller.show_frame("PurchaseMenu"), print("moving to purchase menu")])
        #This puts the buttons onto the frame
        self.RecycleSelectionButton.pack(side = "left")
        self.PurchaseSelectionButton.pack(side = "right")
        #Adjusts the size of the buttons
        #self.RecycleSelectionButton.config(height=400, width=250)
        #self.PurchaseSelectionButton.config(height=300, width=250)
        #This allows us to put images into the buttons
        self.RecycleImageForButton = PhotoImage(file="Recycle__Image.gif")
        self.RecycleSelectionButton.config(image=self.RecycleImageForButton, compound = "bottom")
        self.RecycleSelectionButton.image = self.RecycleImageForButton
        self.PurchaseImageForButton = PhotoImage(file="Purchase_Image.gif")
        self.PurchaseSelectionButton.config(image=self.PurchaseImageForButton, compound = "bottom")
        self.PurchaseSelectionButton.image = self.PurchaseImageForButton

class RecycleMenu(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Would you like to Recycle a Aluminum can or Plastic bottle?", font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.CanSelectionButton = tk.Button(self, text="Aluminum Can",command = lambda: [controller.show_frame("ScanningStage"), print("moving to Scanning menu")])
        self.BottleSelectionButton = tk.Button(self, text = "Plastic bottle", command = lambda: [controller.show_frame("OpeningPlasticDoor"), print("opening plastic door")])
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu", command = lambda: [controller.show_frame("MainMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.CanSelectionButton.pack()
        self.BottleSelectionButton.pack()
        self.ReturnSelectionButton.pack()

class ScanningStage(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Please hold your can up to the sensor for a safety scan", font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.CanOpenDoorButton = tk.Button(self, text = "Move to can door open", command = lambda: [controller.show_frame("OpeningAluminumDoor"), print("moving to aluminum door menu")])
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu", command = lambda: [controller.show_frame("MainMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.CanOpenDoorButton.pack()
        self.ReturnSelectionButton.pack()
    #call scanner method code here

class OpeningPlasticDoor(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.OpeningDoorPromptlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Please wait as the safety plastic door is opening", font = controller.title_font)
        #This puts the label on the frame
        self.OpeningDoorPromptlabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        #note: when servo code is developed we can undo
        #the button and just insert the code so the main
        #menu frame will appear when it is done closing
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu", command = lambda: [controller.show_frame("MainMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.ReturnSelectionButton.pack()


    #call plastic door opeing here

class OpeningAluminumDoor(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Please wait as the safety aluminum door is opening", font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu", command = lambda: [controller.show_frame("MainMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.ReturnSelectionButton.pack()
    #call aluminum door opeing here

class PurchaseMenu(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Would you like to buy a can of soda or bottle of water?", font = controller.title_font)
        self.TotalLabel = tk.Label(self, bg = 'black',fg = 'white', text = "Your total will display here", font = controller.title_font)
        self.Discountlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Your discount will be displayed here", font = controller.title_font)
        self.Cartlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Your cart amount will be displayed here", font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)        
        self.Discountlabel.pack(side="top", fill="x", pady=10)
        self.Cartlabel.pack(side="top", fill="x", pady=10)
        self.TotalLabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.SodaSelectionButton = tk.Button(self, text="Soda",command = lambda: POS.AddPriceOfSoda(self))
        self.WaterSelectionButton = tk.Button(self, text = "Water", command = lambda: POS.AddPriceOfWater(self))
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu",
                    command = lambda: [controller.show_frame("MainMenu"),
                        POS.ResetPrice(self), print("moving to main menu")])
        self.CheckoutSelectionButton = tk.Button(self, text = "Checkout Here", 
                    command = lambda: [controller.show_frame("CheckoutMenu"),
                        POS.ResetPrice(self), print("moving to checkout menu")])
        self.MinusSodaFromTotalButton = tk.Button(self, text = "- Soda", command = lambda: [POS.SubtractPriceOfSoda(self), print("Removing price of soda from total")])
        self.MinusWaterFromTotalButton = tk.Button(self, text = "- Water", command = lambda: [POS.SubtractPriceOfWater(self), print("Removing price of Water from total")])
        self.RecycleOnPurchaseWindowButton = tk.Button(self, text = "Click me to recycle for discount", command = lambda: [controller.show_frame("RecycleMenu"), print("Moving to recycle page")])
        #This puts the buttons onto the frame
        self.SodaSelectionButton.pack(side="left")
        self.MinusWaterFromTotalButton.pack(side ="right")
        self.WaterSelectionButton.pack(side ="right")
        self.MinusSodaFromTotalButton.pack(side="left")
        self.ReturnSelectionButton.pack()
        self.CheckoutSelectionButton.pack()
        self.RecycleOnPurchaseWindowButton.pack(side = "bottom")
        #This puts images inside the buttons
        # self.CanImageForButton = PhotoImage(file="candrinkbutton.gif")
        # self.BottleImageForButton = PhotoImage(file="bottleddrinkbutton.gif")
        # self.SodaSelectionButton.config(image=self.CanImageForButton, compound = "bottom")
        # self.SodaSelectionButton.image = self.CanImageForButton
        # self.WaterSelectionButton.config(image=self.BottleImageForButton, compound = "bottom")
        # self.WaterSelectionButton.image = self.BottleImageForButton


class CheckoutMenu(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Please insert exact change into the coin acceptor please", font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.Stepper1ForwardButton = tk.Button(self, text = "test if the stepper1 moves forward", command = lambda: [STM.Stepper1Forward(self), print("turing on the stepper1 forwards now")])
        self.Stepper1BackwardsButton = tk.Button(self, text = "test if the stepper1 moves backward", command = lambda: [STM.Stepper1Backwards(self), print("turing on the stepper1 backwards now")])
        self.Stepper2ForwardButton = tk.Button(self, text = "test if the stepper2 moves forward", command = lambda: [STM.Stepper2Forward(self), print("turing on the stepper2 forwards now")])
        self.Stepper2BackwardsButton = tk.Button(self, text = "test if the stepper2 moves backward", command = lambda: [STM.Stepper2Backwards(self), print("turing on the stepper2 backwards now")])
        self.ReturnToPurchaseSelectionButton = tk.Button(self, text = "Return to the Purchase menu", command = lambda: [controller.show_frame("PurchaseMenu"), print("moving to Purchase menu")])
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu", command = lambda: [controller.show_frame("MainMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.Stepper1ForwardButton.pack()
        self.Stepper1BackwardsButton.pack()
        self.Stepper2ForwardButton.pack()
        self.Stepper2BackwardsButton.pack()
        self.ReturnToPurchaseSelectionButton.pack()
        self.ReturnSelectionButton.pack()
        
#call method to detect coin acceptor then return to main menu when your are done
#>>>>>>> RVM-2.0:SeniorProject_GUI_V2.py
if __name__ == "__main__":
    app = RvmMainApp()
    app.title("recycling vending machine")
    app.geometry("425x150")
    app.mainloop()