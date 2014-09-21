#!/usr/bin/env python2

import strip
from time import sleep
import sys

strip = strip.LEDstrip()

if len(sys.argv) > 1 and sys.argv[1] == "ok":
    strip.layer[0].setRing(0,55,0)
    strip.show()
    sleep(0.2)
    strip.layer[0].dim(-65,0.03)
else:
    for i in range(0,3):
        strip.layer[0].setRing(55,0,0)
        strip.show()
        sleep(0.2)
        strip.clear()
        strip.show()
        sleep(0.2)
