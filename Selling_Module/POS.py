# Point Of Sale (POS) Module:
# this module contains all methods for calculating amount due
  

Price = 0.0 # Global variable
SodaLimit = 0 # Global variable
WaterLimit = 0 #Global variable
SodaSelected = 0 #Global variable
WaterSelected = 0 #Global variable
CoinAcceptorTotal = 0 #Globabl variable
DiscountEnabler = 0 #Global variable
DiscountDisabler = 0 #Global variable
Discount = 0 #Global variable
FinalPrice = 0 #Global Variable

def main():
     pass
#this method is to activate the discount
def DiscountEnablerMethod(self):
    global DiscountEnabler
    DiscountEnabler = 1
    print("Discount is now enabled")
#this method is to deactivate the discount
def DiscountReturnMethod(self):
    global Discount
    global DiscountEnabler
    if DiscountEnabler == 1:
        print("im in the discount return method")
        self.controller.show_frame("PurchaseMenu")
        CanDiscountMethod(self)
#this method is to calculate the discount
def CanDiscountMethod(self):
    global Discount
    global DiscountEnabler
    global FinalPrice
    if DiscountEnabler == 1:
        Discount += 25
        print("discount is this before math" ,Discount)
        print("Final price is this before math" ,FinalPrice)
        FinalPrice -= Discount
        print("discount is this after math" ,Discount)
        print("Final price is this after math" ,FinalPrice)
        self.TotalLabel.config(text = ("Your Final value is " '$%s      ' "Your discount was "'$%s'%(FinalPrice,Discount)))
        print("Discount is now set to $0.25")
#this method is to calculate the discount
def WaterDiscountMethod(self):
    global Discount
    global DiscountEnabler
    global FinalPrice
    if DiscountEnabler == 1:
        Discount += 50
        FinalPrice -= Discount
        self.TotalLabel.config(text = ("Your Final value is " '$%s      ' "Your discount was "'$%s'%(FinalPrice,Discount)))
        print("Discount is now set to $0.50")

#this method is used to set the goal of the amount due for the coin acceptor
def SetFinalTotalPrice2(self):
    global CoinAcceptorTotal
    global Price
    CoinAcceptorTotal = Price
    print("Setting the CoinAcceptorTotal equal to the price")

#these methods are used to determine what we are going to dispense
def SodaSelectedMethod(self):
    global SodaSelected
    SodaSelected = SodaLimit
    print("SodaSelected is now set to the SodaLimit")

def WaterSelectedMethod(self):
    global WaterSelected
    WaterSelected = WaterLimit
    print("WaterSelected is now set to the WaterLimit")

#method to add the price of a soda to the total
def AddPriceOfSoda(self):
    global SodaLimit
    global WaterLimit
    global Price
    global FinalPrice
    global Discount
    if SodaLimit < 1 and WaterLimit < 1:
        Price += 75
        SodaLimit += 1
        FinalPrice = (FinalPrice + Price)
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ("Your Cart Value is " '$%s' %Price))
        self.TotalLabel.config(text = ("Your Final value is " '$%s      ' "Your discount was "'$%s'%(FinalPrice,Discount)))
        print("adding soda")
        print("Increasing sodaLimit")
#method to add the price of a water to the total
def AddPriceOfWater(self):
    global SodaLimit
    global WaterLimit
    global Price
    global FinalPrice
    global Discount
    if WaterLimit < 1 and SodaLimit < 1:
        Price += 125
        WaterLimit += 1
        FinalPrice = (FinalPrice + Price)
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ("Your Cart Value is " '$%s' %Price))
        self.TotalLabel.config(text = ("Your Final value is " '$%s      ' "Your discount was "'$%s'%(FinalPrice,Discount)))
        print("adding water")
        print("Increasing waterLimit")
#method to add the price of a soda to the total
def SubtractPriceOfSoda(self):
    global SodaLimit
    global WaterLimit
    global Price
    global FinalPrice
    global Discount
    if SodaLimit > 0 and WaterLimit < 1:
        FinalPrice -= Price
        Price -= 75
        SodaLimit -= 1
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ("Your Cart Value is " '$%s' %Price))
        self.TotalLabel.config(text = ("Your Final value is " '$%s      ' "Your discount was "'$%s'%(FinalPrice,Discount)))
        print("Subtracting soda")
        print("Decreasing sodaLimit")
#method to add the price of a water to the total
def SubtractPriceOfWater(self):
    global SodaLimit
    global WaterLimit
    global Price
    global FinalPrice
    global Discount
    if WaterLimit > 0 and SodaLimit < 1:
        FinalPrice -= Price
        Price -= 125
        WaterLimit -= 1
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ("Your Cart Value is " '$%s' %Price))
        self.TotalLabel.config(text = ("Your Final value is " '$%s      ' "Your discount was "'$%s'%(FinalPrice,Discount)))
        print("Subtracting water")
        print("Decreasing waterLimit")
# Method reset price to 0.00
def ResetPrice(self):
    global Price
    global SodaLimit
    global WaterLimit
    global FinalPrice
    global Discount
    FinalPrice = 000
    Discount = 000
    SodaLimit = 0
    WaterLimit = 0
    Price = 000
    self.Cartlabel.config(text = ('$%s' %Price))
    self.TotalLabel.config(text = ('$%s' %FinalPrice))
    print("Resetting price")


if __name__== '__POS__':
    main() 