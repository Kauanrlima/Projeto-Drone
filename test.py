'''
importação do pygame para criar os controles do drone e 
importação do djitellopy para a comunicação com o drone
importação do time para criar um delay
importação do cv2 para comunicação com a câmera do drone
'''

from djitellopy import tello
import pygame as pg
import time
import cv2

'''
Class related to the drone, most of the connection and key assignments are done here 
'''
class Drone:
    '''
    The init function sets the first things to be done when calling the Class drone
    The self.tello variable sets the way to refer to the drone's functions such as connect, streamon etc.
    The self.screen variable is to set the display from pygame since its required to start using the library
    self.tello.connect() refers to the function of the tello drone that connects the drone to the code
    self.tello.streamon() refers to the function of the tello drone that initializes the streaming mode(in other words it starts the drone camera)
    '''

    def __init__(self):
        self.tello = tello.Tello()
        self.screen = pg.display.set_mode((100, 100))
        self.capture = cv2.VideoCapture(0)
        # self.tello.connect()
        # self.tello.streamon()

    '''
    The KeyBoardInput function allows the user to choose the buttons for the basic controls and the speed of the drone
    Fistly, there are 12 parameters going from b1 to b12 that refers to the buttons of the keyboard, all of them have
    already assigned keys however the user is able to change them by calling the function and typping the parameter and the 
    key of interest. The b1 and b2 are the left and right velocity of the drone, the b3 and b4 are for the forward and backward velocity,
    the b5 and b6 are for the up and down velocity, the b7 and b8 velocity are for the yaw velocity, the b9 is to command the drone to land,
    the b10 is to command the drone to take off, the b11 is to start streaming and b12 is to end streaming
    The last parameter refers to the drone's speed when a button is pressed, it also can be changed by the user
    '''

    
    def KeyBoardInput(self, b1='LEFT', b2='RIGHT', b3='UP', b4='DOWN', b5='w', b6='s', b7='a', b8='d',b9='x', b10='z', b11='c', b12='v', speed=50):
        '''
        set lr,fb,up,yv variables referring to the drone's velocity values (start with 0 so the buttons can change it)
        assigned a variable to represent the function from pygame "get_pressed" that returns a sequence of boolean values representing the 
        state of every key on the keyboard. 
        '''
        
        lr, fb, up, yv = 0, 0, 0, 0
        keys = pg.key.get_pressed()
        
        #changed the format of the buttons to match the pg format using the getattr function

        b1 = getattr(pg,'K_{}'.format(b1))
        b2 = getattr(pg,'K_{}'.format(b2))
        b3 = getattr(pg,'K_{}'.format(b3))
        b4 = getattr(pg,'K_{}'.format(b4))
        b5 = getattr(pg,'K_{}'.format(b5))
        b6 = getattr(pg,'K_{}'.format(b6))
        b7 = getattr(pg,'K_{}'.format(b7))
        b8 = getattr(pg,'K_{}'.format(b8))
        b9 = getattr(pg,'K_{}'.format(b9))
        b10 = getattr(pg,'K_{}'.format(b10))
        b11 = getattr(pg,'K_{}'.format(b11))
        b12 = getattr(pg,'K_{}'.format(b12))

        #using a sequence of ifs to "change" the value of the velocities 

        if keys[b1]:
            lr = -speed
        if keys[b2]:
            lr = speed
        if keys[b3]:
            fb = speed
        if keys[b4]:
            fb = -speed
        if keys[b5]:
            up = speed
        if keys[b6]:
            up = -speed
        if keys[b7]:
            yv = -speed
        if keys[b8]:
            yv = speed
        if keys[b9]:
            self.tello.land()
        if keys[b10]:
            self.tello.takeoff()
        if keys[b11]:
            self.tello.streamon()
        if keys[b12]:
            self.tello.streamoff()

        #sets a delay for when a button is pressed
            
        time.sleep(0.05)

        #returns the values of lr,fb,up,yv

        return [lr, fb, up, yv]
        
    
    '''
    O método cascata utiliza o metoda da viola jones para reconhecimento facial
    faceCascade vai receber o caminho para encontra o arquivo 'haarcascade_frontalface_default.xml', esse arquivo é instalado junto com a biblioteca OpenCV
    imgGray transforma a imagem já processada pela função get_frame_read().frame de BGR (padrão do OpenCV) para escala cinza (escala que permite o reconhecimento pelo
    método da Viola Jones)
    faces = executa o arquivo 'haarcascade_frontalface_default.xml' para imgGray, assim a função retorna as "faces" identificadas, com coordenadas iniciais das faces 
    (x,y) e finais (x+w,w+h)
    '''

    def cascata(self,img):
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)
        return faces 
    '''
    O método trackFace, ao receber os valores de faces e img, cria um retângulo ao redos da face 
    além de criar uma lista com o cálculo da área do retângulo e das coordenadas de seu centro (cx,cy)
    '''
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
        
    '''
    A função main executa os métodos anteriores de maneira que processa e lê a imagem capturada pelo drone; redimensiona a imagem preocessada; utiliza o 
    método da viola jones para retornar as faces; as faces são contornadas por um retângulo;  por fim, essa imagem é mostrada em uma janela.
    '''

    def main(self, window_name="Frame", width=360, height=240, delay=1):

        # self.cap = self.tello.get_frame_read().frame
        _, self.cap = self.capture.read()
        img = cv2.resize(self.cap, (width,height))
        faces = Drone.cascata(self,img)
        img = Drone.trackFace(self,faces,img)
        cv2.imshow(window_name, img[0])
        cv2.waitKey(delay)

    '''
    def pygame(self,event,vals):
        if event.type == pg.KEYDOWN:
            self.tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        if event.type == pg.KEYUP:
            self.tello.send_rc_control(0,0,0,0)
    '''        
                
   
    
        
        