import cv2
import numpy as np
from djitellopy import tello

dr = tello.Tello()
img = dr.get_frame_read().frame

class drone:
    def __init__(self,img,speed):
        self.speed = speed
        self.img = img
        
    
    def findFace(self,faces):
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)
        

    def trackFace(self,area,x,w,fb):
        fb = 0
        pid = [[0.4, 0.4, 0]]
        error = x - w//2
        speed = pid[0]* error + pid[1] * (error - pError)
        speed = int(np.clip(self.speed,-100,100))
        
        return dr.send_rc_control(0,fb,0,self.speed)
