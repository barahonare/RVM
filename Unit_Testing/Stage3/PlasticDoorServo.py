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
    servo1.ChangeDutyCycle(2.5)

def main():
    pass

def PlasticDoorOpen(self):
    while True:
        servo_max()
        servo_min()
        print("min(unlock)")
        sleep(3)
        servo_max()
        print("max(lock)")
        sleep(1)
        if POS.DiscountEnabler == 1:
            POS.CanDiscountMethod(self)
            POS.DiscountReturnMethod(self)
        self.Scanninglabel.config(text = "Thank you for recycling!")
if __name__=="__PlasticDoorServo__":
    main()