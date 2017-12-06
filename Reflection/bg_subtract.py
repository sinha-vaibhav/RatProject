import numpy as np
import cv2
cap = cv2.VideoCapture('../Videos/Video_Object_1_Rat.mp4')

background = cv2.imread('avg_bg_1.png',0)
detector = cv2.SimpleBlobDetector_create()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
while(1):
    ret, frame = cap.read()
    if not ret:
    	break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sub = frame - background
    
    fgmask = cv2.morphologyEx(sub, cv2.MORPH_OPEN, kernel)
    #keypoints = detector.detect(fgmask)
   
    #im_with_keypoints = cv2.drawKeypoints(fgmask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.imshow('frame',fgmask)
#cv2.destroyAllWindows()