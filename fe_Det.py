import numpy as np
import cv2
import time
import requests, time, thread

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

    while(1):
       face = {widthtag: width, heighttag: height ,posxtag: posx, posytag:posy}
       r = requests.post('http://requestb.in/1bbag281', params=face)
       print r.status_code
       print r.content

try:
   thread.start_new_thread( send_postrequest, () )
except:
   print "Error: unable to start thread"


cap = cv2.VideoCapture(0)
if not cap.isOpened()  :
    print("can't open the camera")

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        width = w
        height = h
        posx = x
        posy = y


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
