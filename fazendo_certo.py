import cv2
import numpy as np
from djitellopy import tello
import keyboard as kb


class controlador:
    def __init__(self,drone,tecla):
        self_drone = tello.Tello()
        self_tecla = {}

    def comandos_basicos(self,drone):
        self.connect(drone)
        self.streamon(drone)
        self.takeoff(drone) 

    def keypress(self,tecla):
        self.kb.read_key == "tecla"

    def movimentacao(self)
         self.keypress(drone) = send_rc_control(vals[0], vals[1], vals[2], vals[3])

