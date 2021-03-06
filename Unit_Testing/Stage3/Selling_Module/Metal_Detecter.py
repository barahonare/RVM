import serial
import RPi.GPIO as GPIO
from time import sleep
from Selling_Module import POS

#Serial port and baudrate from Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

#Servo GPIO
ServoPin = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ServoPin, GPIO.OUT)
servo1 = GPIO.PWM(ServoPin, 50) # PWM with 50 Hz
servo1.start(12.5)

def main():
    pass

def servo_max():
    servo1.ChangeDutyCycle(12.5) # turn towards 180 degree
def servo_min():
    servo1.ChangeDutyCycle(2.5)

def ScanToOpen(self,controller):
    #to change the label
    PurchasePage = controller.get_page('PurchaseMenu')
    while True:
        servo_max()
        if b'METAL DETECTED\r\n' in ser:
            print('Metal Detected with Pi')
            servo_min()
            print("min(unlock)")
            sleep(3)
            servo_max()
            print("max(lock)")
            sleep(1)
            if POS.DiscountEnabler == 1:
                POS.CanDiscountMethod(PurchasePage)
                POS.DiscountReturnMethod(self)
            self.Scanninglabel.config(text = "Thank you for recycling!")
            break
if __name__=="__Metal_Detecter__":
    main()


# import serial
# from gpiozero import Servo
# from time import sleep
# from Selling_Module import POS

# #Serial port and baudrate from Arduino
# ser = serial.Serial('/dev/ttyACM0', 9600)



# #Servo GPIO
# myGPIO=16
# servo = Servo(myGPIO)
# def main():
#     pass

# def ScanToOpen(self,controller):
#     #to change the label
#     PurchasePage = controller.get_page('PurchaseMenu')
#     while True:
#         servo.max()
#         if b'METAL DETECTED\r\n' in ser:
#             print('Metal Detected with Pi')
#             servo.min()
#             print("min(unlock)")
#             sleep(3)
#             servo.max()
#             print("max(lock)")
#             sleep(1)
#             if POS.DiscountEnabler == 1:
#                 POS.CanDiscountMethod(PurchasePage)
#                 POS.DiscountReturnMethod(self)
#             self.Scanninglabel.config(text = "Thank you for recycling!")
#             break
# if __name__=="__Metal_Detecter__":
#     main()