#!/usr/bin/env python2

import strip
from time import sleep


s= strip.LEDstrip('/dev/ttyACM0',16,0)

s.clear()
#s.setRing(0,0,240)#160-160/16*i)

s.show()

newLayer1=strip.LEDlayer(s)
newLayer1.setBits(range(0,8),5,0,0)
newLayer2=strip.LEDlayer(s)
newLayer2.setBits(range(8,16),0,5,0)

#for i in range(0,8):
#    s.layer[0].setBit(i,0,0,10+5*(i-1))
#    s.layer[0].setBit(15-i,0,0,10+5*(i+1))

while True:
    s.layer.append(newLayer1)
    s.update()
    s.layer[0].shift(3)

    s.layer.append(newLayer2)
    s.update()

    s.show()

    sleep(1)

    s.layer.remove(newLayer1)
    s.layer.remove(newLayer2)
    s.update()

    s.clear()
    s.show()

    sleep(0.2)
