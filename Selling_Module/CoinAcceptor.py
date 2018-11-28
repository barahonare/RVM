import serial
import numpy as np
from time import sleep
from Selling_Module import POS
from Selling_Module import Stepper_Motor as SM

def main():
    pass

def ActivateCoinAcceptor(self, controller):
    ser = serial.Serial('/dev/ttyACM1', 9600)
    PurchaseMenuPage = controller.get_page("PurchaseMenu")
    while True:
        if POS.EndProcess == 1:
            break
        #Converting the byte to string
        s = ser.readline()
        ss = np.fromstring(s, dtype=np.uint8)
        sss = "".join(map(chr,ss))
        #Convert the string to integers
        total_amount = int(sss)
        self.Final_amount = POS.Price
        print(total_amount)
        if total_amount >= 25:
            self.coinlabeltest.config(text = "You have deposited $0.25")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
            self.update()
        if total_amount >= 50:
            self.coinlabeltest.config(text = "You have deposited $0.50")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
            self.update()
        if total_amount >= 75:
            self.coinlabeltest.config(text = "You have deposited $0.75")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
            self.update()
        if total_amount >= 100:
            self.coinlabeltest.config(text = "You have deposited $1.00")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
            self.update()
        if total_amount >= 125:
            self.coinlabeltest.config(text = "You have deposited $1.25")
            self.Final_amount -= 25
            self.FinalTotalLabel.config(text = '$%s' %self.Final_amount)
            self.update()
        if total_amount >= POS.FinalPrice:
            self.coinlabeltest.config(text = "Thank you for choosing RVM")
            if POS.SodaSelected == 1:
                SM.Stepper1Forward(self)
            if POS.WaterSelected == 1:
                SM.Stepper2Forward(self)
            print(total_amount, POS.Price)
            ser.close()
            POS.ResetPrice(PurchaseMenuPage)
            controller.show_frame("MainMenu")
            break
if __name__=="__CoinAcceptor__":
    main()