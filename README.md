FloraNeopixel
=============

Arduino Flora with NeoPixel 16 LED ring Python library


This repository contains the Adafruit NeoPixel "strandtest" animations with some additions.

PLUS the an interpreter that listens on the Arduinos serial console for commands in the following form:

ABBCCDD (A = LED id, B = red, C = green, D = blue. All values in HEX)
s   (show the set values on the LED ring)
.   (0.01s delay)


In addition to the interpreter code for the Arduino there is a Python library with methods to controll the LED ring.

Examples are also provided for CPU monitoring, fancy animations, save an replay in BASH, portscan detector, SSH auth failure indicator, ...
