### Main code of the project

import pygame as pg
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT)

class keyboard:
    def __init__(self):
        self.pg.init()
        self.pressed_keys = pg.key.get_pressed()
    
    screen = pg.display.set_mode((400,400))
    
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    print('a')
    
