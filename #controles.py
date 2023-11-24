#controles 
from djitellopy import tello
from test import keyboard as kb

dr = tello.Tello()
dr.connect()
print(dr.get_battery())

dr.takeoff()


while True:
    dr.send_rc_control(0,0,0,0)