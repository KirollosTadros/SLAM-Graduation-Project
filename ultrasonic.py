import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

Trig= 26
Echo = 19

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)


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

while True:
    dist = ultrasonic_echo(Trig, Echo)

    print(dist)

    print("\n")
