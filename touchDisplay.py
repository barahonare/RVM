#!/usr/bin/python
#
#   backlight-toggle.py   10-25-2015 
#     
#   RPF 7" Touchscreen Display
#          Toggles backlight on/off with button press 
#          Uses GPIO5  (BOARD Pin 29)


import RPi.GPIO as gpio
from subprocess import call
import time

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.IN, pull_up_down = gpio.PUD_UP)

def set_backlight(channel):
    file = open('/sys/devices/platform/rpi_backlight/backlight/rpi_backlight/bl_power','r+')
    current_status = int(file.read(1))
    
    if current_status == 0:
        bl_set = 1
    else:
        bl_set = 0

    bl_update = str(bl_set)
    file.seek(0)
    file.write(bl_update)
    file.close
    
gpio.add_event_detect(5, gpio.FALLING, callback=set_backlight, bouncetime=300)

while 1:
    time.sleep(360)