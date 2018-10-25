#---GUI todo list ---- #
#add servo
#add metal detector code
#metal detector - figure out how to send a boolean
#add sleep mode

#----------anthony / jose
#add coin acceptor
#add discounts
#add images to recycle window
#photo shop images to prevent copywrite stuff

#--------------notes--------------
#counter to detect how many sodas or waters are on the cart
#coin acceptor calling stepper for dispening if total is 0
#not enough pins... have 17 gpio pins
#servo = 3 pins each / touchscreen = 2 pins
#stepper = 4 pins each / coin acceptor = 3 pins


import math
import RPI.GPIO as GPIO #uncomment when running on pi
import time
import tkinter as tk
#import Vending_module as Vm #import the door source file
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
        self.SodaSelectionButton = tk.Button(self, text="Soda",command = lambda: self.AddPriceOfSoda())
        self.WaterSelectionButton = tk.Button(self, text = "Water", command = lambda: self.AddPriceOfWater())
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu", command = lambda: [controller.show_frame("MainMenu"), print("moving to main menu")])
        self.CheckoutSelectionButton = tk.Button(self, text = "Checkout Here", command = lambda: [controller.show_frame("CheckoutMenu"), print("moving to checkout menu")])
        self.MinusSodaFromTotalButton = tk.Button(self, text = "- Soda", command = lambda: [self.SubtractPriceOfSoda(), print("Removing price of soda from total")])
        self.MinusWaterFromTotalButton = tk.Button(self, text = "- Water", command = lambda: [self.SubtractPriceOfWater(), print("Removing price of Water from total")])
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
        self.CanImageForButton = PhotoImage(file="candrinkbutton.gif")
        self.BottleImageForButton = PhotoImage(file="bottleddrinkbutton.gif")
        self.SodaSelectionButton.config(image=self.CanImageForButton, compound = "bottom")
        self.SodaSelectionButton.image = self.CanImageForButton
        self.WaterSelectionButton.config(image=self.BottleImageForButton, compound = "bottom")
        self.WaterSelectionButton.image = self.BottleImageForButton
        
        #-Buissness methods and variables-#
        self.Price = 0
    #method to add the price of a soda to the total
    def AddPriceOfSoda(self):
        self.Price += .25
        #updates the label containing the total
        self.Cartlabel.config(text = self.Price)
        print("adding soda")
    #method to add the price of a water to the total
    def AddPriceOfWater(self):
        self.Price += 1.00
        #updates the label containing the total
        self.Cartlabel.config(text = self.Price)
        print("adding water")
    #method to add the price of a soda to the total
    def SubtractPriceOfSoda(self):
        self.Price -= .25
        #updates the label containing the total
        self.Cartlabel.config(text = self.Price)
        print("Subtracting soda")
    #method to add the price of a water to the total
    def SubtractPriceOfWater(self):
        self.Price -= 1.00
        #updates the label containing the total
        self.Cartlabel.config(text = self.Price)
        print("Subtracting water")

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
        self.Stepper1ForwardButton = tk.Button(self, text = "test if the stepper1 moves forward", command = lambda: [self.Stepper1Forward(), print("turing on the stepper1 forwards now")])
        self.Stepper1BackwardsButton = tk.Button(self, text = "test if the stepper1 moves backward", command = lambda: [self.Stepper1Backwards(), print("turing on the stepper1 backwards now")])
        #self.Stepper2ForwardButton = tk.Button(self, text = "test if the stepper2 moves forward", command = lambda: [self.Stepper2Forward(), print("turing on the stepper2 forwards now")])
        #self.Stepper2BackwardsButton = tk.Button(self, text = "test if the stepper2 moves backward", command = lambda: [self.Stepper2Backwards(), print("turing on the stepper2 backwards now")])
        self.ReturnToPurchaseSelectionButton = tk.Button(self, text = "Return to the Purchase menu", command = lambda: [controller.show_frame("PurchaseMenu"), print("moving to Purchase menu")])
        self.ReturnSelectionButton = tk.Button(self, text = "Return to the Main menu", command = lambda: [controller.show_frame("MainMenu"), print("moving to main menu")])
        #This puts the buttons onto the frame
        self.Stepper1ForwardButton.pack()
        self.Stepper1BackwardButton.pack()
        #self.Stepper2ForwardButton.pack()
        #self.Stepper2BackwardButton.pack()
        self.ReturnToPurchaseSelectionButton.pack()
        self.ReturnSelectionButton.pack()
    #Stepper code for dispensing module
    #code for dispensing soda or stepper #1
    def Stepper1Forward(self):
        GPIO.setmode(GPIO.BOARD)
        RPiPins=[11,12,13,15]
        for pin in RPiPins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,False)
        Step_Seq_Num=0
        Rot_Spd=.01
        Rotate=4096
        Rotate_Dir=-1
        Revolutions=1

        Step_Seq=[[0,1,0,1],
                  [0,1,0,0],
                  [0,1,1,0],
                  [0,0,1,0],
                  [1,0,1,0],
                  [1,0,0,0],
                  [1,0,0,1],
                  [0,0,0,1]]

        Rotate=int(Revolutions*4096/10)
        if Rotate<1:Rotate=4096/10
        Rotate_Dir = int(Rotate_Dir)
        if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
        Rot_Spd=float(Rot_Spd)
        if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
        print(Rotate,Rotate_Dir,Rot_Spd)

        for x in range(0,(Rotate+1)):
            for pin in range(0,4):
                Pattern_Pin=RPiPins[pin]
                if Step_Seq[Step_Seq_Num][pin]==1:
                    GPIO.output(Pattern_Pin,True)
                else:
                    GPIO.output(Pattern_Pin,False)
            Step_Seq_Num+=Rotate_Dir
            if(Step_Seq_Num>=8):
                Step_Seq_Num=0
            elif(Step_Seq_Num<0):
                Step_Seq_Num=7
            time.sleep(Rot_Spd)
        GPIO.cleanup()
        print('Done')

    def Stepper1Backwards(self):
        GPIO.setmode(GPIO.BOARD)
        RPiPins=[11,12,13,15]
        for pin in RPiPins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,False)
        Step_Seq_Num=0
        Rot_Spd=.01
        Rotate=4096
        Rotate_Dir=-1
        Revolutions=1

        Step_Seq=[[0,1,0,1],
                  [0,1,0,0],
                  [0,1,1,0],
                  [0,0,1,0],
                  [1,0,1,0],
                  [1,0,0,0],
                  [1,0,0,1],
                  [0,0,0,1]]

        Rotate=int(Revolutions*4096/10)
        if Rotate<1:Rotate=4096/10
        Rotate_Dir = int(Rotate_Dir)
        if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
        Rot_Spd=float(Rot_Spd)
        if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
        print(Rotate,Rotate_Dir,Rot_Spd)

        for x in range(0,(Rotate+1)):
            for pin in range(0,4):
                Pattern_Pin=RPiPins[pin]
                if Step_Seq[Step_Seq_Num][pin]==1:
                    GPIO.output(Pattern_Pin,True)
                else:
                    GPIO.output(Pattern_Pin,False)
            Step_Seq_Num+=Rotate_Dir*-1
            if(Step_Seq_Num>=8):
                Step_Seq_Num=0
            elif(Step_Seq_Num<0):
                Step_Seq_Num=7
            time.sleep(Rot_Spd)
        GPIO.cleanup()
        print('Done')
