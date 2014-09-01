#!/usr/bin/env python2

import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)


NUM_LEDS=16


if not ser.isOpen():
    ser.open()

def setBit(led,red,blu,gre):
    ser.write("%02d%03d%03d%03d\n"%(led,red,blu,gre))
#    print     "%02d%03d%03d%03d"  %(led,red,blu,gre)

def show():
    ser.write("show\n")

def setRing(red,blu,gre):
    for i in range(0,NUM_LEDS):
        setBit(i,red,blu,gre)

def clear():
    setRing(0,0,0)



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
    setRing(0,55,0)
    show()
    sleep(0.2)
    clear()
    show()
if (sys.argv[1] == "no"):
    setRing(55,0,0)
    show()
    sleep(0.2)
    clear()
    show()


ser.close()
