#controles 
from djitellopy import tello
from test import keyboard as kb
import test as kb

dr = tello.Tello()
dr.connect()
print(dr.get_battery())

dr.takeoff()


