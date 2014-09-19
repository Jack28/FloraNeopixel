#!/usr/bin/env python2

import strip
from time import sleep


s= strip.LEDstrip('/dev/ttyACM0',16,1)

s.clear()

s.show()


newLayer2=strip.LEDlayer(s)
###newLayer2.rainbow(10)

#for i in range(0,8):
#    s.layer[0].setBit(i,0,0,10+5*(i-1))
#    s.layer[0].setBit(15-i,0,0,10+5*(i+1))

while True:
    s.layer[0].setBits(range(0,16),0,55,0)
    newLayer2.setBits(range(0,8),0,0,0)
    newLayer2.setBits(range(8,16),250,0,0)

    for i in range(0,3):
        s.layer[0].transition(newLayer2)
        sleep(1)
        s.show()

        s.layer[0].setBits(range(0,16),0,55,0)
        s.show()
        sleep(1)


#    s.layer[0].rainbow(10)
#    newLayer2.rainbow(10)
#    for i in range(0,9):
#        s.layer[0].transition(newLayer2)
#        newLayer2.shift(2)
#        s.show()
