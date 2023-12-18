#Main code 
'''
importa o pygames pra criar uma saida da janela
importa o arquivo test
'''

import pygame as pg
import test 

'''
objeto da classe Drone
'''
dr = test.Drone()

'''
Criação de uma variãvel running para dar dar o start no looping do código
'''

running = True
while running:
	'''
	puxa a função main da classe Drone
	'''
	dr.main()
	'''
	definição de evento para travar a janela do pygame quando sair
	'''
	for event in pg.event.get():
		
		if event.type == pg.QUIT:
			running = False
			dr.tello.land()
	'''
	puxa a função pygame da classe Drone
	'''
	dr.pygame()
    
