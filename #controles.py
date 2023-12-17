#Main code 
import time
import pygame as pg
import test 
import cv2
import class_camera

dr = test.Drone()
video = class_camera.Camera()

running = True
while running:
	video.main()
	
	for event in pg.event.get():
		
		if event.type == pg.QUIT:
			running = False
			dr.tello.land()
		if event.type == pg.KEYDOWN:
			vals = dr.KeyBoardInput('LEFT','RIGHT','UP','DOWN','w','s','a','d','x','z','c','v')
			dr.tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
		if event.type == pg.KEYUP:
			dr.tello.send_rc_control(0,0,0,0)

