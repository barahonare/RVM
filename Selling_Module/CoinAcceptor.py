import serial
import numpy as np
from time import sleep
from Selling_Module import POS
from Selling_Module import Stepper_Motor as SM

ser = serial.Serial('/dev/ttyACM1', 9600)
def main():
    pass

def ActivateCoinAcceptor(self):
    while True:
        #Converting the byte to string
        s = ser.readline()
        ss = np.fromstring(s, dtype=np.uint8)
        sss = "".join(map(chr,ss))
        #Convert the string to integers
        total_amount = int(sss)
        self.Final_amount = POS.Price
        print(total_amount)
        if total_amount >= 25:
            self.coinlabeltest.config(text = "You have deposited 25 cents")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %Final_amount)
        if total_amount >= 50:
            self.coinlabeltest.config(text = "You have deposited 50 cents")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
        if total_amount >= 75:
            self.coinlabeltest.config(text = "You have deposited 75 cents")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
        if total_amount >= 100:
            self.coinlabeltest.config(text = "You have deposited 1 dollar")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
        if total_amount >= 125:
            self.coinlabeltest.config(text = "You have deposited 1.25 dollar")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
        if total_amount >= POS.Price:
            self.coinlabeltest.config(text = "Thank you for choosing RVM")
            if POS.SodaSelected == 1:
                SM.Stepper1Forward()
            if POS.WaterSelected == 1:
                SM.Stepper2Forward()
            break
if __name__=="__CoinAcceptor__":
    main()