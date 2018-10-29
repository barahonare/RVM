# Point Of Sale (POS) Module:
# this module contains all methods for calculating amount due
  

Price = 0.0 # Global variable

def main():
     pass
#method to add the price of a soda to the total
def AddPriceOfSoda(self):
    global Price
    Price += .25
    #updates the label containing the total
    self.Cartlabel.config(text = ('$%s' %Price))
    print("adding soda")
#method to add the price of a water to the total
def AddPriceOfWater(self):
    global Price
    Price += 1.00
    #updates the label containing the total
    self.Cartlabel.config(text = ('$%s' %Price))
    print("adding water")
#method to add the price of a soda to the total
def SubtractPriceOfSoda(self):
    global Price
    Price -= .25
    #updates the label containing the total
    self.Cartlabel.config(text = ('$%s' %Price))
    print("Subtracting soda")
#method to add the price of a water to the total
def SubtractPriceOfWater(self):
    global Price
    Price -= 1.00
    #updates the label containing the total
    self.Cartlabel.config(text = ('$%s' %Price))
    print("Subtracting water")
# Method reset price to 0.00
def ResetPrice(self):
    global Price
    Price = 0.00
    self.Cartlabel.config(text = ('$%s' %Price))
    print("Resetting price")


if __name__== '__POS__':
    main() 