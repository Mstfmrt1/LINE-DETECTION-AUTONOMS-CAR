import cv2

cam=cv2.VideoCapture(0)
    
def getimg(display=False):
    _,img=cam.read()
    img=cv2.resize(img,480,480)
        
    if display==True:
        cv2.imshow("kamera",img)
    return img
        
    


if __name__=="__main_":
    while True:
        img=getimg(True)
        
       
        
    
    
    
    
    