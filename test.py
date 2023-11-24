### Main code of the project

import pygame as pg


class keyboard:
    def __init__(self):
        self.pg.init()
    
    screen = pg.display.set_mode((400,400))
    
    running = True
    while running:
        for event in pg.event.get():
         if event.type == pg.QUIT:
             running = False
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                print('a')
            if keys[pg.K_RIGHT]:
                print('d')
            if keys[pg.K_UP]:
                print('w')
            if keys[pg.K_DOWN]:
                print('s')
