#!/usr/bin/env python2

import strip
import sys
from time import sleep


strip = strip.LEDstrip()


def showState(num):
    strip.clear()
    strip.show()

    state = bin(int(num))

    state = state[2:]

    for i in range(0,len(state)):
        if state[len(state)-i-1] == "1":
            strip.layer[0].setBit(15-i,0,0,255)

    strip.show()

for i in range(0,int(sys.argv[1])):
    #sys.argv[1]
    showState(int(i))
