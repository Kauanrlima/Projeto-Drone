### Main code of the project
import pygame as pg
from djitellopy import tello

dr = tello.Tello()
dr.connect()

class keyboard:
    def __init__(self):
        self.pg.init()
    
    screen = pg.display.set_mode((100,100))
      
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
             running = False
            if event.type == pg.KEYDOWN:
                def KeyBoardInput():
                    lr, fb, up, yv = 0,0,0,0
                    speed = 20
                    keys = pg.key.get_pressed()
                    if keys[pg.K_LEFT]:
                        lr = -speed
                    if keys[pg.K_RIGHT]:
                        lr = speed
                    if keys[pg.K_UP]:
                        fb = speed
                    if keys[pg.K_DOWN]:
                        fb = -speed
                    if keys[pg.K_w]:
                        up = speed
                    if keys[pg.K_s]:
                        up = -speed
                    if keys[pg.K_a]:
                        yv = -speed
                    if keys[pg.K_d]:
                        yv = speed
                    return [lr,fb,up,yv]
                vals = KeyBoardInput()
                dr.send_rc_control(vals[0],vals[1],vals[2],vals[3])
                print(vals)
   
    
        
        