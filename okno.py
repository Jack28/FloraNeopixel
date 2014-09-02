#!/usr/bin/env python2

import strip
from time import sleep
import sys

strip = strip.LEDstrip()



if (sys.argv[1] == "ok"):
    strip.setRing(0,55,0)
    strip.show()
    sleep(0.2)
    strip.dim(0.03)
if (sys.argv[1] == "no"):
    for i in range(0,3):
        strip.setRing(55,0,0)
        strip.show()
        sleep(0.2)
        strip.clear()
        strip.show()
        sleep(0.2)

