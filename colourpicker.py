import cv2
import numpy as np


# framewidth=400
# frameheight=300

# cam=cv2.VideoCapture(0)

# cam.set(3,framewidth)
# cam.set(4,frameheight)

# # cam=cv2.VideoCapture(0)
# #  kamera açılırsa bunları kullanabiliriz


def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE MIN","HSV",0,179,empty)
cv2.createTrackbar("HUE MAX","HSV",179,179,empty)
cv2.createTrackbar("SAT MIN","HSV",0,255,empty)
cv2.createTrackbar("SAT MAX","HSV",255,179,empty)
cv2.createTrackbar("VAL MIN","HSV",0,255,empty)
cv2.createTrackbar("VAL MAX","HSV",255,255,empty)
cam=cv2.VideoCapture('lane.mp4')
framecounter=0
while cam.isOpened():
        framecounter+=1
        if cam.get(cv2.CAP_PROP_FRAME_COUNT)==framecounter:
            cam.set(cv2.CAP_PROP_POS_FRAMES,0)
            framecounter=0
    
        
    
        _,frame=cam.read()
        frame=cv2.resize(frame,(480,240))
    
        framehsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        h_min=cv2.getTrackbarPos("HUE MIN","HSV")
        h_max=cv2.getTrackbarPos("HUE MAX","HSV")    
        s_min=cv2.getTrackbarPos("SAT MIN","HSV")
        s_max=cv2.getTrackbarPos("SAT MAX","HSV")
        v_min=cv2.getTrackbarPos("VAL MIN","HSV")
        v_max=cv2.getTrackbarPos("VAL MAX","HSV")
    
        lower=np.array([h_min,s_min,v_min])
        upper=np.array([h_max,s_max,v_max])
    
        mask=cv2.inRange(framehsv,lower,upper)
    
        result=cv2.bitwise_and(frame,frame,mask=mask)
    
        mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    
    # cv2.imshow("MASK",mask)
   
        hstack=np.hstack([frame,mask,result]) 
        cv2.imshow('HORIZONTAL STACK',hstack)
    
        if cv2.waitKey(1)==ord('q'):
           cam.release()   
           cv2.destroyAllWindows()     
     
            
            
   

