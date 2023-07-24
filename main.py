import pyautogui as pg
import time
time.sleep(5)
txt = open('animals.txt','r')

a = "t!help"


for i in txt:
    # pg.write(a +' ' + i)
    pg.write(a +' '+ i)
    time.sleep(1)
    pg.press('Enter')