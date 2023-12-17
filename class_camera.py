
import cv2
import numpy as np
class Camera:

    
    def __init__(self,cap):
        _, self.cap = cap.read()
   
    def cascata(self,img):
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)
        return faces 
    
    def trackFace(self,faces,img):
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
            return img, [myFaceList[i],myFaceArea[i]]
        else :
            return img, [[0,0], 0]
        

    def main(self):
        while True:
            _, self.cap = cap.read()
            img = cv2.resize(self.cap, (360,240))
            faces = Camera.cascata(self,img)
            img = Camera.trackFace(self,faces,img)
            cv2.imshow("Frame", img[0])
            cv2.waitKey(1)

cap = cv2.VideoCapture(0)
kauan =Camera(cap)
kauan.main()








    













 
