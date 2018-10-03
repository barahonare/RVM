import gpiozero
from time import sleep

pin_gpio = 17
servo1 = gpiozero.Servo(pin_gpio)

# def main():
#     servo1_motor()
# def servo1_motor():
    

    # for i in range(1,4):
    #     motor1.min()
    #     sleep(1)
    #     motor1.mid()
    #     sleep(1)
def servo1_open():
    servo1.max()
    
def servo1_close():
    servo1.min()


# if __name__ == '__main__':
#     main()
