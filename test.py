import RPi.GPIO as GPIO
import sys, tty, termios, time
GPIO.setmode(GPIO.BCM)

#ultrasonic pins
Trig_M= 26
Echo_M = 19

Trig_R = 13
Echo_R = 6

Trig_L = 21
Echo_L = 20


#Motor A pins
enA = 22
IN1 = 24
IN2 = 17

#Motor B Pins
enB = 23
IN3 = 27
IN4 = 18


#Motor Pins setup
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

enA_PWM=GPIO.PWM(enA,500)
enB_PWM=GPIO.PWM(enB,500)

#Ultrasonic Pins Setup
GPIO.setup(Trig_M, GPIO.OUT)
GPIO.setup(Echo_M, GPIO.IN)

#GPIO.setup(Trig_L, GPIO.OUT)
#GPIO.setup(Echo_L, GPIO.IN)

GPIO.setup(Trig_R, GPIO.OUT)
GPIO.setup(Echo_R, GPIO.IN)


#Ultrasonic Function
def ultrasonic_echo(Trig, Echo):
    
    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)


    while GPIO.input (Echo) == 0:
        StartTime = time.time()

    while GPIO.input (Echo) == 1:
        StopTime = time.time()


    TimeElapsed = StopTime -StartTime

    distance = (TimeElapsed * 34300)/2
    
    return distance
#End Ultrasonic Function


#Motor Functions

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


#End Motor Functions



while True:
    try:
        '''
        dist_m = ultrasonic_echo (Trig_M, Echo_M)
        dist_l = ultrasonic_echo (Trig_L, Echo_L)
        dist_r = ultrasonic_echo (Trig_R, Echo_R)
      
        if dist_m>50:
            Motor_A_Forward(100)
            Motor_B_Forward(100)

        elif dist_r<40 and dist_m>50:

            Motor_A_Stop()
            Motor_B_Stop()
            
            time.sleep(0.5)

            Motor_A_Forward(100)
            Motor_B_Backward(100)
            
            time.sleep(0.5)


        elif dist_l<40 and dist_m>50:

            Motor_A_Stop()
            Motor_B_Stop()
            
            time.sleep(0.5)

            Motor_A_Backward(100)
            Motor_B_Forward(100)
            
            time.sleep(0.5)

            
            
        else:
            Motor_A_Stop()
            Motor_B_Stop()
            
            time.sleep(0.5)

            Motor_A_Forward(100)
            Motor_B_Backward(100)
            
            time.sleep(0.9)
            '''

        print(ultrasonic_echo(Trig_R, Echo_R))
        print("\n")
        

    
    except KeyboardInterrupt:
        GPIO.cleanup()
        
    


    

