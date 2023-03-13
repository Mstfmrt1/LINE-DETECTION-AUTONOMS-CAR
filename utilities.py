import cv2
import numpy as np


def thresholding(img):
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # kernel=np.ones((6,6),np.uint8)
    lowerwhite=np.array([0,0,91])
    upperwhite=np.array([179,34,255])
    maskwhite=cv2.inRange(imghsv,lowerwhite,upperwhite)
    blur=cv2.GaussianBlur(maskwhite,(5,5),0)
    # closing=cv2.morphologyEx(blur,cv2.MORPH_CLOSE,kernel)
     
    
   
    cv2.imshow("blur",blur)
    return blur


def warpimg(img,points,wT,hT,inverse=False):
    point1=np.float32(points)
    point2=np.float32([(0,0),(wT,0),(0,hT),(wT,hT)])
    if inverse:
        donusummatrix=cv2.getPerspectiveTransform(point2,point1)
    else:    
        donusummatrix=cv2.getPerspectiveTransform(point1,point2)
    imgwarp=cv2.warpPerspective(img,donusummatrix,(wT,hT))
    return imgwarp


def nothing(a):
    pass

def initiliazetrackbar(initialtrackbarval,wT=480,hT=240):
    cv2.namedWindow("TRACKBAR")
    cv2.resizeWindow("TRACKBAR",360,240)
    cv2.createTrackbar("WIDTH TOP","TRACKBAR",initialtrackbarval[0],wT//2,nothing)
    cv2.createTrackbar("HEIGHT TOP","TRACKBAR",initialtrackbarval[1],hT,nothing)
    cv2.createTrackbar("WIDTH BOTTOM","TRACKBAR",initialtrackbarval[2],wT//2,nothing)
    cv2.createTrackbar("HEIGHT BOTTOM","TRACKBAR",initialtrackbarval[3],hT,nothing)

def valtrackbars(wT=480,hT=240):
    widthtop=cv2.getTrackbarPos("WIDTH TOP","TRACKBAR")
    heighttop=cv2.getTrackbarPos("HEIGHT TOP","TRACKBAR")
    widthbottom=cv2.getTrackbarPos("WIDTH BOTTOM","TRACKBAR")
    heightbottom=cv2.getTrackbarPos("HEIGHT BOTTOM","TRACKBAR")
    points=np.float32([(widthtop,heighttop),(wT-widthtop,heighttop)
                       ,(widthbottom,heightbottom),(wT-widthbottom,heightbottom)])    
    return points          

def drawpoints(img,points):
    for x in range(4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),15,(0,0,255),cv2.FILLED)
        
    return img

def getHistogram(img,minpercent=0.1,display=False,region=4):
    
    if region==1:
        histvalues=np.sum(img,axis=0)# tüm görüntünün ortalaması alınacak
    else:
        histvalues=np.sum(img[img.shape[0]//region:,:],axis=0)#görüntünün 1/4 ünün ort alınacak
        
    
    
    maxvalue=np.max(histvalues) 
    
    minvalue=minpercent*maxvalue
    #histogram değerlerinin minimum değerden büyük eşit olduğu indexleri buluyoruz
    indexarray=np.where(histvalues>=minvalue) 
    #indexarray ortalamasını alarak orta nokta tespiti
    basepoint=int(np.average(indexarray))
    
    
    if(display):
        imghist=np.zeros((img.shape[0],img.shape[1],3),np.uint8)
        # print(imghist)
        for x,intensity in enumerate(histvalues):
            cv2.line(imghist,(x,img.shape[0]),(x,img.shape[0]-intensity//255//region),(0,255,255),1)
            cv2.circle(imghist,(basepoint,img.shape[0]),30,(255,255,0),-1)
    
        return basepoint,imghist
    return basepoint     
    
    
    
    
    
    
    
    
