#!/usr/bin/env python2
import strip
import re
from time import sleep

from twisted.internet import protocol, reactor

strip = strip.LEDstrip()

def flash():
    strip.setRing(55,0,0)
    strip.show()
    sleep(0.2)
    strip.clear()
    strip.show()
    sleep(0.2)

class MyProcessProtocol(protocol.ProcessProtocol):

    def outReceived(self, data):
        print data
        if re.match(".*Failed.*",data):
            flash()

proc = MyProcessProtocol()
reactor.spawnProcess(proc, 'journalctl', ['journalctl', '-f', '/usr/bin/sshd'])
reactor.run()
