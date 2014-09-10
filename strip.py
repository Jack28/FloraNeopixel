#!/usr/bin/env python2

import serial
import random
from time import sleep
import sys

class LEDstrip:
    def __init__(self,TTY='/dev/ttyACM0',NUM_LEDS=16,layer=1):
        self.TTY=TTY
        self.NUM_LEDS=NUM_LEDS
        self.layer=[]
        for i in range(0,layer):
            self.layer.append(LEDlayer(self,NUM_LEDS))
        try:
            self.ser = serial.Serial(TTY, 9600)
            if not self.ser.isOpen():
                self.ser.open()
        except:
            print "ERROR opening serial connection"
            sys.exit()
        self.clear()
        self.show()

    def __del__(self):
        try:
            self.ser.close()
        except:
            0
        for i in self.layer:
            i.clear()

    def clear(self):
        for i in self.layer:
                i.clear()

    def setBit(self,led,red,gre,blu):
        for i in self.layer:
            (rtm,gtm,btm)=i.LEDstates[led]
            (red,gre,blu)=(red+rtm,gre+gtm,blu+btm)
        r = red if red < 255 else 255
        r = r   if r   > 0 else 0
        g = gre if gre < 255 else 255
        g = g   if g   > 0 else 0
        b = blu if blu < 255 else 255
        b = b   if b   > 0 else 0
        self.ser.write("%01x%02x%02x%02x"%(led,r,g,b))
#            print          "%01x%02x%02x%02x"%(l,r,g,b)

    def show(self):
        self.ser.write("s")

class LEDlayer:
    LEDstates = []

    def __init__(self,strip,NUM_LEDS=16):
        self.NUM_LEDS=NUM_LEDS
        self.strip=strip
        self.LEDstates = [(0,0,0) for i in range(0,self.NUM_LEDS)]

    def setBit(self,led,red,gre,blu):
        self.LEDstates[led]=(red,gre,blu)
        self.strip.setBit(led,red,gre,blu)
#        r = red if red < 255 else 255
#        r = r   if r   > 0 else 0
#        g = gre if gre < 255 else 255
#        g = g   if g   > 0 else 0
#        b = blu if blu < 255 else 255
#        b = b   if b   > 0 else 0
#        self.ser.write("%01x%02x%02x%02x"%(led,r,g,b))
#        print          "%01x%02x%02x%02x"%(led,r,g,b)

    def setBits(self,iterable,red,blu,gre):
        for i in iterable:
            self.setBit(i,red,blu,gre)

    def setRing(self,red,blu,gre):
        self.setBits(range(0,self.NUM_LEDS),red,blu,gre)

    def clear(self):
        self.setRing(0,0,0)

    def stateToRing(self):
        for i in range(0,self.NUM_LEDS):
            (r,g,b)=self.LEDstates[i]
            self.setBit(i,r,g,b)

    def dark(self,timeout=0.1):
        tmp = self.LEDstates[::]
        self.clear()
        self.strip.show()
        sleep(timeout)
        self.LEDstates = tmp
        self.stateToRing()
        self.strip.show()

    def shift(self,offset,n=1,delay=0):
        for i in range(0,n):
            tmp = self.LEDstates[::]
            self.LEDstates=tmp[offset:]+tmp[:offset]
            self.stateToRing()
            if n>1:
                self.strip.show()
            sleep(delay)

    def dim(self,brightnessOffset=255,delay=0,stepsize=10):
        tmp = self.LEDstates[::]
        for a in range(0,int(abs(brightnessOffset)/abs(stepsize))):
            for i in range(0,self.NUM_LEDS):
                (r,g,b)=self.LEDstates[i]
                (r0,g0,b0)=tmp[i]
                self.LEDstates[i]=(
                        0 if r0==0 else r-(stepsize),
                        0 if g0==0 else g-(stepsize),
                        0 if b0==0 else b-(stepsize))
            self.stateToRing()
            self.strip.show()
            sleep(delay)

#    def rotateColor(self):

    def wheel(self,pos):
        i = 256/self.NUM_LEDS*pos
        if i < 85:
            return (i*3,255-i*3,0)
        elif i < 170:
            return (255-(i-85)*3,0,(i-85)*3)
        else:
            return (0,(i-170)*3,255-(i-170)*3)


    def rainbow(self):
        for i in range(0,self.NUM_LEDS):
            self.LEDstates[i]=self.wheel(i)
        self.stateToRing()
        self.strip.show()

    def randomColor(self):
        for i in range(0,self.NUM_LEDS):
            self.LEDstates[i]=(random.randint(0,256)/2,random.randint(0,256),random.randint(0,256))
        self.stateToRing()
        self.strip.show()

    def shiftColor(self,offset):
        c = 256/self.NUM_LEDS
        for i in range(0,self.NUM_LEDS):
            (r,g,b) = self.LEDstates[i]
            
            self.LEDstates[i]=()


if __name__ == "__main__":
    print "No, not that way"
