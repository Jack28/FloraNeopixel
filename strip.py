#!/usr/bin/env python2

import serial
from time import sleep

class LEDstrip:
    LEDstates = []

    def __init__(self,TTY='/dev/ttyACM0',NUM_LEDS=16):
        self.TTY=TTY
        self.NUM_LEDS=NUM_LEDS
        self.LEDstates = [(0,0,0) for i in range(0,self.NUM_LEDS)]
        self.ser = serial.Serial(TTY, 9600)

        if not self.ser.isOpen():
            self.ser.open()

    def __del__(self):
        self.ser.close()

    def setBit(self,led,red,blu,gre):
        self.LEDstates[led]=(red,blu,gre)
        self.ser.write("%02d%03d%03d%03d\n"%(led,red,blu,gre))
    #    print     "%02d%03d%03d%03d"  %(led,red,blu,gre)

    def show(self):
        self.ser.write("show\n")

    def setRing(self,red,blu,gre):
        for i in range(0,self.NUM_LEDS):
            self.setBit(i,red,blu,gre)

    def clear(self):
        self.setRing(0,0,0)

    def stateToRing(self):
        for i in range(0,self.NUM_LEDS):
            (r,g,b)=self.LEDstates[i]
            self.setBit(i,r if r>0 else 0,g if g>0 else 0,b if b>0 else 0)

    def shift(self,offset,n=1,delay=0):
        for i in range(0,n):
            tmp = self.LEDstates[::]
            self.LEDstates=tmp[offset:]+tmp[:offset]
            self.stateToRing()
            if n>1:
                self.show()
            sleep(delay)

    def dim(self,delay=0,stepsize=10):
        for a in range(0,255/stepsize):
            for i in range(0,self.NUM_LEDS):
                (r,g,b)=self.LEDstates[i]
                self.LEDstates[i]=(r-stepsize,g-stepsize,b-stepsize)
            self.stateToRing()
            self.show()
            sleep(delay)


if __name__ == "__main__":
    print "No, not that way"
