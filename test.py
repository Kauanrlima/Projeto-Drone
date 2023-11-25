### Main code of the project

'''
importação do pygame para criar os controles do drone e 
importação do djitellopy para a comunicação com o drone
'''
import pygame as pg
from djitellopy import tello

## Conexão com o drone e definição de variável que refere-se ao drone
dr = tello.Tello()
dr.connect()

##Criação de uma classe para representar o código voltado ao teclado
class keyboard:

    #Criação de uma definição inicializadora para rodar o pygame
    def __init__(self):
        self.pg.init()
    
    #Criação de uma janela para o funcionamento do pygame
    screen = pg.display.set_mode((100,100))
      
    #Variável running que permite que o pygame rode, além de servir como um meio de fechar a janela
    running = True
    while running:
        for event in pg.event.get():

            #Evento que ocorre quando é clicado o "x" da janela do pygame 
            #no caso fechará a janela e encerrará o código
            
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
                    if keys[pg.K_w]:
                        up = speed
                    if keys[pg.K_s]:
                        up = -speed
                    if keys[pg.K_a]:
                        yv = -speed
                    if keys[pg.K_d]:
                        yv = speed
                    return [lr,fb,up,yv]
                vals = KeyBoardInput()
                dr.send_rc_control(vals[0],vals[1],vals[2],vals[3])
                
   
    
        
        