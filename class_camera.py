import cv2
import djitellopy as tello
import test

dr = test.Drone()

class camera:
    def __init__(self):
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
    
'''
while True:
    img = dr.get_frame_read().frame
    img =cv2.resize(img,(w,h)) 
    img, info = findFace(img)
    print("center",info[0], "Area",info[1])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        dr.land()
        break
'''