#code for water dispening stepper or stepper #2
#def StepperForward(self):
#        GPIO.setmode(GPIO.BOARD)
#        RPiPins=[11,12,13,15]
#        for pin in RPiPins:
#            GPIO.setup(pin,GPIO.OUT)
#            GPIO.output(pin,False)
#        Step_Seq_Num=0
#        Rot_Spd=.01
#        Rotate=4096
#        Rotate_Dir=-1
#        Revolutions=1

#        Step_Seq=[[0,1,0,1],
#                  [0,1,0,0],
#                  [0,1,1,0],
#                  [0,0,1,0],
#                  [1,0,1,0],
#                  [1,0,0,0],
#                  [1,0,0,1],
#                  [0,0,0,1]]

#        Rotate=int(Revolutions*4096/10)
#        if Rotate<1:Rotate=4096/10
#        Rotate_Dir = int(Rotate_Dir)
#        if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
#        Rot_Spd=float(Rot_Spd)
#        if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
#        print(Rotate,Rotate_Dir,Rot_Spd)

#        for x in range(0,(Rotate+1)):
#            for pin in range(0,4):
#                Pattern_Pin=RPiPins[pin]
#                if Step_Seq[Step_Seq_Num][pin]==1:
#                    GPIO.output(Pattern_Pin,True)
#                else:
#                    GPIO.output(Pattern_Pin,False)
#            Step_Seq_Num+=Rotate_Dir
#            if(Step_Seq_Num>=8):
#                Step_Seq_Num=0
#            elif(Step_Seq_Num<0):
#                Step_Seq_Num=7
#            time.sleep(Rot_Spd)
#        GPIO.cleanup()
#        print('Done')

#    def StepperBackwards(self):
#        GPIO.setmode(GPIO.BOARD)
#        RPiPins=[11,12,13,15]
#        for pin in RPiPins:
#            GPIO.setup(pin,GPIO.OUT)
#            GPIO.output(pin,False)
#        Step_Seq_Num=0
#        Rot_Spd=.01
#        Rotate=4096
#        Rotate_Dir=-1
#        Revolutions=1

#        Step_Seq=[[0,1,0,1],
#                  [0,1,0,0],
#                  [0,1,1,0],
#                  [0,0,1,0],
#                  [1,0,1,0],
#                  [1,0,0,0],
#                  [1,0,0,1],
#                  [0,0,0,1]]

#        Rotate=int(Revolutions*4096/10)
#        if Rotate<1:Rotate=4096/10
#        Rotate_Dir = int(Rotate_Dir)
#        if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
#        Rot_Spd=float(Rot_Spd)
#        if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
#        print(Rotate,Rotate_Dir,Rot_Spd)

#        for x in range(0,(Rotate+1)):
#            for pin in range(0,4):
#                Pattern_Pin=RPiPins[pin]
#                if Step_Seq[Step_Seq_Num][pin]==1:
#                    GPIO.output(Pattern_Pin,True)
#                else:
#                    GPIO.output(Pattern_Pin,False)
#            Step_Seq_Num+=Rotate_Dir*-1
#            if(Step_Seq_Num>=8):
#                Step_Seq_Num=0
#            elif(Step_Seq_Num<0):
#                Step_Seq_Num=7
#            time.sleep(Rot_Spd)
#        GPIO.cleanup()
#        print('Done')
        
#call method to detect coin acceptor then return to main menu when your are done

if __name__ == "__main__":
    app = RvmMainApp()
    app.title("recycling vending machine")
    app.geometry("425x150")
    app.mainloop()