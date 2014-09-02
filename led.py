#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()

strip.clear()
#strip.setRing(0,0,240)#160-160/16*i)
strip.rainbow()
strip.show()

while True:
#    strip.shift(1,5,0.1)
#    strip.shift(-1,5,0.1)
#    strip.shift(1)
#    strip.show()
#    sleep(0.1)
    strip.dim(-130,0.01,8)
    strip.dim(50,0.01,-8)
    strip.setRing(0,0,240)

