#!/usr/bin/env python2

import strip
import sys


s=strip.LEDstrip('/dev/ttyACM0',16,1)

s.clear()

s.layer[0].percent(int(sys.argv[1]),50,50,50)

s.show()
