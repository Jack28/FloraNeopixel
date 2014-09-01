#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()

strip.clear()
for i in range(0,16):
    strip.setBit(i,0,0,160-160/16*i)
strip.show()

while True:
    strip.shift(1,5,0.1)
    strip.shift(-1,5,0.1)
    strip.shift(1)
    strip.show()
    sleep(0.1)
