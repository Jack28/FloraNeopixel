#!/usr/bin/env python2

import strip
from time import sleep


s=strip.LEDstrip('/dev/ttyACM0',16,1)

s.clear()

s.show()

s.layer[0].setRing(0,0,0)

while True:
    for i in range(0,250):
        (r,g,b)=s.layer[0].wheel(i,1,250)
        s.layer[0].setRing(r,g,b)
        s.show()
        sleep(.1)
