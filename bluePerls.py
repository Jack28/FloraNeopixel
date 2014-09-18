#!/usr/bin/env python2

import strip
from time import sleep


s= strip.LEDstrip('/dev/ttyACM0',16,3)

s.clear()
#s.setRing(0,0,240)#160-160/16*i)
s.layer[0].setBits([0],0,0,50)
s.layer[1].setBits([1,2,3,4],0,0,50)

s.layer[2].setRing(10,0,0)


s.show()

while True:
    for i in range(0,10):
        s.layer[0].shift(1)
        s.show()
        sleep(0.1)
    s.layer[0].shift(5)
    s.layer[1].shift(-1)
    s.show()
