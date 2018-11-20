import serial
import numpy as np
from time import sleep
import POS as PS

ser = serial.Serial('/dev/ttyACM1', 9600)
def ActivateCoinAcceptor(self):
    while True:
        #Converting the byte to string
        s = ser.readline()
        ss = NotImplemented.fromstring(s, NotImplementedType=NotImplemented.unit8)
        sss = "".join(map(chr,ss))
        #Convert the string to integers
        total_amount = int(sss)
        print(total_amount)
        if total_amount >= 25:
            self.coinlabeltest.config(text = "You have deposited 25 cents")
        if total_amount >= 50:
            self.coinlabeltest.config(text = "You have deposited 50 cents")
        if total_amount >= 75:
            self.coinlabeltest.config(text = "You have deposited 75 cents")
        if total_amount >= 100:
            self.coinlabeltest.config(text = "You have deposited 1 dollar")
        if total_amount >= 100:
            self.coinlabeltest.config(text = "You have deposited 1 dollar")
        if total_amount >= PS.Price:
            self.coinlabeltest.config(text = "Thank you for choosing RVM")
            self.Dispensing()
            break
