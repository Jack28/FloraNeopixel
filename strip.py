#!/usr/bin/env python2

import serial
from time import sleep

class LEDstrip:
    def __init__(self,TTY='/dev/ttyACM0',NUM_LEDS=16):
        self.TTY=TTY
        self.NUM_LEDS=NUM_LEDS
        self.ser = serial.Serial(TTY, 9600)

        if not self.ser.isOpen():
            self.ser.open()

    def __del__(self):
        self.ser.close()

    def setBit(self,led,red,blu,gre):
        self.ser.write("%02d%03d%03d%03d\n"%(led,red,blu,gre))
    #    print     "%02d%03d%03d%03d"  %(led,red,blu,gre)

    def show(self):
        self.ser.write("show\n")

    def setRing(self,red,blu,gre):
        for i in range(0,self.NUM_LEDS):
            self.setBit(i,red,blu,gre)

    def clear(self):
        self.setRing(0,0,0)



if __name__ == "__main__":
    print "No, not that way"
