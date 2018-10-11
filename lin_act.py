from rrb3 import *
from random import randint

rr = RRB3(12, 12) # Battery voltage 12V, motor 12V

T = 15  # seconds to extend

extended = False

try:
	while True:
            if extended:   # if extended retract
		    print("retracting")
		    rr.set_led1(True)  # LED 1 on
		    rr.reverse(T, 1.0)
		    rr.set_led1(False)
		    extended = False   # now set extended as false
	    elif rr.get_distance() < 10:   # if range finder distance < 15 cm
		    print("extending")
		    rr.set_led2(True)
		    rr.forward(T, 1.0)
		    rr.set_led2(False)
		    extended = True   # now set extended back to true
            print("done")
finally:
	rr.cleanup() # Set all GPIO pins to safe input state