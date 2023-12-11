#Main code 
import time
import pygame as pg
import test 

dr = test.Drone()
#dr.connect()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # dr.tello.land()
            running = False
        if event.type == pg.KEYDOWN:
            vals = dr.KeyBoardInput('LEFT','RIGHT','UP','DOWN','w','s','a','d')
            dr.tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

