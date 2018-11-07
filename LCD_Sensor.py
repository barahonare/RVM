

import RPi.GPIO as GPIO
import time

file = open('/sys/devices/platform/rpi_backlight/backlight/rpi_backlight/bl_power','r+')
current_status = int(file.read(1))

def main():

    GPIO.setmode(GPIO.BOARD)
    Trig = 18
    Echo = 19
    GPIO.setup(Trig,GPIO.OUT)
    GPIO.setup(Echo,GPIO.IN)

    GPIO.output(Trig,False)
    print("waiting for sensor to settle")
    time.sleep(2)

    distance = 500

    while 1 == 1:
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
        
        if distance <= 70 and current_status == 1:
            timeout = time.time()+ 1
            while (time.time()<timeout) and current_status == 1:
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
                print("user detected")
            print("User found")
            switch = LCD_Backlight(0)
        

def LCD_Backlight(switch):
        
    if current_status != switch:
        bl_set = int(switch)
    else:
        bl_set = current_status
    

    print("LCD switched")
    
    bl_update = str(bl_set)
    file.seek(0)
    file.write(bl_update)
    file.close
    
    return bl_update
        


if __name__=='__main__':
    main()
    GPIO.cleanup()