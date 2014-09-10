#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()

strip.clear()
#strip.setRing(0,0,240)#160-160/16*i)
strip.layer[0].randomColor()
strip.layer[0].rainbow()
strip.show()

time = 20
q=2
while True:
    for k in range(0,3):
        strip.layer[0].dark(1)
        for j in range(0,5):
            strip.layer[0].dim(80,0.01,8)
            strip.layer[0].dim(80,0.01,-8)

            strip.layer[0].dim(50,0,50)
            sleep(0.05)
            strip.layer[0].dim(50,0,-25)
            sleep(0.2)
            strip.layer[0].dim(50,0,50)
            sleep(0.05)
            strip.layer[0].dim(50,0,-25)
            sleep(0.2)

            strip.layer[0].dark(0.1)
            sleep(0.1)
        #    strip.randomColor()

        for i in range(0,10):
            strip.layer[0].dark((10-i)/10)
            sleep(0.05)

        strip.layer[0].dim(50,0,50)
        sleep(0.05)
        strip.layer[0].dim(50,0,-25)
        sleep(0.2)
        strip.layer[0].dim(50,0,50)
        sleep(0.05)
        strip.layer[0].dim(50,0,-25)
        sleep(0.2)
    for k in range(0,200):
        strip.layer[0].shift(1)
        strip.show()
