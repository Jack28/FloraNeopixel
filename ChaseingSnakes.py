#!/usr/bin/env python2

import strip
from time import sleep


s= strip.LEDstrip('/dev/ttyACM0',16,2)

s.clear()
#s.setRing(0,0,240)#160-160/16*i)
s.layer[0].setBits([0,1,2,3],0,0,50)
s.layer[1].setBits([0,1,2,3],0,50,50)

s.layer.append(strip.LEDlayer(s))
s.layer[2].setBits([0,1,2,3],25,00,00)

s.show()

while True:
    s.layer[0].shift(1)
    s.layer[1].shift(-2)
    s.layer[2].shift(-1)
    s.show()
    sleep(0.2)
