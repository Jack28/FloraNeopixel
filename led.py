#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()


red=0
gre=0
blu=0
led=0

q=10

#while 1==1:
##    setBit(led,red,blu,gre)
##    setBit((led-2)%16,0,0,0)
##    led=(led+1)%16
#    setRing(red,gre,blu)
#    red+=q
#    if red>255:
#        red=0
#        gre+=q
#        if gre>255:
#            gre=0
#            blu+=q
#
#    show()


import sys

if (sys.argv[1] == "ok"):
    strip.setRing(0,55,0)
    strip.show()
    sleep(0.2)
    strip.clear()
    strip.show()
if (sys.argv[1] == "no"):
    strip.setRing(55,0,0)
    strip.show()
    sleep(0.2)
    strip.clear()
    strip.show()

