'''
Import das biblioteclas de processamento de imagens e de controle do drone Tello
'''
import cv2
import djitellopy as tello

#função para conectar com o drone
dr = tello.Tello()

class Camera:

    def __init__(self):
        self.capture = dr.get_frame_read().frame

    def cascata(self,img, f, p):
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, f, p)
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
        if len(self.myFaceArea) != 0:
            i = myFaceArea.index(max(myFaceArea))
            return img, [myFaceList[i],myFaceArea[i]]
        else :
            return img, [[0,0], 0]

    def main(self, window_name="Frame", width=360, height=240, delay=1, f=1.2, p =5):

        self.cap = dr.get_frame_read().frame
        img = cv2.resize(self.cap, (width,height))
        faces = Camera.cascata(self,img, f, p)
        img = Camera.trackFace(self,faces,img)
        cv2.imshow(window_name, img[0])
        cv2.waitKey(delay)
