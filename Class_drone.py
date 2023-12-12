import cv2
import numpy as np
from djitellopy import tello

class drone:
    def __init__(self,img,speed):
        self.speed = speed
        self.img = img
    
    
    def findFace(self,img,faceCascade,imgGray,faces):
        self.faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)

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

    def trackFace(self,info,w,pid,pError):
        area = info [1]
        x,y = info[0]
        error = x - w//2
        speed = pid[0]* error + pid[1] * (error - pError)
        speed = int(np.clip(speed,-100,100))
        fb = 0 
        if area > 6200 and area < 6800: 
            fb = 0
        elif area > 6800:
            fb = -20
        elif area < 6200 and area != 0: 
            fb = 20
        
        
        if x == 0:
            speed = 0
            error = 0
        
        dr.send_rc_control(0,fb,0,speed)