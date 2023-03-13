import cv2
import numpy as np
import utilities


curvelist=[]
avgvalue=10


def getlanecurve(img,display=1):
    
    imgcopy=img.copy()
    imgresult=img.copy()
    
    ### 1.KISIM THRESHOLD FONKSİYONU ÇAĞIRARAK THRESHOLD İŞLEMİ ve CLOSİNG YAPIYORUZ ###
    imgthresh=utilities.thresholding(img)
    #hsv renklerini ayarladığımız maskelenmiş videoumuzu aldık
    
    ### 2.KISIM WARPİMG FONKSİYONUNU ÇAĞIRARAK KUŞ BAKIŞI GÖRÜNÜME ÇEVİRİORUZ ###
    hT,wT,c=img.shape
    points=utilities.valtrackbars()
    imgwarp=utilities.warpimg(imgthresh,points,wT,hT)
    imgwarppoints=utilities.drawpoints(imgcopy,points)
    # cv2.imshow("kirpma",imgwarp)
    
    ### 3.KISIM HİSTOGRAM ###
    
    middlepoint,imghist=utilities.getHistogram(imgwarp,display=True,minpercent=0.5,region=4)
    
    curveaveragepoint,imghist=utilities.getHistogram(imgwarp,display=True,minpercent=0.9)
    
    curveraw=curveaveragepoint-middlepoint#ortalama değeri orta noktadan çıkarıyoruz

    ### 4.KISIM GÜRÜLTÜLÜ DEĞERLERİ AZALTMA İŞLEMİ###
    
    curvelist.append(curveraw)
    
    if len(curvelist)>=avgvalue:
        curvelist.pop(0)#LİSTENİN  10 DEĞERİNEN FAZLA AŞILMASINI İSTEMİYORUZ
    curve=int(sum(curvelist)/len(curvelist))
    

    # ### 5.KISIM GÖSTERİM ###
    if display==1:
        imginversewarp=utilities.warpimg(imgwarp,points,wT,hT,inverse=True)
        imginversewarp=cv2.cvtColor(imginversewarp,cv2.COLOR_GRAY2BGR)
        imginversewarp[0:hT//3,0:wT]==0,0,0
        imglanecolor=np.zeros_like(img)#videomuzun boyutlarında ve tipinde matris oluşturduk
        imglanecolor[:]=    0,5,255 #şerit rengi kırmızı olarak seçtik
        imglanecolor=cv2.bitwise_and(imginversewarp,imglanecolor)
        imgresult=cv2.addWeighted(imgresult,0.5,imglanecolor,1,0)
        ##alfa  değeri transparanlık değeri(1.değer)-0-1 arası değiştirilebilir,2.değer geçiş değeri
        midy=utilities.getHistogram(img,minpercent=0.1,display=False,region=1)
        cv2.putText(imgresult,str(curve),(wT//2 -80 ,85),cv2.FONT_HERSHEY_COMPLEX,2,(0,10,250),5)
        cv2.line(imgresult,(wT // 2,midy),(wT//2+(curve*3),midy),(0,0,0),5)
        cv2.line(imgresult,((wT//2+(curve*3)),midy), (wT//2+(curve*3),midy),(0,0,255),5,)
           
        for i in range(-30,30):
            w=wT//10
            cv2.line(imgresult,(w*i +int(curve//50),midy-10),
                      (w*i+int(curve//50),midy+10),(0,0,255),2) 
        cv2.imshow("result",imgresult)
        cv2.imshow("lanecolor",imglanecolor)
       
         
                 
   
    cv2.imshow("warp",imgwarp)
    # cv2.imshow("warppoints",imgwarppoints)
    ## değerleri -1 1 aralğına normalize ediyoruz  ##
    cv2.imshow("histogram",imghist)
    curve=curve/10
    # if curve>1: curve==1
    # if curve<1: curve==-1
        
    return curve

if __name__=='__main__':
    
    cam=cv2.VideoCapture('lane.mp4')
    
    initialtrackbarval=[0,135,0,240]
    
    utilities.initiliazetrackbar(initialtrackbarval)
    framecounter=0
    curvelist=[]
    while True:
        
        framecounter+=1
        if cam.get(cv2.CAP_PROP_FRAME_COUNT)==framecounter:
            cam.set(cv2.CAP_PROP_POS_FRAMES,0)
            framecounter=0
            
        _,img=cam.read()
        img=cv2.resize(img,(480,240))
        curve=getlanecurve(img,display=1)
        print(curve)
    
        
        if cv2.waitKey(1)==ord("q"):
            cam.release()
            cv2.destroyAllWindows()
        
         