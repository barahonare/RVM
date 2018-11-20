import serial
from gpiozero import Servo
from time import sleep

#Serial port and baudrate from Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

#Servo GPIO
myGPIO=16
servo = Servo(myGPIO)

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
            self.DoneLabel.config(text = "Thank you for recycling!")