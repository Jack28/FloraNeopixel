#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()

strip.clear()
strip.show()

# before optimisation
# 0:17.66elapsed
# after
# 0:19.14elapsed
# after ssprintf
# 0:15.88elapsed

for i in range(0,10000):
    strip.setBit(i%16,i%255,i/40,0)
    strip.show()
