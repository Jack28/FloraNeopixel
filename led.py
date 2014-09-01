#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()

strip.clear()
for i in range(0,16):
    strip.setBit(i,160/16*i,0,0)
strip.show()

for i in range(0,200):
    strip.shift(1)
    strip.show()
    sleep(.02)
