### Main code of the project

'''
importação do pygame para criar os controles do drone e 
importação do djitellopy para a comunicação com o drone
'''
import pygame as pg
from djitellopy import tello

## Conexão com o drone e definição de variável que refere-se ao drone
#dr = tello.Tello()
#dr.connect()

##Criação de uma classe para representar o código voltado ao teclado
class keyboard:


 
        
    screen = pg.display.set_mode((100,100))
    
    running = True
    lr, fb, up, yv = 0,0,0,0
    keys = pg.key.get_pressed()
    speed = 20
    while running:
        for event in pg.event.get():
           if event.type == pg.QUIT:
                running = False
           if event.type == pg.KEYDOWN:
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
    vals = [lr,fb,up,yv]
    print(vals)                
   
    
        
        