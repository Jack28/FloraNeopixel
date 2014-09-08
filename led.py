#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()

strip.clear()
#strip.setRing(0,0,240)#160-160/16*i)
strip.randomColor()
strip.rainbow()
strip.show()

time = 20
q=2
while True:
#    for k in range(0,3):
#        strip.dark(1)
#        for j in range(0,5):
#            strip.dim(80,0.01,8)
#            strip.dim(80,0.01,-8)
#
#            strip.dim(50,0,50)
#            sleep(0.05)
#            strip.dim(50,0,-25)
#            sleep(0.2)
#            strip.dim(50,0,50)
#            sleep(0.05)
#            strip.dim(50,0,-25)
#            sleep(0.2)
#
#            strip.dark(0.1)
#            sleep(0.1)
#        #    strip.randomColor()
#
#        for i in range(0,10):
#            strip.dark((10-i)/10)
#            sleep(0.05)
#
#        strip.dim(50,0,50)
#        sleep(0.05)
#        strip.dim(50,0,-25)
#        sleep(0.2)
#        strip.dim(50,0,50)
#        sleep(0.05)
#        strip.dim(50,0,-25)
#        sleep(0.2)
    for k in range(0,10):
        strip.shift(2,k,(20-k)/10)

