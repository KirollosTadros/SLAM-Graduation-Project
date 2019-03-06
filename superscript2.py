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

    

while True:
    c= getch()
    
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    if(c=="w"):
        GPIO.output (17, False)
        GPIO.output (18, False)
        GPIO.output (22, True)
        GPIO.output (23, True)
        GPIO.output (24, True)
        GPIO.output (27, True)

    #time.sleep(3)
    elif (c== "a"):
	GPIO.output (17, False)
        GPIO.output (18, False)
        GPIO.output (22, True)
        GPIO.output (23, True)
        GPIO.output (24, True)
        GPIO.output(27, False)

    #time.sleep(3)
    elif (c == "d"):
	GPIO.output (18, False)
        GPIO.output (18, False)
        GPIO.output (22, True)
        GPIO.output (23, True)
        GPIO.output(27, True)
        GPIO.output(24, False)
    elif(c=="s"):
        GPIO.output (17, True)
        GPIO.output (18, True)
        GPIO.output (22, True)
        GPIO.output (23, True)
        GPIO.output (24, False)
        GPIO.output (27, False)
    elif(c==" "):
        GPIO.output (17, True)
        GPIO.output (18, True)
        GPIO.output (22, False)
        GPIO.output (23, False)
        GPIO.output (24, True)
        GPIO.output (27, True)
    elif (c=="q"):
        break;
    elif (c == "\0"):
	 GPIO.output (17, False)
         GPIO.output (18, False)
         GPIO.output (22, False)
         GPIO.output (23, False)
         GPIO.output (24, False)
         GPIO.output (27, False)
 
    #time.sleep(0.1)
   
