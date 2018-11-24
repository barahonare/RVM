from gpiozero import Servo
from time import sleep
from Selling_Module import POS


#Servo GPIO
myGPIO=16
servo = Servo(myGPIO)
def main():
    pass

def PlasticDoorOpen(self):
    while True:
        servo.max()
        servo.min()
        print("min(unlock)")
        sleep(3)
        servo.max()
        print("max(lock)")
        sleep(1)
        if POS.DiscountEnabler == 1:
            POS.CanDiscountMethod(self)
            POS.DiscountReturnMethod(self)
        self.Scanninglabel.config(text = "Thank you for recycling!")
if __name__=="__PlasticDoorServo__":
    main()