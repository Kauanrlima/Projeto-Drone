### Main code of the project

import pygame as pg


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
                        return [lr,fb]
                    print(KeyBoardInput())
    
   
    
        
        