import RPi.GPIO as GPIO
from time import sleep
from Selling_Module import POS

#Servo GPIO
ServoPin = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ServoPin, GPIO.OUT)
servo1 = GPIO.PWM(ServoPin, 50) # PWM with 50 Hz
servo1.start(12.5)

def servo_max():
    servo1.ChangeDutyCycle(12.5) # turn towards 180 degree
def servo_min():
    servo1.ChangeDutyCycle(10)

def main():
    pass

def PlasticDoorOpen(self,controller):
    self.OpeningDoorPromptlabel.config(text = "Please wait as the safety plastic door is opening")
    self.update()
    PurchasePage = controller.get_page("PurchaseMenu")
    servo_max()
    servo_min()
    print("min(unlock)")
    sleep(10)
    servo_max()
    print("max(lock)")
    self.OpeningDoorPromptlabel.config(text = "Thank you for recycling!")
    self.update()
    sleep(3)
    if POS.DiscountEnabler == 1:
        POS.WaterDiscountMethod(PurchasePage)
        POS.DiscountReturnMethod(self)
    elif POS.DiscountEnabler == 0:
        POS.DiscountReturnMethod(self)
if __name__=="__PlasticDoorServo__":
    main()
