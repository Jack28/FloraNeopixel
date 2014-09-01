#!/usr/bin/env python2

import strip
from time import sleep
import sys

strip = strip.LEDstrip()



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

