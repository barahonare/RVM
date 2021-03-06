import serial
import RPi.GPIO as GPIO
from time import sleep
import time
from Selling_Module import POS

#Serial port and baudrate from Arduino


#Servo GPIO
ServoPin = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ServoPin, GPIO.OUT)
servo1 = GPIO.PWM(ServoPin, 50) # PWM with 50 Hz
servo1.start(6.0)

def main():
    pass

def servo_locked():
    servo1.ChangeDutyCycle(6.0) # turn towards 180 degree
def servo_open():
    servo1.ChangeDutyCycle(10.0)

def ScanToOpen(self,controller):
    #to change the label
    self.Scanninglabel.config(text="Place can on the alumimum sensor")
    self.update()
    ser = serial.Serial('/dev/ttyACM0', 9600)
    PurchasePage = controller.get_page('PurchaseMenu')
    timeout = time.time() +6
    flag = True
    while (time.time() < timeout):
        servo_locked()
        # print(time.time(), timeout)
        if b'METAL DETECTED\r\n' in ser:
            print('Metal Detected with Pi')
            servo_open()
            print("min(unlock)")
            sleep(10)
            servo_locked()
            print("max(lock)")
            sleep(1)
            if POS.DiscountEnabler == 1:
                POS.CanDiscountMethod(PurchasePage)
                self.Scanninglabel.config(text = "Thank you for recycling!")
                ser.close()
                # self.update()
                # sleep(2)
                flag = False
                ser.close()
                self.Scanninglabel.config(text = "Press the scanning button to check can")
                POS.DiscountReturnMethod(self)
                # controller.show_frame("MainMenu")
                break
            elif POS.DiscountEnabler == 0:
                flag = False
                ser.close()
                POS.DiscountReturnMethod(self)
                break
    # if flag:
    #     print("time out while loop")
    #     controller.show_frame("MainMenu")
    # if flag:
    #     self.Scanninglabel.config(text = "Metal was not detected")
    #     # self.update()
    #     # sleep(3)
    #     controller.show_frame("MainMenu")

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




# import serial
# import RPi.GPIO as GPIO
# from time import sleep
# import time
# from Selling_Module import POS

# #Serial port and baudrate from Arduino


# #Servo GPIO
# ServoPin = 36
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(ServoPin, GPIO.OUT)
# servo1 = GPIO.PWM(ServoPin, 50) # PWM with 50 Hz
# servo1.start(6.0)

# def main():
#     pass

# def servo_locked():
#     servo1.ChangeDutyCycle(6.0) # turn towards 180 degree
# def servo_open():
#     servo1.ChangeDutyCycle(10.0)

# def ScanToOpen(self,controller):
#     #to change the label
#     ser = serial.Serial('/dev/ttyACM0', 9600)
#     PurchasePage = controller.get_page('PurchaseMenu')
#     timeout = time.time() +6
#     flag = True
#     while (time.time() < timeout):
#         servo_locked()
#         print(time.time(), timeout)
#         if b'METAL DETECTED\r\n' in ser:
#             print('Metal Detected with Pi')
#             servo_open()
#             print("min(unlock)")
#             sleep(10)
#             servo_locked()
#             print("max(lock)")
#             sleep(1)
#             if POS.DiscountEnabler == 1:
#                 POS.CanDiscountMethod(PurchasePage)
#                 self.Scanninglabel.config(text = "Thank you for recycling!")
#                 ser.close()
#                 # self.update()
#                 # sleep(2)
#                 # flag = False
#                 POS.DiscountReturnMethod(self)
#                 # controller.show_frame("MainMenu")
#                 break
#             elif POS.DiscountEnabler == 0:
#                 # flag = False
#                 POS.DiscountReturnMethod(self)
#                 break

#     # if flag:
#     #     self.Scanninglabel.config(text = "Metal was not detected")
#     #     # self.update()
#     #     # sleep(3)
#     #     controller.show_frame("MainMenu")

# if __name__=="__Metal_Detecter__":
#     main()


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
