import numpy as np
import cv2
import time
import requests, time, thread
import json

face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_eye.xml')

def send_postrequest():
    global widthtag, heighttag, posxtag, posytag
    global width, height, posx, posy
    widthtag = 'width'
    heighttag = 'height'
    posxtag = 'posx'
    posytag = 'posy'
    width=0
    height=0
    posx = 0
    posy = 0
    time.sleep(0.3)

    while(1):
       face = {widthtag: int(width),
               heighttag: int(height) ,posxtag: int(posx), posytag:int(posy)}
       r = requests.post('http://requestb.in/1bbag281', data=json.dumps(face))
       print r.status_code
       print r.content

try:
   thread.start_new_thread( send_postrequest, () )
except:
   print "Error: unable to start thread"


cap = cv2.VideoCapture(1)
if not cap.isOpened()  :
    print("can't open the camera")

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print len(faces)
    if len(faces):
        print "entro"
        for (x,y,w,h) in faces:

            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            if (w > 40 and h > 40):
                width = w
                height = h
                posx = x
                posy = y
            else:
                width = 0
                height = 0
                posx = 0
                posy = 0
    else:
        width = 0
        height = 0
        posx = 0
        posy = 0

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
