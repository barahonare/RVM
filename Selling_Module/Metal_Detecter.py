import serial
from gpiozero import Servo
from time import sleep
from Selling_Module import POS

#Serial port and baudrate from Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

#to change the label
PurchasePage = controller.get_page('PurchaseMenu')

#Servo GPIO
myGPIO=16
servo = Servo(myGPIO)
def main():
    pass

def ScanToOpen(self):
    while True:
        servo.max()
        if b'METAL DETECTED\r\n' in ser:
            print('Metal Detected with Pi')
            servo.min()
            print("min(unlock)")
            sleep(3)
            servo.max()
            print("max(lock)")
            sleep(1)
            if POS.DiscountEnabler == 1:
                POS.CanDiscountMethod(PurchasePage)
                POS.DiscountReturnMethod(self)
            self.Scanninglabel.config(text = "Thank you for recycling!")
            break
if __name__=="__Metal_Detecter__":
    main()