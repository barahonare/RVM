import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
Trig = 18
Echo = 19

GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig,False)
print("waiting for sensor to settle")
time.sleep(2)

GPIO.output(Trig,True)
time.sleep(0.0001)
GPIO.output(Trig,False)

while GPIO.input(Echo) == 0:
    pulse_start = time.time()

while GPIO.input(Echo) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance,2)

print("Distance: ", distance, "cm")

GPIO.cleanup()