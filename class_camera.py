...
Foi importado as biblitecas open CV e djitellopy, para, respectivamente
reconhecer imagens e controlar os comandos do drone pelo computador
...
import cv2
import djitellopy as tello

class Camera:

    def __init__(self):
        self.capture = tello.Tello.get_frame_read().frame

        
    def cascata(self,img):
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)
        return faces 
    
    def trackFace(self,faces,img):
        self.myFaceList = []
        self.myFaceArea = []

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255), 2)
            cx = x + w //2
            cy = y + h //2
            area = w * h
            cv2.circle(img,(cx,cy), 5, (0,255,0), cv2.FILLED)
            self.myFaceList.append([cx,cy])
            self.myFaceArea.append(area)
        if len(self.myFaceArea) != 0:
            i = self.myFaceArea.index(max(self.myFaceArea))
            return img, [self.myFaceList[i],self.myFaceArea[i]]
        else :
            return img, [[0,0], 0]
        

    def main(self, window_name="Frame", width=360, height=240, delay=1):

        _, self.cap = self.capture
        img = cv2.resize(self.cap, (width,height))
        faces = Camera.cascata(self,img)
        img = Camera.trackFace(self,faces,img)
        cv2.imshow(window_name, img[0])
        cv2.waitKey(delay)










    













 
