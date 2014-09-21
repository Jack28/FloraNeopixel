#!/usr/bin/env python2

import strip
from time import sleep
from threading import *
import os


s= strip.LEDstrip('/dev/ttyACM0',16,2)

s.clear()
#s.setRing(0,0,240)#160-160/16*i)
s.layer[0].setBits([0,1,2,3],50,0,0)
s.layer[1].setBits([0,1,2,3],0,50,0)

s.layer.append(strip.LEDlayer(s))
s.layer[2].setBits([0,1,2,3],00,00,50)

s.show()

def red():
    while True:
        s.layer[0].shift(1)
        s.show()
        sleep(0.18)

def green():
    while True:
        s.layer[1].shift(-2)
        s.show()
        sleep(0.2)

def blue():
    while True:
        s.layer[2].shift(-1)
        s.show()
        sleep(0.22)

t1=Thread(target=red)
t1.daemon=True
t1.start()

t2=Thread(target=blue)
t2.daemon=True
t2.start()

green()

os._exit(0)
