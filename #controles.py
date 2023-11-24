#controles 
from djitellopy import tello
from test import keyboard as kb
import test as kb

dr = tello.Tello()
dr.connect()
print(dr.get_battery())

dr.takeoff()



vals = kb.KeyBoardInput()
dr.send_rc_control(vals[0],vals[1],vals[2],vals[3])
