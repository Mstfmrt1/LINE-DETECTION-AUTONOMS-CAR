from motormodul import MOTOR
from lanedetectionmodule import getlanecurve
import cammodule
import distancemodule
import cv2
######
motor1=MOTOR(2,3,4,18,14,15)##motor sınıfından motor1 objesi
######

def main():
    img=cammodule.get_img()
    curvevalue=getlanecurve(img,1)
    distance=distancemodule.get_distance()#mesafe ölçümü
    if distance<12:#mesafe 12cmden küçükse 12cm olana kadar durdurduk 
        while(distance>12):
            motor1.stop(1)
    sen = 1.3  # hassaslık
    maxVAl= 0.3 # maxhız
    if curvevalue>maxVAl:
        curvevalue = maxVAl
    if curvevalue<-maxVAl:
        curvevalue =-maxVAl
    #print(curveVal)
    if curvevalue>0:
        sen =1.7
        if curvevalue<0.05: 
            curvevalue=0
    else:
        if curvevalue>-0.08: curvevalue=0
    motor1.move(0.20,-curvevalue*sen,0.05)
    cv2.waitKey(1)
     
 
if __name__ == '__main__':
    while True:
        main()
    
    