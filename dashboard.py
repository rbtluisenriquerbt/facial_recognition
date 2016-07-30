import numpy as np
import cv2
import requests


cap = cv2.VideoCapture(0)
kernel = np.ones((5,5), np.uint8)
cxpast=0
cypast=0
dashboard = np.zeros((500,500,3), np.uint8)
i=0
def draw_circle(xpas,ypast,x,y):
	#cv2.circle(dashboard,(x,y),3,(255,0,0),-1)	
	cv2.line(dashboard,(xpas,ypast),(x,y),(255,0,0),10)

while 1:
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
    	lower_blue = np.array([110,50,50])
    	upper_blue = np.array([130,255,255])
		
	
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	
	res = cv2.bitwise_and(frame,frame, mask= mask)

	img_erosion = cv2.erode(res, kernel, iterations=4)
	rgb = cv2.cvtColor(img_erosion, cv2.COLOR_HSV2BGR)
	imgray =cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)

	#cv2.imshow('Imagen Filtrada',rgb)
	fimg=cv2.flip(dashboard,1)
	cv2.imshow('Dasboard',fimg)

 	ret,thresh = cv2.threshold(imgray,0,255,0)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	if len(contours) > 0:
	    	cnt = contours[0]
 		M = cv2.moments(cnt)
		if M['m00']!=0:
			cx = int(M['m10']/M['m00'])
 			cy = int(M['m01']/M['m00'])
			#print 'x= ' + str(cx) + ', y= ' + str(cy)
			if i!=0 :
				draw_circle(cxpast,cypast,cx,cy)
				
			i=i+1;
			cxpast=cx
			cypast=cy
	

		
	

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
	
cap.release()
cv2.destroyAllWindows()

