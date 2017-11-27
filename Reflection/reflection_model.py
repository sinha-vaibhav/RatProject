import numpy as np
import cv2

#np.set_printoptions(threshold=np.nan)
cap = cv2.VideoCapture('../Videos/Video_Object_1_Rat.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
detector = cv2.SimpleBlobDetector_create()



fps = 30
capSize = (320,240)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 
vout = cv2.VideoWriter()
success = vout.open('output.mov',fourcc,fps,capSize,False) 


kernel_dil = np.ones((5,5),np.uint8)
while(1):
    ret, frame = cap.read()
    if not ret:
    	break
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    
    fgmask = cv2.blur(fgmask,(3,3))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    #vout.write(fgmask)
    keypoints = detector.detect(fgmask)
   
    im_with_keypoints = cv2.drawKeypoints(fgmask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('frame',fgmask)
    cv2.imshow('frame2',frame)

    print "FGMASK = ",fgmask
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.imshow('frame',fgmask)
vout.release()
vout = None
cv2.destroyAllWindows()