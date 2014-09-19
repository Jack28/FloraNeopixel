#!/usr/bin/env python2

import strip
from time import sleep


s= strip.LEDstrip('/dev/ttyACM0',16,5)

s.clear()
#s.setRing(0,0,240)#160-160/16*i)
s.layer[0].setBits([0],0,0,150)
s.layer[1].setBits([1],0,0,150)
s.layer[2].setBits([2],0,0,150)
s.layer[3].setBits([3],0,0,150)

s.layer[4].setRing(0,5,0)


s.show()

while True:
    for l in range(0,len(s.layer)):
        for i in range(0,l):
            s.layer[i].shift(1)
        s.show()
        sleep(0.5)

    for i in range(0,16):
        for j in range(0,4):
             s.layer[j].shift(1)
        s.show()
    sleep(0.2)
    s.show()
    sleep(0.5)
