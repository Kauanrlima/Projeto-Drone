#Main code 
import time
from djitellopy import tello
import pygame as pg
import test 

dr = tello.Tello()
#dr.connect()
test.keyboard()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            dr.land()
            running = False
        if event.type == pg.KEYDOWN:
            vals = test.keyboard.KeyBoardInput('LEFT','RIGHT','UP','DOWN','w','s','a','d')
            dr.send_rc_control(vals[0],vals[1],vals[2],vals[3])

