import gpiozero
from time import sleep

# def main():
#     servo1_motor()
def servo1_motor():
    pin_gpio = 17
    motor1 = gpiozero.Servo(pin_gpio)
    for i in range(1,4):
        motor1.min()
        sleep(1)
        motor1.mid()
        sleep(1)

# if __name__ == '__main__':
#     main()
