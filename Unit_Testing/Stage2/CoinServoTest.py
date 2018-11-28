import serial
import numpy as np
import RPi.GPIO as GPIO
from time import sleep

#Servo GPIO
ServoPin = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ServoPin, GPIO.OUT)
servo1 = GPIO.PWM(ServoPin, 50) # PWM with 50 Hz
servo1.start(10.0)
print("Start state")

def main():
    pass

def servorun():
    while True:
    ##    servo1.ChangeDutyCycle(2.7)
    ##    sleep(2)
        servo1.ChangeDutyCycle(6.0)
        print("locked")
        sleep(2)
        servo1.ChangeDutyCycle(10.0)
        print("open")
        sleep(2)

def ActivateCoinAcceptor():
    ser = serial.Serial('/dev/ttyACM1', 9600)
    while True:
        #Converting the byte to string
        s = ser.readline()
        ss = np.fromstring(s, dtype=np.uint8)
        sss = "".join(map(chr,ss))
        #Convert the string to integers
        total_amount = int(sss)
        print(total_amount)
        if total_amount >= 25:
            print("Thank you for choosing RVM")
            print(total_amount)
            ser.close()
            servorun()
            break
        
ActivateCoinAcceptor()

if __name__=="__CoinServoTest__":
    main()
        


