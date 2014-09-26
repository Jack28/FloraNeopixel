#!/usr/bin/env python2

import strip
from time import sleep
import math
import psutil



s=strip.LEDstrip('/dev/ttyACM0',16,2)

layer1=strip.LEDlayer(s)

s.clear()

s.show()


while True:
    cpu = psutil.cpu_percent(interval=.2)
    layer1.clear()
    layer1.percent(int(cpu),50,0,0)
    s.layer[0].transition(layer1,25)
    s.show()

