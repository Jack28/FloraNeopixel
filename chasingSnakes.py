#!/usr/bin/env python2

import strip
from time import sleep
from threading import *
import os


s=strip.LEDstrip('/dev/ttyACM0',16,2)

s.clear()


redSnake  =strip.LEDlayer(s)
greenSnake=strip.LEDlayer(s)
blueSnake =strip.LEDlayer(s)


s.layer[0].setBits([0,1,2,3],50,0,0)
redSnake.setBits  ([0,1,2,3],50,0,0)

s.layer[1].setBits([0,1,2,3],0,50,0)
greenSnake.setBits([0,1,2,3],0,50,0)

s.layer.append(strip.LEDlayer(s))
s.layer[2].setBits([0,1,2,3],0,0,50)
blueSnake.setBits ([0,1,2,3],0,0,50)


s.show()

def red():
    while True:
        redSnake.shift(1)
        s.layer[0].transition(redSnake,steps=3)
        sleep(0.02)

def green():
    while True:
        greenSnake.shift(-2)
        s.layer[1].transition(greenSnake,steps=3)

def blue():
    while True:
        blueSnake.shift(-1)
        s.layer[2].transition(blueSnake,steps=2)

t1=Thread(target=red)
t1.daemon=True
t1.start()

t2=Thread(target=blue)
t2.daemon=True
t2.start()

green()

os._exit(0)
