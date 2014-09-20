#!/usr/bin/env python2

import strip
from time import sleep
import random


s=strip.LEDstrip('/dev/ttyACM0',16,1)

s.clear()

s.show()

s.layer[0].setRing(0,0,0)

start=0
while True:
    s.layer[0].setBits(range(start,start+3),0,0,0)
    start=random.randint(0,16-3)
    s.layer[0].setBits(range(start,start+3),0xff,0xff,0xff)
    s.show()
    sleep(.1)
