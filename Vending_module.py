import gpiozero
from time import sleep

# def main():
#     servo1_motor()
def servo1_motor():
    pin_gpio = 17
    motor1 = gpiozero.Servo(pin_gpio)
    motor1.max()


# if __name__ == '__main__':
#     main()
