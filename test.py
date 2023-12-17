'''
importação do pygame para criar os controles do drone e 
importação do djitellopy para a comunicação com o drone
'''

from djitellopy import tello
import pygame as pg
import time

class Drone:

    def __init__(self):
        self.tello = tello.Tello()
        self.screen = pg.display.set_mode((100, 100))
        self.tello.connect()
        self.tello.streamon()
    
    def KeyBoardInput(self, b1='LEFT', b2='RIGHT', b3='UP', b4='DOWN', b5='w', b6='s', b7='a', b8='d',b9='x', b10='z', b11='c', b12='v', speed=50):
        lr, fb, up, yv = 0, 0, 0, 0
        keys = pg.key.get_pressed()
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
        
        time.sleep(0.05)
        return [lr, fb, up, yv]

                
   
    
        
        