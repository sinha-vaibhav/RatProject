import numpy as np
import cv2
cap = cv2.VideoCapture('../Videos/Video_Object_1_Rat.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
detector = cv2.SimpleBlobDetector_create()

kernel_dil = np.ones((5,5),np.uint8)
while(1):
    ret, frame = cap.read()
    if not ret:
    	break
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    #fgmask = cv2.blur(fgmask,(3,3))
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    keypoints = detector.detect(fgmask)
   
    im_with_keypoints = cv2.drawKeypoints(fgmask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('frame',im_with_keypoints)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.imshow('frame',fgmask)
#cv2.destroyAllWindows()