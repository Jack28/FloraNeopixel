#!/usr/bin/env python2
import strip
import re
from time import sleep

from twisted.internet import protocol, reactor

strip = strip.LEDstrip()

def flash():
    for i in range(0,16,4):
        strip.layer[0].setBits(range(i,i+4),55,0,0)
        strip.show()
        sleep(0.2)
    strip.layer[0].dim(-255,0.1)

class MyProcessProtocol(protocol.ProcessProtocol):

    def outReceived(self, data):
        print data
        if re.match(".*Failed.*",data):
            flash()

proc = MyProcessProtocol()
reactor.spawnProcess(proc, 'journalctl', ['journalctl', '-f', '/usr/bin/sshd'])
reactor.run()
