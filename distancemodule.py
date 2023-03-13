import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 27
ECHO = 22

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def getdistance():
    
    GPIO.output(TRIG, False)
 
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    gecenzaman = pulse_end - pulse_start
    distance = gecenzaman * 17150
    distance = round(distance, 2)
    return distance
 
 