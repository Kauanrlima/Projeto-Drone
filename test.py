### Main code of the project

'''
importação do pygame para criar os controles do drone e 
importação do djitellopy para a comunicação com o drone
'''
import pygame as pg
from djitellopy import tello
import time

## Conexão com o drone e definição de variável que refere-se ao drone
dr = tello.Tello()
#dr.connect()

##Criação de uma classe para representar o código voltado ao teclado
class keyboard:

    #Criação de uma definição inicializadora para rodar o pygame
    def __init__(self):
        self.pg.init()
    
    #Criação de uma janela para o funcionamento do pygame
    screen = pg.display.set_mode((100,100))
    def KeyBoardInput(b1,b2,b3,b4,b5,b6,b7,b8):
        lr, fb, up, yv = 0,0,0,0
        speed = 20
        b1 = getattr(pg,'K_{}'.format(b1))
        b2 = getattr(pg,'K_{}'.format(b2))
        b3 = getattr(pg,'K_{}'.format(b3))
        b4 = getattr(pg,'K_{}'.format(b4))
        b5 = getattr(pg,'K_{}'.format(b5))
        b6 = getattr(pg,'K_{}'.format(b6))
        b7 = getattr(pg,'K_{}'.format(b7))
        b8 = getattr(pg,'K_{}'.format(b8))

        keys = pg.key.get_pressed()
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
        time.sleep(0.05)
        return [lr,fb,up,yv]
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            vals = keyboard.KeyBoardInput('LEFT','RIGHT','UP','DOWN','w','s','a','d')
            dr.send_rc_control(vals[0],vals[1],vals[2],vals[3])
                
   
    
        
        