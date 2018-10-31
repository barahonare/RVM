import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0

try:
        while True:
                if (GPIO.input(27) == 1):
                        print("Pulse comming ! (%s)") % counter
                        time.sleep(0.1)
                        counter += 1
                else:
                        time.sleep(0.01)

except KeyboardInterrupt:
        GPIO.cleanup()
