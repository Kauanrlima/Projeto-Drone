#Main code 
import time
import pygame as pg
import test 

dr = test.Drone()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            dr.tello.land()
        if event.type == pg.KEYDOWN:
            vals = dr.KeyBoardInput('LEFT','RIGHT','UP','DOWN','w','s','a','d','x','z')
            dr.tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        if event.type == pg.KEYUP:
            dr.tello.send_rc_control(0,0,0,0)

