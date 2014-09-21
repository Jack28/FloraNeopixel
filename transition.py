#!/usr/bin/env python2

import strip
from time import sleep


s=strip.LEDstrip('/dev/ttyACM0',16,1)

s.clear()

s.show()


newLayer2=strip.LEDlayer(s)
newLayer3=strip.LEDlayer(s)

s.layer[0].setBits(range(0,16),0,55,0)

newLayer2.setBits(range(0,8),0,0,0)
newLayer2.setBits(range(8,16),250,0,0)

newLayer3.setBits(range(0,16),0,55,0)


while True:
    s.layer[0].transition(newLayer2,steps=30)
    sleep(1)
    s.show()

    s.layer[0].transition(newLayer3,steps=30)
    s.show()
    sleep(1)

    newLayer2.shift(1)
