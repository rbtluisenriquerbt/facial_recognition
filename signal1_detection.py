
import numpy as np
import cv2

signal1_cascade = cv2.CascadeClassifier('signal1_cascade_v3.xml')
##RELLENAR AQUI


#this is the cascade we just made. Call what you want
#watch_cascade = cv2.CascadeClassifier('watchcascade10stage.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    signal1 = signal1_cascade.detectMultiScale(gray, 1.3, 5) ##CODIGO RECONOCIMIENTO

    for (x,y,w,h) in signal1:       ##CODIGO PARA DETECTRA
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print "Patron1"

    ##RELLENAR AQUI LAS DEMAS SENHALES

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
