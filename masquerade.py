#!/usr/bin/env python2

import strip
from time import sleep


s=strip.LEDstrip('/dev/ttyACM0',16,2)

s.clear()

s.show()

s.layer[0].rainbow()
# mask
s.layer[1].setBits(range(0,16,2),-1000,-1000,-1000)

while True:
    s.layer[0].shift(1)
    s.layer[1].shift(1)
    s.show()
    sleep(0.3)

