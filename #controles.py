#Main code 
'''
importa o pygames pra criar uma saida da janela
importa o arquivo test
'''

import pygame as pg
import test
import cv2 


# objeto da classe Drone

dr = test.Drone()

# Criação de uma variével running para dar dar o start no looping do código


running = True
while running:
	
	# puxa a função main da classe Drone
	
	#dr.main()
	
	# definição de evento para travar o código e o que acontece se apertar e soltar um botão
	
	for event in pg.event.get():
		
		if event.type == pg.QUIT:
			running = False
			cv2.destroyAllWindows()
			dr.tello.land()
		if event.type == pg.KEYDOWN:
			vals = dr.KeyBoardInput()
			dr.tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
		if event.type == pg.KEYUP:
			dr.tello.send_rc_control(0,0,0,0)
		
		'''
		vals = dr.KeyBoardInput()
		
		dr.pygame(event,vals)
		'''