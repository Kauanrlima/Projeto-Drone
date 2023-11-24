### Main code of the project

import pygame as pg


class keyboard:
    def __init__(self):
        self.pg.init()
        self.pressed_keys = pg.key.get_pressed()
        self.pg.quit()

    screen = pg.display.set_mode((400,400))
    
    run = True
    while run:
         for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    print('w')
                elif event.key == pg.K_DOWN:
                    print('s')
                elif event.key == pg.K_LEFT:
                    print('a')
                elif event.key == pg.K_RIGHT:
                    print('d')
