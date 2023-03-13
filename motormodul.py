import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)#gpıo numaralarına göre bağlantılar yapılır
GPIO.setwarnings(False)

class MOTOR():
    def __init__(self,ENAA,INA1,INA2,ENAB,INB1,INB2):
        self.ENAA=ENAA
        self.INA1=INA1
        self.INA2=INA2
        self.ENAB=ENAB
        self.INB1=INB1
        self.INB2=INB2
        GPIO.setup(self.ENAA,GPIO.OUT)
        GPIO.setup(self.INA1,GPIO.OUT)   
        GPIO.setup(self.INA2,GPIO.OUT)   
        GPIO.setup(self.ENAB,GPIO.OUT)
        GPIO.setup(self.INB1,GPIO.OUT)   
        GPIO.setup(self.INB2,GPIO.OUT)   
        
        self.pwmA=GPIO.PWM(self.ENAA,100)
        self.pwmA.start(0)
        self.pwmB=GPIO.PWM(self.ENAB,100)
        self.pwmB.start(0)
    
     
        
     
    def move(self,speed=0.5,turn=0,time=0):
        #normalizasyon ile 0-100
        speed*=100
        turn*=100
        leftspeed=speed-turn #sola dönüşte daha yavaş olacağından sola dönücektir
        rightspeed=speed+turn
        
        if leftspeed>100: leftspeed=100
        elif leftspeed<-100: leftspeed= -100
        
        if rightspeed>100: rightspeed=100
        elif rightspeed<-100: rightspeed= -100
        
        self.pwmA.ChangeDutyCycle(abs(leftspeed))
        self.pwmB.ChangeDutyCycle(abs(rightspeed))
        
        if leftspeed>0:
            GPIO.output(self.INA1,GPIO.HIGH)
            GPIO.output(self.INA2,GPIO.LOW)
        else:
            GPIO.output(self.INA1,GPIO.LOW)
            GPIO.output(self.INA2,GPIO.HIGH)
 
        if rightspeed>0:
            GPIO.output(self.INB1,GPIO.HIGH)
            GPIO.output(self.INB2,GPIO.LOW)
        else:
            GPIO.output(self.INB1,GPIO.LOW)
            GPIO.output(self.INB2,GPIO.HIGH)
 
        sleep(time)
  
        
    def stop(self,time=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)

        sleep(time)
        
        
# DENEME motor1=MOTOR(2,3,4,18,15,14) #MOTOR SINIFINDAN MOTOR 1 OBJesi OLUşturuyoruz
        
# def main():
    
#     motor1.move(0.9,-0.2,2)
#     motor1.stop(2)
    
#     motor1.move(0.3,0.2,2)
#     motor1.stop(2)
     

# if __name__=='__main__':
#     while True:
    
#        main()

