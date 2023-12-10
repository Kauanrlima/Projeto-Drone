### Main code of the project

'''
importação do pygame para criar os controles do drone e 
importação do djitellopy para a comunicação com o drone
'''
import pygame as pg
import time

class keyboard:

    def __init__(self):
        self.screen = pg.display.set_mode((100,100))
        pg.key.set_repeat(500)

    
    def KeyBoardInput(b1,b2,b3,b4,b5,b6,b7,b8):
        lr, fb, up, yv = 0,0,0,0
        speed = 20
        keys = pg.key.get_pressed()
        b1 = getattr(pg,'K_{}'.format(b1))
        b2 = getattr(pg,'K_{}'.format(b2))
        b3 = getattr(pg,'K_{}'.format(b3))
        b4 = getattr(pg,'K_{}'.format(b4))
        b5 = getattr(pg,'K_{}'.format(b5))
        b6 = getattr(pg,'K_{}'.format(b6))
        b7 = getattr(pg,'K_{}'.format(b7))
        b8 = getattr(pg,'K_{}'.format(b8))

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

                
   
    
        
        