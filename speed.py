#!/usr/bin/env python2

import strip
from time import sleep


strip = strip.LEDstrip()

strip.clear()
strip.show()

# before optimisation
# 0:17.66elapsed
# after
# 0:19.14elapsed
# after ssprintf
# 0:15.88elapsed
# after no \n, show -> s
# 0:13.28elapsed
# with layers
# 1:48.88elapsed
# with optimised layers
# 0:13.31elapsed
# more optimisations
# 0:08.63elapsed

for i in range(0,10000):
    strip.layer[0].setBit(i%16,i%255,i/40,0)
    strip.show()
