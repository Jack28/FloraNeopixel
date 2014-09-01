#!/usr/bin/env python2

import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 4800)

def lazy_open():
    if not ser.isOpen():
        ser.open()

def lazy_close():
    if ser.isOpen():
        ser.close()

def setBit(led,red,blu,gre):
    lazy_open()
    ser.write("%02d%03d%03d%03d\n"%(led,red,blu,gre))
    print     "%02d%03d%03d%03d"  %(led,red,blu,gre)
    lazy_close()

def show():
    lazy_open()
    ser.write("show\n")
    lazy_close()




red=0
gre=200
blu=0
led=0

while 1==1:
    setBit(led,red,blu,gre)
    setBit((led-2)%16,0,0,0)
    led=(led+1)%16;

    show()
    sleep(0.02)



ser.close()
