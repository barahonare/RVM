# Point Of Sale (POS) Module:
# this module contains all methods for calculating amount due
  

Price = 0.0 # Global variable
SodaLimit = 0 # Global variable
WaterLimit = 0 #Global variable
SodaSelected = 0 #Global variable
WaterSelected = 0 #Global variable
CoinAcceptorTotal = 0 #Globabl variable
Discount = 0 #Global variable

def main():
     pass

#this method is to calculate the discount
def DiscountMethod(self):
    global Discount
    Discount += .75
    print("Discount is now set to 75 cents")

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
    if SodaLimit < 1 and WaterLimit < 1:
        Price += .75
        SodaLimit += 1
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ('$%s' %Price))
        print("adding soda")
        print("Increasing sodaLimit")
#method to add the price of a water to the total
def AddPriceOfWater(self):
    global SodaLimit
    global WaterLimit
    global Price
    if WaterLimit < 1 and SodaLimit < 1:
        Price += 1.25
        WaterLimit += 1
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ('$%s' %Price))
        print("adding water")
        print("Increasing waterLimit")
#method to add the price of a soda to the total
def SubtractPriceOfSoda(self):
    global SodaLimit
    global WaterLimit
    global Price
    if SodaLimit > 0 and WaterLimit < 1:
        Price -= .75
        SodaLimit -= 1
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ('$%s' %Price))
        print("Subtracting soda")
        print("Decreasing sodaLimit")
#method to add the price of a water to the total
def SubtractPriceOfWater(self):
    global SodaLimit
    global WaterLimit
    global Price
    if WaterLimit > 0 and SodaLimit < 1:
        Price -= 1.25
        WaterLimit -= 1
        #updates the label containing the total if the limit has not been met
        self.Cartlabel.config(text = ('$%s' %Price))
        print("Subtracting water")
        print("Decreasing waterLimit")
# Method reset price to 0.00
def ResetPrice(self):
    global Price
    global SodaLimit
    global WaterLimit
    SodaLimit = 0
    WaterLimit = 0
    Price = 0.00
    self.Cartlabel.config(text = ('$%s' %Price))
    print("Resetting price")


if __name__== '__POS__':
    main() 