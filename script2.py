import RPi.GPIO as GPIO
import sys, tty, termios, time
GPIO.setmode(GPIO.BCM)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#Motor A pins
enA = 22
IN1 = 24
IN2 = 17

#Motor B Pins
enB = 23
IN3 = 27
IN4 = 18



GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

enA_PWM=GPIO.PWM(enA,500)
enB_PWM=GPIO.PWM(enB,500)


def Motor_A_Forward(PWM):
    GPIO.output (IN1, True)
    GPIO.output (IN2, False)
    enA_PWM.start(PWM)

def Motor_A_Backward(PWM):
    GPIO.output (IN1, False)
    GPIO.output (IN2, True)
    enA_PWM.start(PWM)

def Motor_A_OFF():
    GPIO.output (IN1, False)
    GPIO.output (IN2, False)
    enA_PWM.start(100)

def Motor_A_Stop():
    GPIO.output (IN1, True)
    GPIO.output (IN2, True)
    enA_PWM.start(100)


def Motor_B_Forward(PWM):
    GPIO.output (IN3, True)
    GPIO.output (IN4, False)
    enB_PWM.start(PWM)

def Motor_B_Backward(PWM):
    GPIO.output (IN3, False)
    GPIO.output (IN4, True)
    enB_PWM.start(PWM)


def Motor_B_OFF():
    GPIO.output (IN3, False)
    GPIO.output (IN4, False)
    enB_PWM.start(100)

def Motor_B_Stop():
    GPIO.output (IN3, True)
    GPIO.output (IN4, True)
    enB_PWM.start(100)



while True:
    c= getch()


    if(c=="w"):
        Motor_A_Forward(100)
        Motor_B_Forward(100)


    elif (c== "a"):
        Motor_A_Forward(85)
        Motor_B_Stop()

    #time.sleep(3)
    elif (c == "d"):
        Motor_A_Stop()
        Motor_B_Forward(85)

    elif(c=="s"):
        Motor_A_Backward(100)
        Motor_B_Backward(100)


    elif(c==" "):
        Motor_A_Stop()
        Motor_B_Stop()

    elif (c=="q"):
        break


