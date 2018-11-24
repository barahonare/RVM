
import math
import RPi.GPIO as GPIO #uncomment when running on pi
import time
import tkinter as tk
from Selling_Module import POS
from Selling_Module import Stepper_Motor as STM
from Selling_Module import CoinAcceptor as Coin
from Selling_Module import Metal_Detecter as MD
#import PlasticDoorServo as PDS
from tkinter import font as tkfont
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import *
from time import sleep

Final = 0.0

def setFinal(amount):
    global Final
    Final = amount

def updateLabel(Label,value):
    Label.config(text = value)


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
        self.pages = [MainMenu, RecycleMenu, CheckoutMenu, PurchaseMenu, ScanningStage_OpenAlumDoor, OpeningPlasticDoor]
        #we are using a for loop to instantiate new windows as we develop more windows
        #but the window names must be put into the self.pages = [] in order for it to
        #find the windows you are traversing to
        for F in self.pages:
            page_name = F.__name__
            self.frame = F(parent=self.container, controller = self)
            self.frame.config(background = 'black') # Configuration of the frame before placin in frame dictionary
            self.frames[page_name] = self.frame
            #This allows us to put the frames on a stack and pull the frame we are viewing on top
            self.frame.grid(row =0, column = 0, sticky = 'nsew')
        self.show_frame("MainMenu")
    #This method will show the frame for the current page name
    def show_frame(self, page_name):
        self.frame = self.frames[page_name]
        self.frame.tkraise()
    def get_page(self,classname):
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None


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
        self.RecycleSelectionButton = tk.Button(self, text="",command = lambda: [controller.show_frame("RecycleMenu"), print("moving to recycle menu")])
        self.PurchaseSelectionButton = tk.Button(self, text = "", command = lambda: [controller.show_frame("PurchaseMenu"), print("moving to purchase menu")])
        #This puts the buttons onto the frame
        self.RecycleSelectionButton.pack(side = "left")
        self.PurchaseSelectionButton.pack(side = "right")
        #Adjusts the size of the buttons
        #self.RecycleSelectionButton.config(height=400, width=250)
        #self.PurchaseSelectionButton.config(height=300, width=250)
        #This allows us to put images into the buttons
        self.RecycleImageForButton = PhotoImage(file="RecycleButton_image.gif")
        self.RecycleSelectionButton.config(image=self.RecycleImageForButton, compound = "bottom")
        self.RecycleSelectionButton.image = self.RecycleImageForButton
        self.PurchaseImageForButton = PhotoImage(file="PurchaseButton_image.gif")
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
        self.CanSelectionButton = tk.Button(self, text="",command = lambda: [controller.show_frame("ScanningStage_OpenAlumDoor"),POS.CanDiscountMethod(self), print("moving to ScanningStage_OpenAlumDoor")])
        self.BottleSelectionButton = tk.Button(self, text = "", command = lambda: [controller.show_frame("OpeningPlasticDoor"),POS.WaterDiscountMethod(self), print("opening plastic door")])
        self.ReturnSelectionButton = tk.Button(self, text = "", command = lambda: [controller.show_frame("MainMenu"),POS.ResetPrice(self), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.CanSelectionButton.pack()
        self.BottleSelectionButton.pack()
        self.ReturnSelectionButton.pack()
        #This allows us to put images into the buttons
        self.AlumImageForButton = PhotoImage(file="RecycleAluminum_image.gif")
        self.CanSelectionButton.config(image=self.AlumImageForButton, compound = "bottom")
        self.CanSelectionButton.image = self.AlumImageForButton
        self.PlasticImageForButton = PhotoImage(file="RecyclePlastic_image.gif")
        self.BottleSelectionButton.config(image=self.PlasticImageForButton, compound = "bottom")
        self.BottleSelectionButton.image = self.PlasticImageForButton
        self.BackupImageForButton = PhotoImage(file="BackupButton_image.gif")
        self.ReturnSelectionButton.config(image=self.BackupImageForButton, compound = "bottom")
        self.ReturnSelectionButton.image = self.BackupImageForButton

class ScanningStage_OpenAlumDoor(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.Scanninglabel = tk.Label(self, bg = 'black',fg = 'white', text = "Press the scanning button and then hold your can up to the sensor for a safety scan", font = controller.title_font)
        #This puts the label on the frame
        self.Scanninglabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.ScanningButton = tk.Button(self, text = "", command = lambda: [MD.ScanToOpen(self)])
        self.ReturnSelectionButton = tk.Button(self, text = "", command = lambda: [controller.show_frame("RecycleMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.ScanningButton.pack()
        self.ReturnSelectionButton.pack()
        #add images into the buttons
        self.BackupImageForButton = PhotoImage(file="BackupButton_image.gif")
        self.ReturnSelectionButton.config(image=self.BackupImageForButton, compound = "bottom")
        self.ReturnSelectionButton.image = self.BackupImageForButton
        self.ScanningImageForButton = PhotoImage(file="StartScanningButton_image.gif")
        self.ScanningButton.config(image=self.ScanningImageForButton, compound = "bottom")
        self.ScanningButton.image = self.ScanningImageForButton

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
        self.ReturnSelectionButton = tk.Button(self, text = "return to main", command = lambda: [controller.show_frame("RecycleMenu"), print("moving to main menu")])
        self.PlasticDoorButton = tk.Button(self, text = "push to open the plastic door", command = lambda: PDS.PlasticDoorOpen(self))
        #This puts the buttons onto the frame
        self.ReturnSelectionButton.pack()
        self.PlasticDoorButton.pack()
        #adds images into the buttons
        self.BackupImageForButton = PhotoImage(file="BackupButton_image.gif")
        self.ReturnSelectionButton.config(image=self.BackupImageForButton, compound = "bottom")
        self.ReturnSelectionButton.image = self.BackupImageForButton


    #call plastic door opeing here

class PurchaseMenu(tk.Frame):
    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        checkOutFrame = controller.get_page('CheckoutMenu')
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Would you like to buy a can of soda or bottle of water?", font = controller.title_font)
        self.TotalLabel = tk.Label(self, bg = 'black',fg = 'white', text = "Your total will display here as you add items", font = controller.title_font)
        self.Cartlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Your Final value is " '$%s ' "Your discount was "'$%s'%(POS.FinalPrice,POS.Discount), font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)  
        self.Cartlabel.pack(side="top", fill="x", pady=10)
        self.TotalLabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.AddSodaButton = tk.Button(self, text="",command = lambda:[ POS.AddPriceOfSoda(self),POS.SodaSelectedMethod(self)])
        self.AddWaterButton = tk.Button(self, text = "", command = lambda: [POS.AddPriceOfWater(self),POS.WaterSelectedMethod(self)])
        self.ReturnSelectionButton = tk.Button(self, text = "",
                    command = lambda: [controller.show_frame("MainMenu"),
                        POS.ResetPrice(self), print("moving to main menu")])
        self.CheckoutSelectionButton = tk.Button(self, text = "", 
                    command = lambda: [controller.show_frame("CheckoutMenu")
                        , checkOutFrame.FinalTotalLabel.config(text = ('$%s' %POS.FinalPrice))
                        , print("moving to checkout menu")])
        self.MinusSodaFromTotalButton = tk.Button(self, text = "", command = lambda: [POS.SubtractPriceOfSoda(self), print("Removing price of soda from total"),POS.SodaSelectedMethod(self)])
        self.MinusWaterFromTotalButton = tk.Button(self, text = "", command = lambda: [POS.SubtractPriceOfWater(self), print("Removing price of Water from total"),POS.WaterSelectedMethod(self)])
        self.RecycleOnPurchaseWindowButton = tk.Button(self, text = "", command = lambda: [POS.DiscountEnablerMethod(self),controller.show_frame("RecycleMenu"), print("Moving to recycle page")])
        #This puts the buttons onto the frame
        self.AddSodaButton.pack(side="left")
        self.MinusWaterFromTotalButton.pack(side ="right")
        self.AddWaterButton.pack(side ="right")
        self.MinusSodaFromTotalButton.pack(side="left")
        self.CheckoutSelectionButton.pack()
        self.ReturnSelectionButton.pack()
        self.RecycleOnPurchaseWindowButton.pack(side = "bottom")
        #This puts images inside the buttons
        self.AddCanImageForButton = PhotoImage(file="AddSodaButton_image.gif")
        self.AddBottleImageForButton = PhotoImage(file="AddWaterButton_image.gif")
        self.RemoveCanImageForButton = PhotoImage(file="RemoveSodaButton_image.gif")
        self.RemoveBottleImageForButton = PhotoImage(file="RemoveWaterButton_image.gif")
        self.AddSodaButton.config(image=self.AddCanImageForButton, compound = "bottom")
        self.AddSodaButton.image = self.AddCanImageForButton
        self.AddWaterButton.config(image=self.AddBottleImageForButton, compound = "bottom")
        self.AddWaterButton.image = self.AddBottleImageForButton
        self.MinusSodaFromTotalButton.config(image=self.RemoveCanImageForButton, compound = "bottom")
        self.MinusSodaFromTotalButton.image = self.RemoveCanImageForButton
        self.MinusWaterFromTotalButton.config(image=self.RemoveBottleImageForButton, compound = "bottom")
        self.MinusWaterFromTotalButton.image = self.RemoveBottleImageForButton
        self.BackupImageForButton = PhotoImage(file="BackupButton_image.gif")
        self.ReturnSelectionButton.config(image=self.BackupImageForButton, compound = "bottom")
        self.ReturnSelectionButton.image = self.BackupImageForButton
        self.CheckoutImageForButton = PhotoImage(file="Checkout_image.gif")
        self.CheckoutSelectionButton.config(image=self.CheckoutImageForButton, compound = "bottom")
        self.CheckoutSelectionButton.image = self.CheckoutImageForButton
        self.RecycleOnPurchaseImageForButton = PhotoImage(file="DiscountButton_image.gif")
        self.RecycleOnPurchaseWindowButton.config(image=self.RecycleOnPurchaseImageForButton, compound = "bottom")
        self.RecycleOnPurchaseWindowButton.image = self.RecycleOnPurchaseImageForButton

class CheckoutMenu(tk.Frame):
    global Final

    #initalizes the class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #This Creates the labels for the frame
        self.selectionlabel = tk.Label(self, bg = 'black',fg = 'white', text = "Please insert exact change into the coin acceptor please", font = controller.title_font)
        self.coinlabeltest = tk.Label(self, bg = 'black',fg = 'white', text = "This will get updated", font = controller.title_font)
        self.FinalTotalLabel = tk.Label(self, bg = 'black', fg = 'white', text = "You owe $%s" %POS.FinalPrice, font = controller.title_font)
        #This puts the label on the frame
        self.selectionlabel.pack(side="top", fill="x", pady=10)
        self.coinlabeltest.pack(side="top", fill="x", pady=10)
        self.FinalTotalLabel.pack(side="top", fill="x", pady=10)
        #This creates the buttons for the frame
        self.CoinActivatorSelectionButton = tk.Button(self, text = "", command = lambda: [Coin.ActivateCoinAcceptor(self)])
        self.ReturnSelectionButton = tk.Button(self, text = "", command = lambda: [controller.show_frame("PurchaseMenu"), print("moving to main menu")])
        self.ReturnToPurchaseSelectionButton = tk.Button(self, text = "", command = lambda: [controller.show_frame("PurchaseMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.CoinActivatorSelectionButton.pack()
        self.ReturnToPurchaseSelectionButton.pack()
        self.ReturnSelectionButton.pack()
        #puts the images inside the buttons
        self.BackupImageForButton = PhotoImage(file="BackupButton_image.gif")
        self.ReturnSelectionButton.config(image=self.BackupImageForButton, compound = "bottom")
        self.ReturnSelectionButton.image = self.BackupImageForButton
        self.PayingImageForButton = PhotoImage(file="StartPayingButton_image.gif")
        self.CoinActivatorSelectionButton.config(image=self.PayingImageForButton, compound = "top")
        self.CoinActivatorSelectionButton.image = self.PayingImageForButton
        self.PurchaseMenuImageForButton = PhotoImage(file="PurchaseMenuButton_image.gif")
        self.ReturnToPurchaseSelectionButton.config(image=self.PurchaseMenuImageForButton, compound = "bottom")
        self.ReturnToPurchaseSelectionButton.image = self.PurchaseMenuImageForButton
    
        
    # def updatePriceLabel(self,amount):
    #     self.FinalTotalLabel.config(text = 'New label')

        
#call method to detect coin acceptor then return to main menu when your are done
#>>>>>>> RVM-2.0:SeniorProject_GUI_V2.py
if __name__ == "__main__":
    app = RvmMainApp()
    app.title("recycling vending machine")
    app.geometry("425x150")
    app.mainloop()