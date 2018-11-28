import time
import RPi.GPIO as GPIO


RPiPins1=[11,12,13,15]
RPiPins2=[35,37,38,40]

def main():
    pass

def Stepper1Forward(self):
    GPIO.setmode(GPIO.BOARD)
    global RPiPins1
    for pin in RPiPins1:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,False)

    Step_Seq_Num=0
    Rot_Spd=.01
    Rotate=4096
    Rotate_Dir=-1
    Revolutions=8

    Step_Seq=  [[0,1,0,1],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [1,0,1,0],
                [1,0,0,0],
                [1,0,0,1],
                [0,0,0,1]]

    Rotate=int(Revolutions*4096/10)
    if Rotate<1:Rotate=4096/10
    Rotate_Dir = int(Rotate_Dir)
    if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
    Rot_Spd=float(Rot_Spd)
    if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
    print(Rotate,Rotate_Dir,Rot_Spd)

    for x in range(0,(Rotate+1)):
        for pin in range(0,4):
            Pattern_Pin=RPiPins1[pin]
            if Step_Seq[Step_Seq_Num][pin]==1:
                GPIO.output(Pattern_Pin,True)
            else:
                GPIO.output(Pattern_Pin,False)
        Step_Seq_Num+=Rotate_Dir
        if(Step_Seq_Num>=8):
            Step_Seq_Num=0
        elif(Step_Seq_Num<0):
            Step_Seq_Num=7
        time.sleep(Rot_Spd)
    #GPIO.cleanup()
    print('Done')

def Stepper1Backwards(self):
    GPIO.setmode(GPIO.BOARD)
    global RPiPins1
    for pin in RPiPins1:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,False)

    Step_Seq_Num=0
    Rot_Spd=.01
    Rotate=4096
    Rotate_Dir=-1
    Revolutions=8

    Step_Seq=  [[0,1,0,1],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [1,0,1,0],
                [1,0,0,0],
                [1,0,0,1],
                [0,0,0,1]]

    Rotate=int(Revolutions*4096/10)
    if Rotate<1:Rotate=4096/10
    Rotate_Dir = int(Rotate_Dir)
    if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
    Rot_Spd=float(Rot_Spd)
    if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
    print(Rotate,Rotate_Dir,Rot_Spd)

    for x in range(0,(Rotate+1)):
        for pin in range(0,4):
            Pattern_Pin=RPiPins1[pin]
            if Step_Seq[Step_Seq_Num][pin]==1:
                GPIO.output(Pattern_Pin,True)
            else:
                GPIO.output(Pattern_Pin,False)
        Step_Seq_Num+=Rotate_Dir*-1
        if(Step_Seq_Num>=8):
            Step_Seq_Num=0
        elif(Step_Seq_Num<0):
            Step_Seq_Num=7
        time.sleep(Rot_Spd)
    #GPIO.cleanup()
    print('Done')

def Stepper2Forward(self):
    GPIO.setmode(GPIO.BOARD)
    global RPiPins2
    for pin in RPiPins2:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,False)

    Step_Seq_Num=0
    Rot_Spd=.01
    Rotate=4096
    Rotate_Dir=-1
    Revolutions=8

    Step_Seq=  [[0,1,0,1],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [1,0,1,0],
                [1,0,0,0],
                [1,0,0,1],
                [0,0,0,1]]

    Rotate=int(Revolutions*4096/10)
    if Rotate<1:Rotate=4096/10
    Rotate_Dir = int(Rotate_Dir)
    if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
    Rot_Spd=float(Rot_Spd)
    if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
    print(Rotate,Rotate_Dir,Rot_Spd)

    for x in range(0,(Rotate+1)):
        for pin in range(0,4):
            Pattern_Pin=RPiPins2[pin]
            if Step_Seq[Step_Seq_Num][pin]==1:
                GPIO.output(Pattern_Pin,True)
            else:
                GPIO.output(Pattern_Pin,False)
        Step_Seq_Num+=Rotate_Dir
        if(Step_Seq_Num>=8):
            Step_Seq_Num=0
        elif(Step_Seq_Num<0):
            Step_Seq_Num=7
        time.sleep(Rot_Spd)
    #GPIO.cleanup()
    print('Done')

def Stepper2Backwards(self):
    GPIO.setmode(GPIO.BOARD)
    global RPiPins2
    for pin in RPiPins2:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,False)

    Step_Seq_Num=0
    Rot_Spd=.01
    Rotate=4096
    Rotate_Dir=-1
    Revolutions=8

    Step_Seq=  [[0,1,0,1],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [1,0,1,0],
                [1,0,0,0],
                [1,0,0,1],
                [0,0,0,1]]

    Rotate=int(Revolutions*4096/10)
    if Rotate<1:Rotate=4096/10
    Rotate_Dir = int(Rotate_Dir)
    if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
    Rot_Spd=float(Rot_Spd)
    if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
    print(Rotate,Rotate_Dir,Rot_Spd)

    for x in range(0,(Rotate+1)):
        for pin in range(0,4):
            Pattern_Pin=RPiPins2[pin]
            if Step_Seq[Step_Seq_Num][pin]==1:
                GPIO.output(Pattern_Pin,True)
            else:
                GPIO.output(Pattern_Pin,False)
        Step_Seq_Num+=Rotate_Dir*-1
        if(Step_Seq_Num>=8):
            Step_Seq_Num=0
        elif(Step_Seq_Num<0):
            Step_Seq_Num=7
        time.sleep(Rot_Spd)
    #GPIO.cleanup()
    print('Done')

if __name__=="__Stepper_Motor__":
    main()
