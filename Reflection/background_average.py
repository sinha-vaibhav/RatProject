import cv2
import numpy as np
 
c = cv2.VideoCapture('../Videos/Video_Object_1_Rat.mp4')
_,f = c.read()
 
avg1 = np.float32(f)
avg2 = np.float32(f)
 
while(1):
    _,f = c.read()

    if f is None:
        break
     

    cv2.accumulateWeighted(f,avg1,0.1)
    cv2.accumulateWeighted(f,avg2,0.01)
     
    res1 = cv2.convertScaleAbs(avg1)
    res2 = cv2.convertScaleAbs(avg2)
 
    zcv2.imshow('img',f)
    cv2.imshow('avg1',res1)
    cv2.imshow('avg2',res2)
    k = cv2.waitKey(20)
    
    cv2.imwrite('avg_bg_1.png',res1)
    cv2.imwrite('avg_bg_2.png',res2)
    
    if k == 27:
        break
 
cv2.destroyAllWindows()
c.release()