k = "kauan acho que funcionou"

import cv2
import time
import numpy as np
from djitellopy import tello

def drone(self):
    dr = tello.Tello()
    dr.connect()
    print(dr.get_battery())
    dr.streamon()
    dr.takeoff() 
    dr.send_rc_control(0,0,0,0)
    time.sleep(2.2)


fbRange = [6200,6800]
pid = [[0.4, 0.4, 0]]
pError = 0 # previous error
w,h = 360, 240

cap = cv2.VideoCapture(0)

def findFace(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)

    myFaceList = []
    myFaceArea = []

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255), 2)
        cx = x + w //2
        cy = y + h //2
        area = w * h
        cv2.circle(img,(cx,cy), 5, (0,255,0), cv2.FILLED)
        myFaceList.append([cx,cy])
        myFaceArea.append(area)
    if len(myFaceArea) != 0:
        i = myFaceArea.index(max(myFaceArea))
        return img, [myFaceList[i], myFaceArea[i]]
    else :
        return img, [[0,0], 0]
    
def trackFace(me,info,w,pid,pError):
    area = info [1]
    x,y = info[0]
    error = x - w//2
    speed = pid[0]* error + pid[1] * (error - pError)
    speed = int(np.clip(speed,-100,100))
    fb = 0 
    if area > fbRange[0] and area < fbRange[1]: 
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0: 
        fb = 20


    if x == 0:
        speed = 0
        error = 0
        
    drone.send_rc_control(0,fb,0,speed)
      

while True:
    img = drone.get_frame_read().frame
    img =cv2.resize(img,(w,h)) 
    img, info = findFace(img)
    pError = trackFace(info,w,pid,pError)
    print("center",info[0], "Area",info[1])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break