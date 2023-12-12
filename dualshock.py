import Class_drone
import cv2
from djitellopy import tello

dr = tello.Tello()

def findFace(img, faces):
    myFaceListC = []
    myFaceArea = []
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255), 2)
        cx = x + w //2
        cy = y + h //2
        area = w * h
        cv2.circle(img,(cx,cy), 5, (0,255,0), cv2.FILLED)
        myFaceListC.append([cx,cy])
        myFaceArea.append(area)
    if len(myFaceArea) != 0:
        i = myFaceArea.index(max(myFaceArea))
        return img, [myFaceListC[i], myFaceArea[i]]
    else :
        return img, [[0,0], 0], area,x

def trackFace(area,x,w,fb):
    
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
        
    return dr.send_rc_control(0,fb,0,speed)

while True:
    img = dr.get_frame_read().frame
    img =cv2.resize(img,(w,h)) 
    img, info = findFace(img)
    pError = trackFace(info,w,pid,pError)
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        dr.land()
        break
