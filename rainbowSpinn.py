#!/usr/bin/env python2

import strip
from time import sleep


s= strip.LEDstrip('/dev/ttyACM0',16,1)

s.clear()

s.show()


newLayer2=strip.LEDlayer(s)

s.layer[0].setBits(range(0,16),0,255,0)
s.layer[0].rainbow(1)
newLayer2.setBits(range(0,8),0,0,0)
newLayer2.rainbow(1)


while True:
    s.layer[0].transition(newLayer2)
    s.show()

    newLayer2.shift(1)
    s.show()
